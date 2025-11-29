#!/usr/bin/env python3
"""
Test script to verify Hugging Face models are working correctly
"""

import sys
sys.path.append('/Users/MallikRaj.Kunta/Desktop/meeting-minutes-ai/backend')

from services.llm import get_llm, make_summary_chain
from services.vectorstore import get_chroma_store

def test_llm():
    """Test the LLM functionality"""
    print("Testing Hugging Face LLM...")
    try:
        llm = get_llm()
        test_prompt = "Hello, how are you today?"
        response = llm.invoke(test_prompt)
        print(f"✅ LLM Test Successful!")
        print(f"Input: {test_prompt}")
        print(f"Output: {response}")
        return True
    except Exception as e:
        print(f"❌ LLM Test Failed: {e}")
        return False

def test_embeddings():
    """Test the embedding functionality"""
    print("\nTesting Hugging Face Embeddings...")
    try:
        store = get_chroma_store()
        print("✅ Embeddings Test Successful!")
        print("Vector store initialized with Hugging Face embeddings")
        return True
    except Exception as e:
        print(f"❌ Embeddings Test Failed: {e}")
        return False

def test_summary_chain():
    """Test the summary chain"""
    print("\nTesting Summary Chain...")
    try:
        chain = make_summary_chain()
        test_transcript = """
        John: Good morning everyone. Today we need to discuss the quarterly budget.
        Sarah: I've prepared the financial reports. We're 15% over budget in marketing.
        Mike: We should reduce the advertising spend by 20% next quarter.
        John: Agreed. Let's also review the hiring plan.
        """
        
        response = chain.invoke({"transcript": test_transcript})
        print("✅ Summary Chain Test Successful!")
        print(f"Summary: {response}")
        return True
    except Exception as e:
        print(f"❌ Summary Chain Test Failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Testing Hugging Face Integration...")
    print("=" * 50)
    
    tests = [
        test_embeddings,
        test_llm,
        test_summary_chain
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
            results.append(False)
    
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    print(f"✅ Passed: {sum(results)}/{len(results)}")
    print(f"❌ Failed: {len(results) - sum(results)}/{len(results)}")
    
    if all(results):
        print("\n🎉 All tests passed! Your Hugging Face integration is working!")
    else:
        print("\n⚠️  Some tests failed. Please check the error messages above.")
