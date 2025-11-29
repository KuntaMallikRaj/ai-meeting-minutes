#!/bin/bash

echo "📤 Deploying to GitHub..."
echo "========================"

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git not initialized. Please run 'git init' first"
    exit 1
fi

# Check if remote origin exists
if ! git remote | grep -q origin; then
    echo "❌ No GitHub remote found."
    echo "💡 Add your GitHub repo with:"
    echo "   git remote add origin https://github.com/KuntaMallikRaj/ai-meeting-minutes.git"
    exit 1
fi

# Add all files
echo "📁 Adding files to git..."
git add .

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "✅ No changes to commit"
else
    # Commit with timestamp
    COMMIT_MSG="Update: $(date '+%Y-%m-%d %H:%M:%S')"
    echo "💬 Committing with message: $COMMIT_MSG"
    git commit -m "$COMMIT_MSG"
fi

# Push to GitHub
echo "🚀 Pushing to GitHub..."
git push origin main

echo ""
echo "✅ Successfully deployed to GitHub!"
echo "🌐 Your repository: $(git remote get-url origin)"
echo "📱 Share your project with the world!"
