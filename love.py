import streamlit as st
from streamlit_confetti import confetti
import streamlit.components.v1 as components
import time
import os
import base64

# -------------------------
# CONFIG
# -------------------------
st.set_page_config(page_title="For Parshi 💖", layout="centered")

# -------------------------
# SESSION STATE
# -------------------------
if "step" not in st.session_state:
    st.session_state.step = 1

# -------------------------
# AUTOPLAY AUDIO FUNCTION
# -------------------------
def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()

    audio_html = f"""
    <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# -------------------------
# GLOBAL CSS
# -------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ff758c, #ff7eb3);
}
.big-text {
    font-size: 38px;
    text-align: center;
    color: white;
    font-weight: bold;
}
.stButton > button {
    font-size: 20px;
    border-radius: 50px;
    padding: 12px 30px;
}

/* GIF Styling */
.gif-container {
    display: flex;
    justify-content: center;
}
.gif-container img {
    width: 350px;
    height: 350px;
    object-fit: cover;
    border-radius: 15px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# STEP 1 (ENTRY)
# -------------------------
if st.session_state.step == 1:

    st.markdown(
        "<div class='big-text'>💌 Parshi, click below...</div>",
        unsafe_allow_html=True
    )

    left, center, right = st.columns([1,2,1])

    with center:
        if st.button("Click to see the message 💖", use_container_width=True):
            st.session_state.step = 2
            st.rerun()

# -------------------------
# STEP 2 (PROPOSAL)
# -------------------------
elif st.session_state.step == 2:

    st.markdown("<div class='big-text'>Parshi, will you be my girlfriend? 💍</div>", unsafe_allow_html=True)

    left, center, right = st.columns([1,2,1])

    with center:
        if st.button("❤️ YES ❤️", use_container_width=True):
            st.session_state.step = 3
            st.rerun()

    components.html("""
        <style>
        #no-btn {
            position: fixed;
            padding: 12px 25px;
            font-size: 18px;
            background-color: #ff4d6d;
            color: white;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            top: 75%;
            left: 65%;
            transition: all 0.15s ease;
        }
        </style>

        <button id="no-btn">NO</button>

        <script>
        const btn = document.getElementById("no-btn");

        function moveBtn() {
            const x = Math.random() * (window.innerWidth - 150);
            const y = Math.random() * (window.innerHeight - 100);

            btn.style.left = x + "px";
            btn.style.top = y + "px";
        }

        moveBtn();

        document.addEventListener("mousemove", (e) => {
            const rect = btn.getBoundingClientRect();

            const distance = Math.hypot(
                e.clientX - rect.left,
                e.clientY - rect.top
            );

            if (distance < 150) {
                moveBtn();
                const texts = ["No 😢", "Are you sure? 😭", "Think again 😏", "Last chance 😳"];
                btn.innerText = texts[Math.floor(Math.random() * texts.length)];
            }
        });
        </script>
        """, height=300)

# -------------------------
# STEP 3 (CELEBRATION)
# -------------------------
elif st.session_state.step == 3:

    confetti(emojis=["💖", "❤️", "💕", "💘"])
    st.balloons()

    st.markdown("<div class='big-text'>YAAAYYY 💖💖💖</div>", unsafe_allow_html=True)

    # 🎵 AUDIO
    audio_path = "assets/audio.mp3"
    if os.path.exists(audio_path):
        autoplay_audio(audio_path)

    # 🎥 VIDEO
    video_path = "assets/video.mp4"
    if os.path.exists(video_path):
        components.html(f"""
            <div style="display:flex; justify-content:center;">
                <video width="320" autoplay controls>
                    <source src="{video_path}" type="video/mp4">
                </video>
            </div>
            """, height=250)

    st.markdown(
        "<h3 style='text-align: center;'>💞 Muaaah! I love you, my cutiepotato 💞</h3>",
        unsafe_allow_html=True
    )

    # -------------------------
    # 🚀 UPDATED GIF LOADING (FAST)
    # -------------------------
    gifs = []

    for i in range(1, 10):
        gif_path = f"assets/{i}.gif"
        if os.path.exists(gif_path):
            gifs.append(gif_path)

    # -------------------------
    # SLIDESHOW
    # -------------------------
    # components.html(f"""
    # <div style="display:flex; justify-content:center;">
    #     <img id="slideshow" style="
    #         width:350px;
    #         height:350px;
    #         object-fit:cover;
    #         border-radius:15px;
    #         box-shadow:0 8px 20px rgba(0,0,0,0.2);
    #         transition: opacity 0.5s;
    #     ">
    # </div>

    # <script>
    # const gifs = {gifs};
    # let index = 0;
    # const img = document.getElementById("slideshow");

    # function showNextGif() {{
    #     img.style.opacity = 0;

    #     setTimeout(() => {{
    #         img.src = gifs[index];
    #         img.style.opacity = 1;
    #         index = (index + 1) % gifs.length;
    #     }}, 200);
    # }}

    # setInterval(showNextGif, 2000);

    # // 🔥 show first instantly
    # if (gifs.length > 0) {{
    #     img.src = gifs[0];
    # }}

    # </script>
    # """, height=400)

    # st.markdown("""
    #     <hr style="margin-top:5px;">
    #     <div style='
    #         text-align: center;
    #         color: white;
    #         opacity: 0.8;
    #         font-size: 14px;
    #         animation: fadeIn 2s ease-in;
    #     '>
    #         Made with ❤️ by <b>your favourite - Vipul Malyan</b>
    #     </div>

    #     <style>
    #     @keyframes fadeIn {
    #         from {opacity: 0;}
    #         to {opacity: 0.8;}
    #     }
    #     </style>
    #     """, unsafe_allow_html=True)

 # -------------------------
# 🚀 STREAMLIT GIF SLIDESHOW (WORKING)
# -------------------------

    # -------------------------
    # 🚀 PERFECT GIF SLIDESHOW (FAST + SMOOTH + CENTERED)
    # -------------------------
    @st.cache_data
    def load_gifs():
        gifs = []
        for i in range(1, 10):
            path = f"assets/{i}.gif"
            if os.path.exists(path):
                with open(path, "rb") as f:
                    b64 = base64.b64encode(f.read()).decode()
                    gifs.append(f"data:image/gif;base64,{b64}")
        return gifs

    gifs = load_gifs()

    components.html(f"""
    <div style="display:flex; flex-direction:column; align-items:center;">

        <img id="slideshow" style="
            width:350px;
            height:350px;
            object-fit:cover;
            border-radius:15px;
            box-shadow:0 8px 20px rgba(0,0,0,0.2);
            transition: opacity 0.6s ease-in-out;
        ">

        <hr style="width:60%; margin-top:20px; opacity:0.3;">

        <div style="
            text-align:center;
            color:white;
            opacity:0.85;
            font-size:14px;
            margin-top:10px;
        ">
            Made with ❤️ by <b>your favourite - Vipul Malyan</b>
        </div>

    </div>

    <script>
    const gifs = {gifs};
    let index = 0;
    const img = document.getElementById("slideshow");

    function showNextGif() {{
        img.style.opacity = 0;

        setTimeout(() => {{
            img.src = gifs[index];
            img.style.opacity = 1;
            index = (index + 1) % gifs.length;
        }}, 300);
    }}

    // preload first
    if (gifs.length > 0) {{
        img.src = gifs[0];
    }}

    // smooth loop
    setInterval(showNextGif, 2000);
    </script>
    """, height=500)

# -------------------------
# FINAL LAYOUT FIX
# -------------------------
st.markdown("""
<style>
html, body {
    overflow-x: hidden;
}
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 1rem !important;
}
section.main > div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    min-height: 90vh;
}
</style>
""", unsafe_allow_html=True)