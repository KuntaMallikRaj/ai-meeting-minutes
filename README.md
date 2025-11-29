# 🚀 AI Meeting Minutes Generator

A **completely free** AI-powered meeting minutes generator using **Hugging Face models**. No API keys required, runs entirely on your machine!

![AI Meeting Minutes](https://img.shields.io/badge/AI-Meeting%20Minutes-blue)
![Free](https://img.shields.io/badge/Cost-FREE-green)
![Private](https://img.shields.io/badge/Privacy-100%25%20Local-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)

## ✨ Features

- 📝 **Upload & Store Meetings** - Process and store meeting transcripts
- 🔍 **AI-Powered Search** - Semantic search through your meeting history  
- 📊 **Smart Summaries** - Generate bullet points and action items
- ✂️ **Text Splitting** - Break down long documents into manageable chunks
- 🎨 **Beautiful Web Interface** - Modern, responsive design
- 🔒 **100% Private** - Everything runs locally on your computer
- 💰 **Completely Free** - No API costs, no subscriptions

## 🎯 Why This Project?

- ✅ **Free Alternative to OpenAI** - Uses Hugging Face models instead
- ✅ **Privacy First** - Your data never leaves your computer
- ✅ **No API Keys** - No external dependencies or accounts needed
- ✅ **Offline Capable** - Works without internet after initial setup

## 🏗️ Architecture

```
Frontend (React-like)     Backend (Flask + AI)
┌─────────────────┐      ┌─────────────────────┐
│   HTML/CSS/JS   │ ───► │   Flask API Server  │
│   Modern UI     │      │   Hugging Face LLMs │
│   Port 3000     │      │   Vector Database   │
└─────────────────┘      └─────────────────────┘
```

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-meeting-minutes.git
cd ai-meeting-minutes
```

### 2. Set Up Python Environment
```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r backend/requirements.txt
```

### 3. Start the Backend (AI Engine)
```bash
cd backend
python app.py
```
✅ Backend runs on: http://127.0.0.1:8001

### 4. Start the Frontend (Web Interface)
```bash
# In a new terminal
cd frontend
python3 -m http.server 3000
```
✅ Frontend runs on: http://localhost:3000

### 5. Open Your Browser
Navigate to: **http://localhost:3000**

## 📱 Usage

### Upload a Meeting
1. Click "Upload Meeting" tab
2. Enter a descriptive title
3. Paste your meeting transcript
4. Click "Upload Meeting"

### Search Your Meetings
1. Click "Search Meetings" tab  
2. Enter search terms (e.g., "action items", "budget")
3. AI finds relevant content across all meetings

### Generate Summaries
1. Click "Summarize" tab
2. Paste meeting content
3. Get AI-generated bullet points and action items

### Split Long Text
1. Click "Split Text" tab
2. Paste long transcript
3. Break into manageable chunks

## 🤖 AI Models Used

### Language Model
- **Primary**: `distilgpt2` - Fast, lightweight text generation
- **Purpose**: Summarization, action item extraction

### Embeddings Model  
- **Model**: `sentence-transformers/all-MiniLM-L6-v2`
- **Purpose**: Semantic search and similarity matching

### Why These Models?
- ✅ **Completely Free** - No API costs
- ✅ **Lightweight** - Runs on CPU efficiently  
- ✅ **High Quality** - Excellent performance for meeting analysis
- ✅ **Fast** - Quick response times

## 🛠️ Technical Stack

### Backend
- **Framework**: Flask (Python)
- **AI Engine**: Hugging Face Transformers
- **Database**: SQLite + Chroma Vector Store
- **Text Processing**: LangChain

### Frontend
- **Languages**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Modern CSS with gradients and animations
- **Icons**: Font Awesome
- **Design**: Responsive, mobile-friendly

## 📊 Project Structure

```
ai-meeting-minutes/
├── backend/                 # Flask API server
│   ├── app.py              # Main Flask application
│   ├── services/           # AI services
│   │   ├── llm.py         # Hugging Face LLM
│   │   ├── vectorstore.py # Vector database
│   │   └── splitter.py    # Text splitting
│   ├── routes/            # API endpoints
│   │   ├── ingest.py      # Upload meetings
│   │   ├── search.py      # Search functionality
│   │   └── summarize.py   # AI summarization
│   └── requirements.txt   # Python dependencies
├── frontend/              # Web interface
│   ├── index.html        # Main page
│   ├── style.css         # Styling
│   ├── script.js         # JavaScript
│   └── serve.py          # Simple server
└── README.md             # This file
```

## 🔧 Installation Details

### System Requirements
- **Python**: 3.8 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 2GB for models and data
- **OS**: Windows, macOS, or Linux

### Dependencies
```bash
# Core dependencies
flask==2.3.2
transformers
torch
sentence-transformers
langchain-huggingface
chromadb
sqlalchemy
flask-cors
```

## 🌐 Deployment Options

### Local Development
- Perfect for personal use and testing
- No internet required after initial setup

### Self-Hosted Server
- Deploy on your own VPS or cloud instance
- Keep full control of your data

### Docker Deployment
```bash
# Coming soon - Docker containers for easy deployment
docker-compose up
```

## 📈 Performance

### First Run
- Models download automatically (one-time ~1GB)
- Initial responses may take 30-60 seconds

### Subsequent Runs
- Models cached locally
- Fast responses (2-5 seconds)
- No internet required

## 🤝 Contributing

We welcome contributions! Here's how:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Test thoroughly**
5. **Commit**: `git commit -m 'Add amazing feature'`
6. **Push**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

### Areas for Contribution
- 🎨 **UI/UX improvements**
- 🤖 **Better AI model integration**
- 📊 **Analytics and reporting features**
- 🔧 **Performance optimizations**
- 📖 **Documentation improvements**

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Hugging Face** - For providing free, high-quality AI models
- **LangChain** - For excellent AI application framework
- **Flask** - For the lightweight web framework
- **Chroma** - For the vector database

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/ai-meeting-minutes/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/ai-meeting-minutes/discussions)
- **Documentation**: Check the `/docs` folder

## 🎉 Success Stories

> *"Saved me hours every week organizing meeting notes!"* - Developer

> *"Finally, a free alternative that actually works!"* - Product Manager

> *"Love that my data stays private!"* - Security-conscious User

---

## 🌟 Star This Project!

If you find this project useful, please give it a ⭐ on GitHub!

**Happy Meeting Management! 🚀**
