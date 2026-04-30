import streamlit as st

st.set_page_config(page_title="Generator Petunjuk Adegan", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 10px; background: linear-gradient(90deg, #ff4b4b, #4b4bff); color: white; height: 3.5em; font-weight: bold; }
    .stTextArea textarea { background-color: #161b22; color: white; border: 1px solid #30363d; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("Generator 🌸 Petunjuk Adegan")
st.caption("V2 · FLEKSIBEL")

if st.button("🔄 Atur Ulang"):
    st.rerun()

st.write("### 🖼️ REFERENSI")
col1, col2 = st.columns(2)
with col1:
    st.info("**Karakter**")
    st.file_uploader("Upload 1", label_visibility="collapsed")
with col2:
    st.info("**Pakaian**")
    st.file_uploader("Upload 2", label_visibility="collapsed")

st.write("### 👤 KARAKTER UTAMA")
char_desc = st.text_area("Detail Karakter:", value="Aiini Chelsea, slender face, thin jawline, long wavy hair.", height=150)

st.write("### 📍 LOKASI")
lokasi = st.selectbox("Pilih Lokasi:", ["Kafe Estetik", "Jalanan Urban", "Mall Mewah", "Studio Foto"])

st.write("### 🎬 ADEGAN")
adegan = st.selectbox("Pilih Adegan:", ["Adegan 1", "Adegan 2", "Adegan 3"])

if st.button("🚀 HASILKAN PROMPT"):
    st.success("Berhasil!")
    st.code(f"{char_desc}\n\nLocation: {lokasi}, Action: {adegan}", language="markdown")
  
