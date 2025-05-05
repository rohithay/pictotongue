// DOM Elements
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const previewImage = document.getElementById('previewImage');
const translateBtn = document.getElementById('translateBtn');
const languageSelect = document.getElementById('language');
const progressBar = document.getElementById('progressBar');
const progressBarFill = document.getElementById('progressBarFill');
const statusText = document.getElementById('status');
const notification = document.getElementById('notification');
const loadingSpinner = document.getElementById('loadingSpinner');
const resultsCard = document.getElementById('resultsCard');
const originalText = document.getElementById('originalText');
const translatedText = document.getElementById('translatedText');
const tabs = document.querySelectorAll('.tab');
const tabContents = document.querySelectorAll('.tab-content');

// Event Listeners
uploadArea.addEventListener('click', () => {
    fileInput.click();
});

uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.style.borderColor = 'var(--primary)';
    uploadArea.style.backgroundColor = 'rgba(59, 130, 246, 0.05)';
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.style.borderColor = 'var(--border)';
    uploadArea.style.backgroundColor = 'transparent';
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.style.borderColor = 'var(--border)';
    uploadArea.style.backgroundColor = 'transparent';
    
    if (e.dataTransfer.files.length) {
        handleFile(e.dataTransfer.files[0]);
    }
});

fileInput.addEventListener('change', () => {
    if (fileInput.files.length) {
        handleFile(fileInput.files[0]);
    }
});

translateBtn.addEventListener('click', () => {
    translateNewspaper();
});

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        // Remove active class from all tabs
        tabs.forEach(t => t.classList.remove('active'));
        tabContents.forEach(c => c.classList.remove('active'));
        
        // Add active class to clicked tab
        tab.classList.add('active');
        document.getElementById(`${tab.dataset.tab}Tab`).classList.add('active');
    });
});

// Functions
function handleFile(file) {
    // Check if file is an image
    if (!file.type.match('image.*')) {
        showNotification('Please select an image file (JPEG, PNG, BMP, or TIFF)', 'error');
        return;
    }
    
    // Display preview
    const reader = new FileReader();
    reader.onload = (e) => {
        previewImage.src = e.target.result;
        previewImage.style.display = 'block';
        translateBtn.disabled = false;
        statusText.textContent = 'Image uploaded. Click Translate to process.';
    };
    reader.readAsDataURL(file);
}

function translateNewspaper() {
    // Show loading state
    loadingSpinner.style.display = 'flex';
    translateBtn.disabled = true;
    statusText.textContent = 'Processing...';
    
    // Create form data for API call
    const formData = new FormData();
    formData.append('image', fileInput.files[0]);
    formData.append('language', languageSelect.value);
    
    // Simulate progress (in a real app, this would be connected to the backend)
    let progress = 0;
    const progressInterval = setInterval(() => {
        progress += 5;
        if (progress > 90) {
            clearInterval(progressInterval);
        }
        progressBarFill.style.width = `${progress}%`;
    }, 300);
    
    // In a real implementation, make an API call to your backend
    // For now, we'll simulate the process with a timeout
    setTimeout(() => {
        // Simulate API response
        const targetLanguage = languageSelect.value;
        
        // Sample text (in a real app, this would come from the backend)
        const sampleOriginalText = "The global climate summit concluded yesterday with new agreements on carbon emissions. Leaders from 195 countries participated in what many are calling a historic breakthrough in the fight against climate change.";
        
        let sampleTranslation = "";
        
        // Sample translations (in a real app, these would come from the translation service)
        if (targetLanguage === 'es') {
            sampleTranslation = "La cumbre climática global concluyó ayer con nuevos acuerdos sobre emisiones de carbono. Líderes de 195 países participaron en lo que muchos consideran un avance histórico en la lucha contra el cambio climático.";
        } else if (targetLanguage === 'fr') {
            sampleTranslation = "Le sommet mondial sur le climat s'est conclu hier avec de nouveaux accords sur les émissions de carbone. Les dirigeants de 195 pays ont participé à ce que beaucoup considèrent comme une avancée historique dans la lutte contre le changement climatique.";
        } else {
            sampleTranslation = "Translation would appear here in " + languageSelect.options[languageSelect.selectedIndex].text;
        }
        
        // Update UI with results
        progressBarFill.style.width = '100%';
        originalText.textContent = sampleOriginalText;
        translatedText.textContent = sampleTranslation;
        resultsCard.style.display = 'block';
        loadingSpinner.style.display = 'none';
        translateBtn.disabled = false;
        statusText.textContent = 'Translation complete!';
        
        showNotification('Translation completed successfully!', 'success');
        
        // Reset progress bar for next use
        setTimeout(() => {
            progressBarFill.style.width = '0%';
        }, 1000);
    }, 3000);
}

function showNotification(message, type) {
    notification.textContent = message;
    notification.className = 'notification';
    notification.classList.add(type);
    notification.style.display = 'block';
    
    setTimeout(() => {
        notification.style.display = 'none';
    }, 8080);
}
