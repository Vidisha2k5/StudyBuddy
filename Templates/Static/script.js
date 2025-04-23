// 1. Send a chat message
async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (!userInput.trim()) {
        alert('Please enter a question!');
        return;
    }

    const response = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: userInput })
    });
    const data = await response.json();
    document.getElementById('chat-response').innerText = data.question;
}

// 2. Upload a PDF file
async function uploadPDF() {
  const fileInput = document.getElementById('pdf-file');
  const file = fileInput.files[0];
  if (!file) {
      alert('Please select a PDF file!');
      return;
  }

  const formData = new FormData();
  formData.append('file', file);

  const response = await fetch('/upload_pdf', {
      method: 'POST',
      body: formData
  });
  const data = await response.json();

  // Show the extracted text
  document.getElementById('chat-response').innerText = data.extracted_text;
}

// 3. Generate Study Routine
async function generateRoutine() {
    const daysLeft = document.getElementById('days-left').value;
    const topics = document.getElementById('topics').value.split(',').map(t => t.trim());

    if (!daysLeft || topics.length === 0) {
        alert('Please enter the number of days left and at least one topic!');
        return;
    }

    const response = await fetch('/get_routine', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ days_left: daysLeft, topics: topics })
    });

    const data = await response.json();
    document.getElementById('chat-response').innerText = data.routine;
}

// 4. Speak the response using Text-to-Speech
function speakResponse() {
    const text = document.getElementById('chat-response').innerText;
    if (!text) {
        alert('No response to speak!');
        return;
    }

    const utterance = new SpeechSynthesisUtterance(text);
    speechSynthesis.speak(utterance);
}
function downloadText() {
  const text = document.getElementById('chat-response').innerText.trim();
  if (!text) {
      alert("⚡ No text to download! First ask a question or upload a PDF.");
      return;
  }
  const blob = new Blob([text], { type: "text/plain" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = "response.txt";
  a.click();
  URL.revokeObjectURL(url);
}
async function extractText() {
  const fileInput = document.getElementById('pdf-file');
  const file = fileInput.files[0];
  if (!file) {
      alert('Please select a PDF file first!');
      return;
  }

  const formData = new FormData();
  formData.append('file', file);

  const response = await fetch('/extract_text', {
      method: 'POST',
      body: formData
  });

  const data = await response.json();
  document.getElementById('chat-response').innerText = data.text;
}
async function summarizeText() {
  const text = document.getElementById('chat-response').innerText.trim();
  if (!text) {
      alert('No text available to summarize!');
      return;
  }

  const response = await fetch('/summarize', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: text })
  });

  const data = await response.json();
  document.getElementById('chat-response').innerText = data.summary;
}
