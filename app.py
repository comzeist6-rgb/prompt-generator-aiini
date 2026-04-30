import streamlit as st

st.set_page_config(page_title="AIini Influencer Hub", layout="wide")

st.markdown("""
    <style>
    [data-testid="column"] { width: 48% !important; flex: 1 1 48% !important; min-width: 48% !important; }
    .three-col [data-testid="column"] { width: 30% !important; flex: 1 1 30% !important; min-width: 30% !important; }
    .stButton>button { border-radius: 12px; background: linear-gradient(90deg, #00C9FF, #92FE9D); font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 AIini Chelsea Engine")

st.write("### 🖼️ REFERENSI VISUAL")
c1, c2 = st.columns(2)
with c1: st.file_uploader("Karakter", key="c")
with c2: st.file_uploader("Outfit", key="o")

if st.button("🪄 ANALISIS CHARACTER SHEET"):
    st.session_state.res = "Aiini Chelsea, slender face, long wavy hair, full body focus."

st.text_area("Sheet:", value=st.session_state.get('res', ''), height=100)

st.markdown('<div class="three-col">', unsafe_allow_html=True)
sc, lc, dr = st.columns(3)
with sc: scene = st.selectbox("Scene:", list(range(1, 11)))
with lc: loc = st.selectbox("Lokasi:", ["Apartemen", "Kafe", "Urban"])
with dr: dur = st.selectbox("Durasi:", ["5s", "10s", "15s"])
st.markdown('</div>', unsafe_allow_html=True)

if st.button("🚀 HASILKAN PROMPT"):
    for i in range(1, scene + 1):
        f, v = st.columns(2)
        f.code(f"Photo Scene {i}")
        v.code(f"Video Scene {i}")
