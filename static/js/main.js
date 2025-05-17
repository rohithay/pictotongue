// PictoTongue JavaScript - Simple and Clean Implementation
document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const uploadForm = document.getElementById('uploadForm');
    const imageUpload = document.getElementById('imageUpload');
    const imagePreview = document.getElementById('imagePreview');
    const processBtn = document.getElementById('processBtn');
    const fromLanguage = document.getElementById('fromLanguage');
    const toLanguage = document.getElementById('toLanguage');
    const originalText = document.getElementById('originalText');
    const translatedText = document.getElementById('translatedText');
    const loadingOriginal = document.getElementById('loadingOriginal');
    const loadingTranslation = document.getElementById('loadingTranslation');
    const resultInfo = document.getElementById('resultInfo');
    const processingTime = document.getElementById('processingTime');
    const originalTextContainer = document.getElementById('originalTextContainer');
    const translatedTextContainer = document.getElementById('translatedTextContainer');

    // Handle image upload and preview
    imageUpload.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (!file) return;

        // Clear previous results
        clearResults();
        
        // Check if the file is an image
        if (!file.type.match('image.*')) {
            alert('Please select an image file.');
            return;
        }

        // Display image preview
        const reader = new FileReader();
        reader.onload = function(e) {
            imagePreview.innerHTML = `<img src="${e.target.result}" alt="Uploaded Image" style="max-width:100%; max-height:200px;">`;
        };
        reader.readAsDataURL(file);
    });

    // Handle form submission
    uploadForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const file = imageUpload.files[0];
        if (!file) {
            alert('Please select an image file.');
            return;
        }

        // Clear previous results
        clearResults();
        
        // Show loading indicators
        originalTextContainer.style.display = 'none';
        translatedTextContainer.style.display = 'none';
        loadingOriginal.style.display = 'flex';
        loadingTranslation.style.display = 'flex';
        
        // Disable the process button
        processBtn.disabled = true;
        
        // Read the file as data URL
        const reader = new FileReader();
        reader.onload = function(e) {
            // Send the image to the server for processing
            processImage(e.target.result, fromLanguage.value, toLanguage.value);
        };
        reader.readAsDataURL(file);
    });

    // Process the image with the API
    function processImage(imageData, fromLang, toLang) {
        // Prepare the request data
        const requestData = {
            imageData: imageData,
            fromLang: fromLang,
            toLang: toLang
        };

        // Send the request to the server
        fetch('/api/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Update the UI with the results
            displayResults(data);
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while processing the image. Please try again.');
            
            // Hide loading indicators
            loadingOriginal.style.display = 'none';
            loadingTranslation.style.display = 'none';
            originalTextContainer.style.display = 'block';
            translatedTextContainer.style.display = 'block';
            
            // Re-enable the process button
            processBtn.disabled = false;
        });
    }

    // Display the results in the UI
    function displayResults(data) {
        // Hide loading indicators
        loadingOriginal.style.display = 'none';
        loadingTranslation.style.display = 'none';
        originalTextContainer.style.display = 'block';
        translatedTextContainer.style.display = 'block';
        
        // Display the original and translated text
        originalText.value = data.originalText;
        translatedText.value = data.translatedText;
        
        // Display processing time
        processingTime.textContent = data.processingTime;
        resultInfo.style.display = 'block';
        
        // Re-enable the process button
        processBtn.disabled = false;
    }

    // Clear results from previous operations
    function clearResults() {
        originalText.value = '';
        translatedText.value = '';
        resultInfo.style.display = 'none';
        
        // Make sure text containers are visible and loading spinners are hidden
        originalTextContainer.style.display = 'block';
        translatedTextContainer.style.display = 'block';
        loadingOriginal.style.display = 'none';
        loadingTranslation.style.display = 'none';
        
        processBtn.disabled = false;
    }
});// PictoTongue JavaScript - DictPress Inspired
document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const uploadForm = document.getElementById('uploadForm');
    const imageUpload = document.getElementById('imageUpload');
    const imagePreview = document.getElementById('imagePreview');
    const processBtn = document.getElementById('processBtn');
    const fromLanguage = document.getElementById('fromLanguage');
    const toLanguage = document.getElementById('toLanguage');
    const originalText = document.getElementById('originalText');
    const translatedText = document.getElementById('translatedText');
    const loadingOriginal = document.getElementById('loadingOriginal');
    const loadingTranslation = document.getElementById('loadingTranslation');
    const resultInfo = document.getElementById('resultInfo');
    const processingTime = document.getElementById('processingTime');

    // Handle image upload and preview
    imageUpload.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (!file) return;

        // Clear previous results
        clearResults();
        
        // Check if the file is an image
        if (!file.type.match('image.*')) {
            alert('Please select an image file.');
            return;
        }

        // Display image preview
        const reader = new FileReader();
        reader.onload = function(e) {
            imagePreview.innerHTML = `<img src="${e.target.result}" alt="Uploaded Image">`;
        };
        reader.readAsDataURL(file);
    });

    // Handle form submission
    uploadForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const file = imageUpload.files[0];
        if (!file) {
            alert('Please select an image file.');
            return;
        }

        // Clear previous results
        clearResults();
        
        // Show loading indicators
        loadingOriginal.style.display = 'flex';
        loadingTranslation.style.display = 'flex';
        
        // Disable the process button
        processBtn.disabled = true;
        
        // Read the file as data URL
        const reader = new FileReader();
        reader.onload = function(e) {
            // Send the image to the server for processing
            processImage(e.target.result, fromLanguage.value, toLanguage.value);
        };
        reader.readAsDataURL(file);
    });

    // Process the image with the API
    function processImage(imageData, fromLang, toLang) {
        // Prepare the request data
        const requestData = {
            imageData: imageData,
            fromLang: fromLang,
            toLang: toLang
        };

        // Send the request to the server
        fetch('/api/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Update the UI with the results
            displayResults(data);
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while processing the image. Please try again.');
            
            // Hide loading indicators
            loadingOriginal.style.display = 'none';
            loadingTranslation.style.display = 'none';
            
            // Re-enable the process button
            processBtn.disabled = false;
        });
    }

    // Display the results in the UI
    function displayResults(data) {
        // Hide loading indicators
        loadingOriginal.style.display = 'none';
        loadingTranslation.style.display = 'none';
        
        // Display the original and translated text
        originalText.value = data.originalText;
        translatedText.value = data.translatedText;
        
        // Display processing time
        processingTime.textContent = data.processingTime;
        resultInfo.style.display = 'block';
        
        // Re-enable the process button
        processBtn.disabled = false;
        
        // Scroll to results if needed
        scrollToResults();
    }

    // Clear results from previous operations
    function clearResults() {
        originalText.value = '';
        translatedText.value = '';
        resultInfo.style.display = 'none';
        loadingOriginal.style.display = 'none';
        loadingTranslation.style.display = 'none';
        processBtn.disabled = false;
    }
    
    // Scroll to results section
    function scrollToResults() {
        // Only scroll on mobile view when columns are stacked
        if (window.innerWidth <= 992) {
            const resultArea = document.querySelector('.result-area');
            if (resultArea) {
                resultArea.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    }
    
    // Add keyboard shortcut (Ctrl+Enter) to submit form
    document.addEventListener('keydown', function(event) {
        if (event.ctrlKey && event.key === 'Enter') {
            if (!processBtn.disabled) {
                uploadForm.dispatchEvent(new Event('submit'));
            }
        }
    });
});