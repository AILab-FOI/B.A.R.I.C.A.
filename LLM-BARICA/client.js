const output = document.getElementById('output');
const pttBtn = document.getElementById('pttBtn');

const ws = new WebSocket(`ws://${APP_CONFIG.WS_HOST}:${APP_CONFIG.WS_PORT}`);

window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

if (!window.SpeechRecognition) {
  output.innerHTML = "Speech recognition not supported.";
} else {
  const recognition = new SpeechRecognition();
  recognition.continuous = true;
  recognition.interimResults = true;
  recognition.lang = 'hr-HR';

  let finalText = '';
  let isListening = false;

  const reset = () => {
    finalText = '';
    output.innerHTML = '';
  };

  recognition.onresult = (event) => {
    let interim = '';

    for (let i = event.resultIndex; i < event.results.length; i++) {
      const result = event.results[i];
      if (result.isFinal) {
        finalText += result[0].transcript;
      } else {
        interim += result[0].transcript;
      }
    }

    output.innerHTML = finalText + interim;
  };

  recognition.onend = () => {
    isListening = false;
    pttBtn.classList.remove('listening');
    pttBtn.textContent = '🎤';

    if (finalText && ws.readyState === WebSocket.OPEN) {
      ws.send(finalText.trim());
    }

    reset();
  };

  pttBtn.addEventListener('click', () => {
    if (!isListening) {
      reset();
      recognition.start();
      isListening = true;
      pttBtn.classList.add('listening');
      pttBtn.textContent = '🛑';
    } else {
      recognition.stop(); 
    }
  });
}
