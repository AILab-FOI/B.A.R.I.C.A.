const output = document.getElementById('output');

const ws = new WebSocket(`ws://${APP_CONFIG.WS_HOST}:${APP_CONFIG.WS_PORT}`);

ws.onopen = () => {
  console.log('WebSocket connected.');
};

ws.onerror = (error) => {
  console.error('WebSocket error:', error);
};

window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

if (!window.SpeechRecognition) {
  output.innerHTML = "Your browser does not support speech recognition.";
} else {
  const recognition = new SpeechRecognition();
  recognition.continuous = true;
  recognition.interimResults = true;
  recognition.lang = 'hr-HR';

  let silenceTimer;
  let currentText = '';

  const resetText = () => {
    currentText = '';
    output.innerHTML = '';
  };

  const startRecognition = () => {
    try {
      recognition.start();
    } catch (e) {
      
    }
  };

  recognition.onresult = (event) => {
    let interimText = '';
    let finalText = '';

    for (let i = 0; i < event.results.length; i++) {
      const result = event.results[i];
      if (result.isFinal) {
        finalText += result[0].transcript;
      } else {
        interimText += result[0].transcript;
      }
    }

    // Show the text in browser
    output.innerHTML = currentText + interimText;

    // Send only final text 
    if (finalText && ws.readyState === WebSocket.OPEN) {
      ws.send(finalText);
      currentText += finalText + ' ';
    }

    // Silence timer
    clearTimeout(silenceTimer);
    silenceTimer = setTimeout(() => {
      resetText();
    }, 5000); 
  };

  recognition.onerror = (e) => {
    console.error('Error in speech recognition', e);
  };

  recognition.onend = () => {
    startRecognition();
  };

  startRecognition();
}