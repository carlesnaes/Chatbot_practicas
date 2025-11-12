console.log(" script.js cargado correctamente");


function safeUUID() {
  if (window.crypto && window.crypto.getRandomValues) {
    return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>
      (c ^ window.crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
    );
  }
  
  return Math.random().toString(36).substring(2) + Date.now().toString(36);
}

// 
function getOrCreateUserID() {
  let uid = localStorage.getItem("userID");
  if (!uid) {
    uid = safeUUID();   // 
    localStorage.setItem("userID", uid);
    ;
  } else {
    ;
  }
  return uid;
}
const userID = getOrCreateUserID();

let cooldownInterval = null;

function startCooldown(seconds) {
    const timerDiv = document.getElementById("timer-counter");
    const sendBtn = document.getElementById("send-btn");
    const userInput = document.getElementById("user-input");

    let remaining = seconds;

    localStorage.setItem("cooldown_end", Date.now() + seconds * 1000);

    timerDiv.style.display = "block";
    sendBtn.disabled = true;
    userInput.disabled = true;

    function updateTimer() {
        const mins = Math.floor(remaining / 60);
        const secs = remaining % 60;
        timerDiv.textContent = `⏳ Podrás volver a preguntar en ${String(mins).padStart(2,'0')}:${String(secs).padStart(2,'0')}`;

        if (remaining <= 0) {
            clearInterval(cooldownInterval);
            timerDiv.style.display = "none";
            sendBtn.disabled = false;
            userInput.disabled = false;
            localStorage.removeItem("cooldown_end");  
            return;
        }

        remaining--;
    }

    updateTimer();
    cooldownInterval = setInterval(updateTimer, 1000);
}


const savedCooldownEnd = localStorage.getItem("cooldown_end");

if (savedCooldownEnd) {
    const remaining = Math.floor((savedCooldownEnd - Date.now()) / 1000);
    if (remaining > 0) {
        startCooldown(remaining);
    } else {
        localStorage.removeItem("cooldown_end");
    }
}


const chatContainer = document.getElementById("chat-container");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");
const roleSelect = document.getElementById("role");
const schoolSelect = document.getElementById("school");

function generateUUID() {
  return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>
    (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
  );
}

if (!sessionStorage.getItem("session_id")) {
  const newId = generateUUID();
  sessionStorage.setItem("session_id", newId);
  console.log(" Nuevo session_id generado:", newId);
} else {
  console.log(" session_id existente:", sessionStorage.getItem("session_id"));
}
const sessionId = sessionStorage.getItem("session_id");

window.addEventListener("beforeunload", () => {
  sessionStorage.removeItem("session_id");
});


roleSelect.addEventListener("change", () => {
  if (roleSelect.value === "empresa") {
    schoolSelect.value = "ALL";
    schoolSelect.disabled = true;
    schoolSelect.style.display = "none"; 
  } else {
    schoolSelect.disabled = false;
    schoolSelect.style.display = "inline"; 
  }
});

if (roleSelect.value === "empresa") {
  schoolSelect.style.display = "none";
}

async function sendMessage() {
  const message = userInput.value.trim();
  const role = roleSelect.value;
  const school = schoolSelect.value;
  if (!message) return;

  appendMessage("user", message);
  userInput.value = "";
  appendMessage("bot", "💬 Pensando...");

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-User-ID": userID       
      },
      body: JSON.stringify({
        message,
        role,
        school,
        session_id: sessionId,   
        user_id: userID          
      })
    });


    const data = await res.json();
    removeLastBotPlaceholder();

if (data.error) {
    appendMessage(
        "bot",
        `⚠️ ${data.error}<br><br>⏳ Espera ${data.retry_after_minutes} minutos.`
    );

    startCooldown(data.retry_after_minutes * 60);

    return;
}


const botMsg = appendMessage("bot", data.answer);
    if (data.sources && data.sources.length > 0) {
      appendSources(data.sources);
    }

    if (data.fallback_used) {
      const warn = document.createElement("div");
      warn.classList.add("fallback-warning");
      warn.textContent = "⚠️ Se ha usado normativa general UPV (ALL) por falta de información específica.";
      chatContainer.appendChild(warn);
    }

    const feedbackDiv = document.createElement("div");
  feedbackDiv.classList.add("feedback");

  const thumbUp = document.createElement("button");
  thumbUp.classList.add("thumb-up");
  thumbUp.title = "Respuesta útil 👍";
  thumbUp.textContent = "👍";

  const thumbDown = document.createElement("button");
  thumbDown.classList.add("thumb-down");
  thumbDown.title = "Respuesta poco útil 👎";
  thumbDown.textContent = "👎";

  feedbackDiv.appendChild(thumbUp);
  feedbackDiv.appendChild(thumbDown);
  botMsg.appendChild(feedbackDiv);

  thumbUp.addEventListener("click", () =>
    sendFeedback("positive", message, data.answer, feedbackDiv)
  );
  thumbDown.addEventListener("click", () =>
    sendFeedback("negative", message, data.answer, feedbackDiv)
  );

  } catch (err) {
    console.error(err);
    removeLastBotPlaceholder();
    appendMessage("bot", "Error al conectar con el servidor.");
  }
}

function appendSources(sources) {
  if (!sources || !sources.length) return;

  const details = document.createElement("details");
  details.classList.add("sources-block");

  const summary = document.createElement("summary");
  summary.textContent = `📚 Fuentes consultadas (${sources.length})`;
  details.appendChild(summary);

  sources.forEach(src => {
    const div = document.createElement("div");
    div.classList.add("source-item");
    div.innerHTML = `
      <p><b>${src.source}</b> – ${src.school}</p>
      <p class="preview">📝 ${src.preview}</p>
    `;
    details.appendChild(div);
  });

  chatContainer.appendChild(details);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

async function sendFeedback(feedback, question, answer, feedbackDiv) {
  try {
    await fetch("/feedback", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-User-ID": userID     
      },
      body: JSON.stringify({
        feedback,
        question,
        answer,
        session_id: sessionId,
        role: roleSelect.value,
        user_id: userID
      })
    });

    feedbackDiv.innerHTML = `<span class="feedback-thanks">✅ ¡Gracias por tu valoración!</span>`;
  } catch (e) {
    console.error("Error enviando feedback:", e);
    feedbackDiv.innerHTML = `<span class="feedback-thanks">⚠️ Error al enviar feedback</span>`;
  }
}

function removeLastBotPlaceholder() {
  const msgs = document.querySelectorAll(".bot-msg");
  const last = msgs[msgs.length - 1];
  if (last && last.textContent === "💬 Pensando...") last.remove();
}

sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keypress", e => {
  if (e.key === "Enter") sendMessage();
});



function appendMessage(type, text) {
  const msg = document.createElement("div");
  msg.classList.add("message", type === "user" ? "user-msg" : "bot-msg");

  if (!text) text = "";

  text = text.replace(/\n/g, "<br>");

  text = text.replace(
    /\bhttps?:\/\/[^\s<>()"]+/gi,
    url => `<a href="${url}" target="_blank" rel="noopener noreferrer">${url}</a>`
  );

  const tempDiv = document.createElement("div");
  tempDiv.innerHTML = text;

  tempDiv.querySelectorAll("script, iframe, object, embed, svg, style, link").forEach(el => el.remove());

  tempDiv.querySelectorAll("*").forEach(el => {
    if (!["A", "B", "I", "BR"].includes(el.tagName)) {
      const safeText = document.createTextNode(el.textContent);
      el.replaceWith(safeText);
    } else if (el.tagName === "A") {
      const href = el.getAttribute("href") || "";
      if (!/^https?:\/\//i.test(href)) {
        el.replaceWith(document.createTextNode(el.textContent));
      } else {
        el.setAttribute("target", "_blank");
        el.setAttribute("rel", "noopener noreferrer");
      }
    }
  });

  msg.innerHTML = tempDiv.innerHTML;
  chatContainer.appendChild(msg);
  chatContainer.scrollTop = chatContainer.scrollHeight;
  return msg;
}


window.addEventListener("DOMContentLoaded", () => {

  const micBtn = document.getElementById("mic-btn");
  const userInput = document.getElementById("user-input");
  if (!micBtn) return;

  let mediaRecorder;
  let audioChunks = [];
  let isRecording = false;

  micBtn.addEventListener("click", async () => {
    if (window.location.protocol !== "https:" && window.location.hostname !== "localhost") {
      alert(" Para usar el micrófono necesitas acceder desde una conexión segura (HTTPS) o desde localhost.");
      return;
    }

    if (!isRecording) {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];

        mediaRecorder.ondataavailable = e => audioChunks.push(e.data);
        mediaRecorder.start();
        isRecording = true;

        micBtn.textContent = "🛑 Grabando...";
        micBtn.style.backgroundColor = "#d9534f";
        console.log("🎙️ Grabación iniciada");
      } catch (err) {
        console.error("⚠️ No se pudo acceder al micrófono:", err);

        let msg;
        if (err.name === "NotAllowedError") {
          msg = "🎤 Has denegado el acceso al micrófono. Activa el permiso en tu navegador.";
        } else if (err.name === "NotFoundError") {
          msg = "🎧 No se ha detectado ningún micrófono disponible.";
        } else {
          msg = "⚠️ No se pudo acceder al micrófono. Revisa permisos o la conexión segura (HTTPS).";
        }
        alert(msg);
        return;
      }
    } else {
      console.log("🛑 Grabación detenida, procesando...");
      isRecording = false;
      micBtn.textContent = "🎤";
      micBtn.style.backgroundColor = "";
      if (!mediaRecorder) return;
      mediaRecorder.stop();

      mediaRecorder.onstop = async () => {
        const blob = new Blob(audioChunks, { type: "audio/webm" });
        const formData = new FormData();
        formData.append("file", blob, "audio.webm");

        try {
          const res = await fetch("/transcribe", {
            method: "POST",
            body: formData
          });
          const data = await res.json();
          console.log("📝 Transcripción:", data.text);

          if (data.text) {
            userInput.value = data.text;
            sendMessage(); 
          } else {
            alert("⚠️ No se pudo transcribir el audio.");
          }
        } catch (err) {
          console.error("❌ Error al enviar audio:", err);
          alert("⚠️ Error al enviar el audio al servidor. Verifica la conexión.");
        }
      };
    }
  });
});




