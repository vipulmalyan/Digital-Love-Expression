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
</style>
""", unsafe_allow_html=True)

# -------------------------
# STEP 1
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
# STEP 2
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
# STEP 3
# -------------------------
elif st.session_state.step == 3:

    confetti(emojis=["💖", "❤️", "💕", "💘"])
    st.balloons()

    st.markdown("<div class='big-text'>YAAAYYY 💖💖💖</div>", unsafe_allow_html=True)

    # 🎵 AUDIO
    audio_path = "assets/audio.mp3"
    if os.path.exists(audio_path):
        autoplay_audio(audio_path)

    # 🎥 MAIN VIDEO (REPLACES GIFs)
    # 🎥 MAIN VIDEO (FIXED)
    video_path = "assets/video.mp4"

    if os.path.exists(video_path):
        with open(video_path, "rb") as f:
            video_bytes = f.read()
            video_b64 = base64.b64encode(video_bytes).decode()

        components.html(f"""
        <div style="display:flex; flex-direction:column; align-items:center;">

            <video width="350" autoplay loop muted playsinline style="
                border-radius:15px;
                box-shadow:0 8px 20px rgba(0,0,0,0.2);
            ">
                <source src="data:video/mp4;base64,{video_b64}" type="video/mp4">
            </video>

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