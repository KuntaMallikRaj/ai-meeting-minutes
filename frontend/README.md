# AI Meeting Minutes - Frontend

A simple, beautiful web interface for your AI Meeting Minutes application powered by Hugging Face models.

## 🚀 Quick Start

### Option 1: Simple Python Server (Recommended)
```bash
cd /Users/MallikRaj.Kunta/Desktop/meeting-minutes-ai/frontend
python3 -m http.server 3000
```

Then open: http://localhost:3000

### Option 2: Live Server (VS Code Extension)
1. Install "Live Server" extension in VS Code
2. Right-click on `index.html` 
3. Select "Open with Live Server"

### Option 3: Direct File Access
Simply double-click `index.html` to open in your browser.

## 🎯 Features

### 📝 Upload Meetings
- Add meeting title and transcript
- AI processes and stores for future search

### 🔍 Search Meetings  
- Search through all uploaded meetings
- AI-powered semantic search finds relevant content

### 📊 Summarize Content
- Get AI-generated summaries of meeting content
- Extract action items automatically

### ✂️ Split Long Text
- Break long transcripts into manageable chunks
- Useful for processing very long meetings

## 🛠 How to Use

1. **Start your backend server first:**
   ```bash
   cd /Users/MallikRaj.Kunta/Desktop/meeting-minutes-ai/backend
   /Users/MallikRaj.Kunta/Desktop/meeting-minutes-ai/.venv/bin/python app.py
   ```

2. **Start the frontend:**
   ```bash
   cd /Users/MallikRaj.Kunta/Desktop/meeting-minutes-ai/frontend
   python3 -m http.server 3000
   ```

3. **Open your browser:** http://localhost:3000

4. **Start using the interface:**
   - Upload a meeting transcript
   - Search for specific topics
   - Generate summaries
   - Split long text

## 🎨 Interface Overview

- **Clean, modern design** with gradient backgrounds
- **Responsive layout** works on desktop, tablet, and mobile
- **Real-time feedback** with loading indicators and toast notifications
- **Intuitive tabs** for different functions
- **Keyboard shortcuts** (Ctrl+1-4 for tab switching)

## 🔧 Technical Details

- **Pure HTML/CSS/JavaScript** - no frameworks needed
- **Responsive design** using CSS Grid and Flexbox
- **Modern UI** with glassmorphism effects
- **API integration** with your Hugging Face backend
- **Error handling** with user-friendly messages

## 🌐 Browser Compatibility

- ✅ Chrome (recommended)
- ✅ Firefox  
- ✅ Safari
- ✅ Edge

## 📱 Mobile Friendly

The interface is fully responsive and works great on:
- 📱 Smartphones
- 📱 Tablets  
- 💻 Desktop computers

## 🚨 Troubleshooting

### Frontend not connecting to backend?
1. Make sure your backend is running on port 8001
2. Check the console for error messages
3. Verify the API_BASE_URL in script.js

### Styling looks broken?
1. Make sure all CSS files are loading
2. Check browser developer tools for errors
3. Try hard refresh (Ctrl+F5)

### Features not working?
1. Check browser console for JavaScript errors
2. Ensure backend is running and accessible
3. Try different browser

## 🎉 You're All Set!

Your beautiful AI Meeting Minutes interface is ready to use with your free Hugging Face backend!
