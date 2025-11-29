import os
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

def get_llm(model: str = "distilgpt2", temperature: float = 0.7):
    """
    Initialize Hugging Face LLM pipeline for text generation
    Using a lightweight, fast model suitable for summarization
    """
    # Use a smaller, faster model for better performance
    model_name = "distilgpt2"  # Fast and lightweight
    
    try:
        # Initialize the pipeline with the model
        pipe = pipeline(
            "text-generation",
            model=model_name,
            tokenizer=model_name,
            max_new_tokens=150,  # Reduced for faster responses
            temperature=temperature,
            do_sample=True,
            device=-1,  # Force CPU for compatibility
            return_full_text=False,
            pad_token_id=50256  # Explicit pad token for distilgpt2
        )
        
        return HuggingFacePipeline(pipeline=pipe)
    except Exception as e:
        print(f"Error loading model {model_name}: {e}")
        # Fallback with even more basic settings
        pipe = pipeline(
            "text-generation",
            model="gpt2",
            max_new_tokens=100,
            temperature=temperature,
            do_sample=True,
            device=-1,
            return_full_text=False
        )
        return HuggingFacePipeline(pipeline=pipe)

def make_summary_chain():
    prompt = PromptTemplate(
        input_variables=["transcript"],
        template=(
            "Please summarize the following meeting transcript into 5-7 clear bullet points:\n\n"
            "Transcript: {transcript}\n\n"
            "Summary:"
        )
    )
    return prompt | get_llm() | StrOutputParser()

def make_action_item_chain():
    prompt = PromptTemplate(
        input_variables=["transcript"],
        template=(
            "Extract all clear action items from the following meeting transcript:\n\n"
            "Transcript: {transcript}\n\n"
            "Action Items:"
        )
    )

    chain = prompt | get_llm() | StrOutputParser()
    return chain
