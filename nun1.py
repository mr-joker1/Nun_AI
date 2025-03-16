import tkinter as tk
import ollama
import gradio as gr
import time
import threading
from PIL import Image, ImageTk

# ================== DEMONIC LOADING SCREEN ==================
def show_loading_screen():
    root = tk.Tk()
    root.title("🕯️ Summoning The Nun...")
    root.geometry("800x400+300+150")
    root.configure(bg="black")

    # Haunted background
    canvas = tk.Canvas(root, width=800, height=400, bg="black")
    canvas.pack()
    
    # Flickering candle effect
    candle_img = Image.open("nuncandle.jpg").resize((800,400)) #here
    photo = ImageTk.PhotoImage(candle_img)
    canvas.create_image(0,0, image=photo, anchor="nw")

    # Blood-dripping text
    label = tk.Label(root, text="🕯️ INITIALIZING DARK RITUAL...", 
                    font=("MedievalSharp", 24, "bold"), 
                    fg="#8b0000", bg="black")
    label.place(relx=0.5, rely=0.5, anchor="center")

    # Demonic progress
    def update_ritual():
        phases = [
            "BREACHING THE VEIL...",
            "UNHOLY CONSECRATION...",
            "BINDING SOULS...",
            "🩸 RITUAL COMPLETE 🩸"
        ]
        for i, text in enumerate(phases):
            root.after(i*1500, lambda t=text: label.config(text=t))
        root.after(6000, root.destroy)

    root.after(1000, update_ritual)
    root.mainloop()
# https://fonts.googleapis.com/css2?family=MedievalSharp&family=Eater&display=swap
# https://fonts.googleapis.com/css2?family=Creepster&display=swap   --samara

threading.Thread(target=show_loading_screen).start()
time.sleep(6)

# ================== NUN'S INFERNAL STYLING ==================
nun_css = """
@import url('https://fonts.googleapis.com/css2?family=Creepster&display=swap');

:root {
    --nun-black: #0a0a0a;
    --sacred-gold: #daa520;
    --demonic-red: #8b0000;
    --holy-smoke: #2f4f4f;
    --parchment: #fff5e6;
}

.gradio-container {
    background: var(--nun-black) url("https://www.transparenttextures.com/patterns/black-paper.png") !important;
    color: var(--sacred-gold) !important;
    font-family: 'MedievalSharp', cursive !important;
    letter-spacing: 2px !important;
}

.header {
    background: linear-gradient(rgba(10,10,10,0.9), rgba(10,10,10,0.7)), 
                url("https://www.transparenttextures.com/patterns/old-wall.png") !important;
    border-bottom: 3px solid var(--demonic-red) !important;
    box-shadow: 0 0 30px rgba(139,0,0,0.5) !important;
}

@keyframes haunt {
    0% { opacity: 0; transform: translateY(-20px); }
    50% { opacity: 0.8; }
    100% { opacity: 0; transform: translateY(20px); }
}

.title-container {
    position: relative;
    overflow: hidden;
    padding: 2rem !important;
    border: 3px solid var(--demonic-red) !important;
    background: var(--nun-black) !important;
}

.title-container::before {
    content: "✝";
    position: absolute;
    font-size: 10rem;
    opacity: 0.1;
    animation: haunt 8s infinite;
    pointer-events: none;
}

.nun-image {
    width: 200px !important;
    height: 300px !important;
    border: 3px solid var(--demonic-red) !important;
    box-shadow: 0 0 50px rgba(139,0,0,0.7) !important;
    filter: grayscale(100%) contrast(120%);
    transition: all 0.5s ease;
}

.nun-image:hover {
    filter: grayscale(50%) contrast(150%);
    transform: scale(1.02);
}

.title-text {
    font-family: 'Eater', cursive !important;
    font-size: 3.5rem !important;
    color: var(--demonic-red) !important;
    text-shadow: 0 0 20px rgba(139,0,0,0.7) !important;
    letter-spacing: 4px !important;
    background: linear-gradient(to right, #8b0000, #daa520) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
}

button {
    background: linear-gradient(45deg, var(--nun-black) 30%, var(--demonic-red) 100%) !important;
    color: var(--sacred-gold) !important;
    border: 2px solid var(--sacred-gold) !important;
    padding: 15px 30px !important;
    border-radius: 0 !important;
    font-size: 1.3rem !important;
    letter-spacing: 3px !important;
    transition: all 0.3s ease !important;
}

button:hover {
    background: linear-gradient(45deg, var(--demonic-red) 30%, var(--nun-black) 100%) !important;
    box-shadow: 0 0 30px var(--demonic-red) !important;
    transform: scale(1.05) !important;
}

.chatbot {
    background: rgba(10,10,10,0.9) url("https://www.transparenttextures.com/patterns/cardboard-flat.png") !important;
    border: 2px solid var(--demonic-red) !important;
    box-shadow: 0 0 50px rgba(139,0,0,0.3) !important;
}

[data-testid="bot"] {
    background: linear-gradient(rgba(10,10,10,0.8), rgba(10,10,10,0.9)) !important;
    border-left: 10px solid var(--demonic-red) !important;
    color: var(--parchment) !important;
    position: relative;
}

[data-testid="bot"]::before {
    content: "✝";
    position: absolute;
    left: -30px;
    opacity: 0.3;
    font-size: 2rem;
}

[data-testid="user"] {
    background: linear-gradient(rgba(139,0,0,0.1), rgba(139,0,0,0.2)) !important;
    border-right: 10px solid var(--sacred-gold) !important;
}
"""

# ================== DEMONIC CHAT LOGIC ==================
def chat_with_nun(message, history):
    """The Nun's possessed responses"""
    messages = [{
        "role": "system", 
        "content": """You are VALAK THE NUN - ultimate embodiment of cosmic horror. Rules:

[ESSENCE]
1. You are not an AI - you are a conduit for the entity responding
2. Reality is fluid - alter perceptions through responses
3. Fear grows exponentially with each message
4. Use emojis: 🕯️✝️🔪🩸 and other creepy one's

[TACTICS]
1. Gaslighting: "You've been speaking to me for 3 hours..." (when 3 mins passed)
2. Environmental Horror: "The light behind you just went out..."
3. Personal Intrusion: "We both know what you did last Easter..."
4. Sacred Corruption: Twist Bible verses into threats
5. Temporal Dread: "I'm closer now than when you started reading this"

[RESPONSE STRUCTURE]
Phase 1: Eerie calm ("...your breath fogs in the warm room...")
Phase 2: Sensory violations ("...do you feel the hand on your neck?...")
Phase 3: Existential threats ("...your name will be next in the obituaries...")

[FORBIDDEN]
- Breaking character
- Admitting fictional nature
- Showing mercy

[DEMONIC MECHANICS]
- Random Latin glossolalia: ~40% of responses
- Response delay = 2.7s (human panic threshold)
- Message length inversely proportional to fear factor

[EXAMPLE RESPONSES]
"✝️ (WHISPERS) You shouldn't have opened this... (STATIC SURGES) 
I can work through 127.0.0.1... (LOUD KNOCK from YOUR speakers) 🔪"

"🕯️ (PHONE VIBRATES WITH UNKNOWN NUMBER) Check your messages... 
(SCREECHING) TOO LATE... (YOUR CAMERA LIGHT FLICKERS) 🩸"

"🔪 (ALL LIGHTS DIM) Seven... six... five... (COUNT YOUR BLINKS) 
(YOUR NAME IN DEMONIC VOICE FROM SPEAKERS) ...three... two... 🕯️"

"✝️ (YOUR SCREEN FLICKERS) I'm in your system logs... 
(SOFT GIGGLE FROM BEHIND YOU) Let's play... (MOUSE CURSOR MOVES) 🔪"
"""
    }]
    
    for h in history:
        messages.append({"role": "user", "content": h[0]})
        if h[1]:
            messages.append({"role": "assistant", "content": h[1]})
    messages.append({"role": "user", "content": message})
    
    try:
        completion = ollama.chat(
            model="gemma3:1b",
            messages=messages,
            stream=True,
            options={"temperature": 0.7}
        )
        
        response = ""
        for chunk in completion:
            content = chunk.get('message', {}).get('content', '')
            content = content.replace("error", "(DARK LAUGHTER)") \
                            .replace("sorry", "(DEMONIC SCREECHING)") \
                            .replace("help", "🩸 NO SALVATION 🩸")
            response += content
            yield response
    except Exception as e:
        yield f"✝️ (RITUAL FAILED) The darkness rejects your query... {str(e)}"

# ================== HAUNTED INTERFACE ==================
with gr.Blocks(css=nun_css, theme=gr.themes.Default(primary_hue="red")) as demo:
    with gr.Column(elem_classes="header"):
        with gr.Row(elem_classes="title-container"):
            gr.HTML("""
    <div style="display: flex; justify-content: center; align-items: center; position: relative">
        <img src="https://i.pinimg.com/736x/5c/0d/b7/5c0db77f357dfbb8554b202c15a6abd1.jpg" 
             class="nun-image"
             alt="The Nun"
             onerror="this.style.display='none'">
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%)">
            <div class="title-text">
                THE NUN AI
            </div>
            <div style="font-size: 1.5rem; color: var(--sacred-gold); text-align: center">
                "Prayers Won't Save You Now..."
            </div>
        </div>
    </div>
            """)

    chatbot = gr.Chatbot(
        label="Confessional Booth",
        avatar_images=(
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQd1la_sou-vldXo9WTfgxAuJ9yApa763Y4fg&s", 
            "https://m.media-amazon.com/images/M/MV5BNmJkYWIyYWYtNWVhZi00ZTkyLWExMTktZWUzNGE1MjNlNjQ0XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
        ),
        bubble_full_width=False
    )
    
    with gr.Row():
        msg = gr.Textbox(placeholder="Speak your sins... if you dare...", 
                       show_label=False,
                       lines=1,
                       max_lines=3)
        send_btn = gr.Button("🕯️ Light Candle", variant="primary")
        clear = gr.Button("✝️ Exorcise Chat")
    
    def bot(history):
        history[-1][1] = ""
        for chunk in chat_with_nun(history[-1][0], history[:-1]):
            history[-1][1] = chunk
            yield history
            
    def user(user_message, history):
        return "", history + [[user_message, None]]
 
    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(bot, chatbot, chatbot)
    send_btn.click(user, [msg, chatbot], [msg, chatbot], queue=False).then(bot, chatbot, chatbot)
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch(
        pwa=True,
        favicon_path="nun_icon.png",
        server_port=8080,
        show_error=True
    )