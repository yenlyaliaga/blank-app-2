import streamlit as st
import time

st.set_page_config(page_title="Feliz Aniversario Mi Osi", page_icon="💖", layout="centered")

# Estilos personalizados
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(to bottom, #ffe6f0, #fff0f5);
    }
    .title {
        text-align: center;
        font-size: 50px;
        color: #d63384;
        font-weight: bold;
        margin-top: 20px;
    }
    .subtitle {
        text-align: center;
        font-size: 24px;
        color: #6f42c1;
        margin-bottom: 20px;
    }
    .message {
        background-color: rgba(255,255,255,0.8);
        padding: 25px;
        border-radius: 20px;
        font-size: 20px;
        color: #444;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }
    .footer {
        text-align: center;
        margin-top: 30px;
        font-size: 18px;
        color: #d63384;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Animación simple
placeholder = st.empty()
for i in range(3):
    placeholder.markdown(
        f"<div class='title'>💖 Feliz Aniversario Mi Osi 💖</div>",
        unsafe_allow_html=True,
    )
    time.sleep(0.4)

st.markdown("<div class='subtitle'>Gracias por cada momento juntos ✨</div>", unsafe_allow_html=True)

st.image(
    "https://images.unsplash.com/photo-1518199266791-5375a83190b7?q=80&w=1200&auto=format&fit=crop",
    use_container_width=True,
)

st.markdown(
    """
    <div class='message'>
    Hoy celebramos nuestro aniversario y todos los recuerdos hermosos que hemos construido juntos 💕<br><br>
    Gracias por tu cariño, paciencia y por hacer cada día especial. ✨<br><br>
    Espero seguir compartiendo muchos momentos más contigo. 💖
    </div>
    """,
    unsafe_allow_html=True,
)

st.balloons()

st.markdown(
    "<div class='footer'>Con mucho cariño para mi Osi 💌</div>",
    unsafe_allow_html=True,
)
