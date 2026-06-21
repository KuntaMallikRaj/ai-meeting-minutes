// API Configuration
// Empty string = same origin, so the UI talks to whichever host serves it
// (localhost in dev, the Render URL in production). No hardcoded host.
const API_BASE_URL = '';

// DOM Elements
const loadingOverlay = document.getElementById('loadingOverlay');
const toast = document.getElementById('toast');

// Utility Functions
function showLoading() {
    loadingOverlay.style.display = 'flex';
}

function hideLoading() {
    loadingOverlay.style.display = 'none';
}

function showToast(message, type = 'info') {
    toast.textContent = message;
    toast.className = `toast ${type}`;
    toast.classList.add('show');
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 4000);
}

// Tab Navigation
function showTab(tabName) {
    // Hide all tab contents
    const tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(content => content.classList.remove('active'));
    
    // Remove active class from all tab buttons
    const tabButtons = document.querySelectorAll('.tab-btn');
    tabButtons.forEach(btn => btn.classList.remove('active'));
    
    // Show selected tab content
    document.getElementById(tabName).classList.add('active');
    
    // Add active class to clicked button
    event.target.classList.add('active');
}

// API Functions
async function makeAPIRequest(endpoint, data, method = 'POST') {
    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

// Upload Meeting Form Handler
document.getElementById('uploadForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const title = document.getElementById('meetingTitle').value;
    const transcript = document.getElementById('meetingTranscript').value;
    
    if (!title || !transcript) {
        showToast('Please fill in both title and transcript', 'error');
        return;
    }
    
    showLoading();
    
    try {
        const response = await makeAPIRequest('/ingest/upload', {
            title: title,
            transcript: transcript
        });
        
        hideLoading();
        showToast('Meeting uploaded successfully!', 'success');
        
        // Clear form
        document.getElementById('meetingTitle').value = '';
        document.getElementById('meetingTranscript').value = '';
        
    } catch (error) {
        hideLoading();
        showToast('Failed to upload meeting. Please try again.', 'error');
        console.error('Upload error:', error);
    }
});

// Search Form Handler
document.getElementById('searchForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const query = document.getElementById('searchQuery').value;
    
    if (!query) {
        showToast('Please enter a search query', 'error');
        return;
    }
    
    showLoading();
    
    try {
        const response = await makeAPIRequest('/search', {
            query: query
        });
        
        hideLoading();
        displaySearchResults(response);
        showToast('Search completed!', 'success');
        
    } catch (error) {
        hideLoading();
        showToast('Search failed. Please try again.', 'error');
        console.error('Search error:', error);
    }
});

// Summarize Form Handler
document.getElementById('summarizeForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const content = document.getElementById('summaryText').value;
    
    if (!content) {
        showToast('Please enter content to summarize', 'error');
        return;
    }
    
    showLoading();
    
    try {
        const response = await makeAPIRequest('/summarize', {
            content: content
        });
        
        hideLoading();
        displaySummaryResults(response);
        showToast('Summary generated!', 'success');
        
    } catch (error) {
        hideLoading();
        showToast('Summarization failed. Please try again.', 'error');
        console.error('Summarize error:', error);
    }
});

// Split Text Form Handler
document.getElementById('splitForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const text = document.getElementById('splitText').value;
    
    if (!text) {
        showToast('Please enter text to split', 'error');
        return;
    }
    
    showLoading();
    
    try {
        const response = await makeAPIRequest('/split', {
            text: text
        });
        
        hideLoading();
        displaySplitResults(response);
        showToast('Text split successfully!', 'success');
        
    } catch (error) {
        hideLoading();
        showToast('Text splitting failed. Please try again.', 'error');
        console.error('Split error:', error);
    }
});

// Display Functions
function displaySearchResults(response) {
    const resultsContainer = document.getElementById('searchResults');

    // The API returns { answer, contexts }.
    const answer = response.answer;
    const contexts = response.contexts || [];

    if (!answer && contexts.length === 0) {
        resultsContainer.innerHTML = `
            <div class="result-item">
                <h3><i class="fas fa-info-circle"></i> No Results Found</h3>
                <p>No meetings found matching your search query. Try uploading some meetings first or using different keywords.</p>
            </div>
        `;
        return;
    }

    let html = '';

    if (answer) {
        html += `
            <div class="result-item">
                <h3><i class="fas fa-robot"></i> Answer</h3>
                <p>${answer}</p>
            </div>
        `;
    }

    if (contexts.length > 0) {
        html += `<h3><i class="fas fa-search"></i> Source Excerpts (${contexts.length})</h3>`;
        contexts.forEach((ctx, index) => {
            html += `
                <div class="result-item">
                    <h4>Excerpt ${index + 1}</h4>
                    <p>${ctx}</p>
                </div>
            `;
        });
    }

    resultsContainer.innerHTML = html;
}

function displaySummaryResults(response) {
    const resultsContainer = document.getElementById('summaryResults');
    
    let html = '<h3><i class="fas fa-file-alt"></i> Summary Results</h3>';
    
    if (response.summary) {
        html += `
            <div class="result-item">
                <h4><i class="fas fa-clipboard-list"></i> Summary</h4>
                <p>${response.summary}</p>
            </div>
        `;
    }
    
    if (response.action_items) {
        html += `
            <div class="result-item">
                <h4><i class="fas fa-tasks"></i> Action Items</h4>
                <p>${response.action_items}</p>
            </div>
        `;
    }
    
    if (!response.summary && !response.action_items) {
        html += `
            <div class="result-item">
                <h4><i class="fas fa-exclamation-triangle"></i> No Summary Generated</h4>
                <p>The AI model couldn't generate a summary. This might be because the text is too short or the model is still processing.</p>
            </div>
        `;
    }
    
    resultsContainer.innerHTML = html;
}

function displaySplitResults(response) {
    const resultsContainer = document.getElementById('splitResults');
    
    if (!response.chunks || response.chunks.length === 0) {
        resultsContainer.innerHTML = `
            <div class="result-item">
                <h3><i class="fas fa-info-circle"></i> No Chunks Created</h3>
                <p>The text was too short to split into multiple chunks.</p>
            </div>
        `;
        return;
    }
    
    let html = `<h3><i class="fas fa-cut"></i> Text Split Results</h3>`;
    html += `<p><strong>Total chunks created:</strong> ${response.total_chunks}</p>`;
    
    response.chunks.forEach((chunk, index) => {
        html += `
            <div class="chunk-item">
                <div class="chunk-header">
                    <i class="fas fa-puzzle-piece"></i> Chunk ${index + 1} 
                    <span style="color: #888; font-weight: normal;">(${chunk.length} characters)</span>
                </div>
                <div class="chunk-content">${chunk}</div>
            </div>
        `;
    });
    
    resultsContainer.innerHTML = html;
}

// Initialize the app
document.addEventListener('DOMContentLoaded', () => {
    console.log('AI Meeting Minutes Frontend Loaded');
    showToast('Welcome! Your AI Meeting Assistant is ready.', 'info');
    
    // Check if backend is running
    fetch(`${API_BASE_URL}/health`)
        .then(response => response.json())
        .then(data => {
            if (data.status === 'ok') {
                showToast('✅ Connected to AI backend successfully!', 'success');
            }
        })
        .catch(error => {
            showToast('⚠️ Backend not connected.', 'error');
            console.error('Backend connection error:', error);
        });
});

// Keyboard shortcuts
document.addEventListener('keydown', (e) => {
    // Ctrl/Cmd + 1-4 for tab switching
    if ((e.ctrlKey || e.metaKey) && e.key >= '1' && e.key <= '4') {
        e.preventDefault();
        const tabs = ['upload', 'search', 'summarize', 'split'];
        const tabIndex = parseInt(e.key) - 1;
        if (tabs[tabIndex]) {
            // Simulate clicking the tab button
            const tabButtons = document.querySelectorAll('.tab-btn');
            if (tabButtons[tabIndex]) {
                tabButtons[tabIndex].click();
            }
        }
    }
});

// Add some helpful tooltips or hints
function addHelpTooltips() {
    const helpTexts = {
        'meetingTitle': 'Give your meeting a descriptive title (e.g., "Weekly Team Standup", "Quarterly Review")',
        'meetingTranscript': 'Paste the full transcript of your meeting here. The AI will process and store it for searching and summarization.',
        'searchQuery': 'Search for specific topics, people, decisions, or action items from your uploaded meetings.',
        'summaryText': 'Paste any meeting content here to get an AI-generated summary and action items.',
        'splitText': 'Paste long text here to split it into smaller, manageable chunks for processing.'
    };
    
    Object.entries(helpTexts).forEach(([id, helpText]) => {
        const element = document.getElementById(id);
        if (element) {
            element.setAttribute('title', helpText);
        }
    });
}

// Initialize tooltips when page loads
document.addEventListener('DOMContentLoaded', addHelpTooltips);
