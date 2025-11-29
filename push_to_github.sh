#!/bin/bash

echo "🚀 Pushing AI Meeting Minutes to GitHub..."
echo "=========================================="

# Check if we're in the right directory
if [ ! -f "README.md" ]; then
    echo "❌ Please run this script from the project root directory"
    exit 1
fi

# Set your GitHub repository URL
REPO_URL="https://github.com/KuntaMallikRaj/ai-meeting-minutes.git"

# Initialize git if not already done
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
    echo "✅ Git initialized"
fi

# Configure git user (replace with your details)
echo "👤 Configuring Git user..."
git config user.name "KuntaMallikRaj"
git config user.email "mallikraj.kunta@example.com"

# Add remote origin if not exists
if ! git remote | grep -q origin; then
    echo "🔗 Adding GitHub remote..."
    git remote add origin $REPO_URL
    echo "✅ Remote added: $REPO_URL"
else
    echo "🔄 Updating remote URL..."
    git remote set-url origin $REPO_URL
fi

# Stage all files
echo "📦 Staging all files..."
git add .

# Check if there are files to commit
if git diff --staged --quiet; then
    echo "⚠️  No changes to commit"
    echo "📤 Attempting to push existing commits..."
    git push -u origin main 2>/dev/null || git push -u origin master 2>/dev/null
else
    # Commit with a descriptive message
    COMMIT_MSG="🎉 Initial commit: Free AI Meeting Minutes Generator with Hugging Face

Features:
- 🤖 Free AI models (Hugging Face) - no API costs
- 📝 Upload and search meeting transcripts  
- 📊 Generate summaries and action items
- ✂️ Split long text into chunks
- 🎨 Beautiful responsive web interface
- 🔒 100% private - runs locally
- 🐳 Docker support
- 🚀 Multiple deployment options

Created by: Mallik Raj Kunta
Tech Stack: Python Flask + HTML/CSS/JS + Hugging Face Transformers"

    echo "💬 Committing changes..."
    git commit -m "$COMMIT_MSG"
    echo "✅ Files committed"

    # Push to GitHub
    echo "🚀 Pushing to GitHub..."
    if git push -u origin main; then
        echo "✅ Successfully pushed to main branch"
    elif git push -u origin master; then
        echo "✅ Successfully pushed to master branch"
    else
        echo "❌ Failed to push. You may need to create the repository on GitHub first."
        echo "💡 Go to https://github.com/KuntaMallikRaj and create a new repository named 'ai-meeting-minutes'"
        exit 1
    fi
fi

echo ""
echo "🎉 SUCCESS! Your project is now on GitHub!"
echo "🌐 Repository URL: $REPO_URL"
echo "📱 View your project: https://github.com/KuntaMallikRaj/ai-meeting-minutes"
echo ""
echo "📋 Next Steps:"
echo "   1. Go to your GitHub repository"
echo "   2. Edit the repository description"
echo "   3. Add topics/tags for better discoverability"
echo "   4. Consider starring your own repo! ⭐"