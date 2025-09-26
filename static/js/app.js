// CrewAI Web Interface JavaScript
class CrewAIApp {
    constructor() {
        this.queryInput = document.getElementById('queryInput');
        this.sendBtn = document.getElementById('sendBtn');
        this.resultsContainer = document.getElementById('resultsContainer');
        this.loadingOverlay = document.getElementById('loadingOverlay');
        this.weatherAgent = document.getElementById('weatherAgent');
        this.apiAgent = document.getElementById('apiAgent');
        this.mathAgent = document.getElementById('mathAgent');
        
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.setupQuickActions();
    }

    setupEventListeners() {
        // Send button click
        this.sendBtn.addEventListener('click', () => this.handleQuery());
        
        // Enter key press
        this.queryInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.handleQuery();
            }
        });

        // Input focus
        this.queryInput.addEventListener('focus', () => {
            this.queryInput.parentElement.style.borderColor = '#667eea';
        });

        this.queryInput.addEventListener('blur', () => {
            if (!this.queryInput.value) {
                this.queryInput.parentElement.style.borderColor = '#e2e8f0';
            }
        });
    }

    setupQuickActions() {
        const quickBtns = document.querySelectorAll('.quick-btn');
        quickBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const query = btn.getAttribute('data-query');
                this.queryInput.value = query;
                this.handleQuery();
            });
        });
    }

    async handleQuery() {
        const query = this.queryInput.value.trim();
        
        if (!query) {
            this.showError('Please enter a query');
            return;
        }

        this.showLoading(true);
        this.clearAgentStatus();

        try {
            const response = await fetch('/api/query', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query })
            });

            const data = await response.json();

            if (data.success) {
                this.displayResult(data);
                this.highlightActiveAgent(data.agent_used);
            } else {
                this.showError(data.error || 'An error occurred');
            }
        } catch (error) {
            console.error('Error:', error);
            this.showError('Failed to process your request. Please try again.');
        } finally {
            this.showLoading(false);
            this.queryInput.value = '';
        }
    }

    displayResult(data) {
        const resultItem = document.createElement('div');
        resultItem.className = 'result-item';
        
        const currentTime = new Date().toLocaleTimeString();
        
        resultItem.innerHTML = `
            <div class="result-header">
                <div class="result-query">"${data.query}"</div>
                <div class="result-agent">${data.agent_used}</div>
            </div>
            <div class="result-response">${data.response}</div>
            <div class="result-time">${currentTime}</div>
        `;

        // Remove welcome message if it exists
        const welcomeMessage = this.resultsContainer.querySelector('.welcome-message');
        if (welcomeMessage) {
            welcomeMessage.remove();
        }

        // Add new result at the top
        this.resultsContainer.insertBefore(resultItem, this.resultsContainer.firstChild);

        // Scroll to top of results
        this.resultsContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    highlightActiveAgent(agentUsed) {
        // Clear previous active states
        this.weatherAgent.classList.remove('active');
        this.apiAgent.classList.remove('active');
        this.mathAgent.classList.remove('active');

        // Highlight the active agent
        if (agentUsed.includes('Weather')) {
            this.weatherAgent.classList.add('active');
        } else if (agentUsed.includes('API')) {
            this.apiAgent.classList.add('active');
        } else if (agentUsed.includes('Math')) {
            this.mathAgent.classList.add('active');
        }

        // Remove active state after 3 seconds
        setTimeout(() => {
            this.weatherAgent.classList.remove('active');
            this.apiAgent.classList.remove('active');
            this.mathAgent.classList.remove('active');
        }, 3000);
    }

    clearAgentStatus() {
        this.weatherAgent.classList.remove('active');
        this.apiAgent.classList.remove('active');
        this.mathAgent.classList.remove('active');
    }

    showError(message) {
        const errorItem = document.createElement('div');
        errorItem.className = 'result-item error-message';
        
        const currentTime = new Date().toLocaleTimeString();
        
        errorItem.innerHTML = `
            <div class="result-header">
                <div class="result-query">Error</div>
            </div>
            <div class="result-response">${message}</div>
            <div class="result-time">${currentTime}</div>
        `;

        // Remove welcome message if it exists
        const welcomeMessage = this.resultsContainer.querySelector('.welcome-message');
        if (welcomeMessage) {
            welcomeMessage.remove();
        }

        this.resultsContainer.insertBefore(errorItem, this.resultsContainer.firstChild);
    }

    showLoading(show) {
        this.loadingOverlay.style.display = show ? 'flex' : 'none';
        this.sendBtn.disabled = show;
        
        if (show) {
            this.sendBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
        } else {
            this.sendBtn.innerHTML = '<i class="fas fa-paper-plane"></i>';
        }
    }

    // Utility method to clear all results
    clearResults() {
        this.resultsContainer.innerHTML = `
            <div class="welcome-message">
                <i class="fas fa-lightbulb"></i>
                <p>Try asking me about weather or math! Use the examples above or type your own question.</p>
            </div>
        `;
    }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new CrewAIApp();
});

// Add some nice animations and interactions
document.addEventListener('DOMContentLoaded', () => {
    // Animate elements on load
    const elements = document.querySelectorAll('.query-section, .results-section, .agent-status');
    elements.forEach((element, index) => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(30px)';
        
        setTimeout(() => {
            element.style.transition = 'all 0.6s ease';
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }, index * 200);
    });

    // Add typing effect to placeholder
    const placeholder = document.getElementById('queryInput').placeholder;
    const input = document.getElementById('queryInput');
    let placeholderIndex = 0;
    let isDeleting = false;
    
    function typePlaceholder() {
        const currentPlaceholder = placeholder.substring(0, placeholderIndex);
        input.placeholder = currentPlaceholder;
        
        if (!isDeleting) {
            placeholderIndex++;
            if (placeholderIndex === placeholder.length) {
                setTimeout(() => { isDeleting = true; }, 2000);
            }
        } else {
            placeholderIndex--;
            if (placeholderIndex === 0) {
                isDeleting = false;
            }
        }
        
        setTimeout(typePlaceholder, isDeleting ? 50 : 100);
    }
    
    // Start typing effect after a delay
    setTimeout(typePlaceholder, 1000);
});
