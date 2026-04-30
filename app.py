import streamlit as st

st.set_page_config(page_title="AIini Influencer Hub", layout="wide")

# CSS UNTUK PAKSA BERDAMPINGAN DI HP
st.markdown("""
    <style>
    [data-testid="column"] {
        display: inline-block !important;
        width: 48% !important;
        min-width: 45% !important;
        vertical-align: top !important;
    }
    .three-col [data-testid="column"] {
        width: 31% !important;
        min-width: 30% !important;
    }
    .stButton>button { 
        width: 100%; border-radius: 12px; 
        background: linear-gradient(90deg, #00C9FF, #92FE9D); 
        color: black; border: none; font-weight: bold; height: 3rem;
    }
    .stTextArea textarea { background-color: #161b22; color: white; border: 1px solid #30363d; border-radius: 12px; }
    .scene-box { background-color: #1c2128; padding: 15px; border-radius: 12px; border: 1px solid #00C9FF; margin-bottom: 20px; }
    label { font-size: 0.75rem !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 AIini Chelsea Engine")

# --- 1. REFERENSI VISUAL ---
st.write("### 🖼️ REFERENSI VISUAL")
c1, c2 = st.columns(2)
with c1:
    st.file_uploader("👤 Karakter", key="char")
with c2:
    st.file_uploader("👗 Outfit", key="out")

# --- 2. KOTAK KARAKTER UTAMA (DINAMIS) ---
st.write("---")
st.write("### 👤 KOTAK KARAKTER UTAMA")

# Tombol analisis sekarang hanya memberikan template, Anda bisa edit warnanya di sini
if st.button("🪄 KLIK UNTUK ANALISIS CHARACTER SHEET"):
    st.session_state.analysis = (
        "Aiini Chelsea, slender face, thin jawline, grey hair, photorealistic, 8k, full body, visible sandals."
    )

# Jika belum ada isi, buat string kosong
if 'analysis' not in st.session_state:
    st.session_state.analysis = ""

# PENTING: Deskripsi ini bisa Anda edit manual di kotak sebelum klik "Hasilkan Prompt"
user_description = st.text_area("Edit Deskripsi Karakter Di Sini:", value=st.session_state.analysis, height=120)

# --- 3. SCENE, LOKASI, DURASI ---
st.write("---")
st.markdown('<div class="three-col">', unsafe_allow_html=True)
sc_col, lc_col, dr_col = st.columns(3)
with sc_col:
    jml_scene = st.selectbox("Scene:", list(range(1, 11)))
with lc_col:
    lokasi = st.selectbox("Lokasi:", ["Apartemen", "Minimalis", "Kafe", "Urban"])
with dr_col:
    durasi = st.selectbox("Durasi:", ["5s", "10s", "15s", "30s"])
st.markdown('</div>', unsafe_allow_html=True)

# --- 4. GENERATE PROMPT ---
st.write("---")
if st.button("🚀 HASILKAN PROMPT"):
    if not user_description:
        st.error("Isi dulu deskripsi karakter di kotak atas!")
    else:
        st.balloons()
        
        for i in range(1, jml_scene + 1):
            st.markdown(f'<div class="scene-box">', unsafe_allow_html=True)
            st.markdown(f"#### 🎬 HASIL SCENE {i}")
            
            p1, p2 = st.columns(2)
            with p1:
                st.write("📸 **Gambar**")
                # SEKARANG MENGGUNAKAN user_description LANGSUNG
                st.code(f"Photo of {user_description}, at {lokasi}, pose {i}, wearing outfit from reference, focus on footwear, cinematic lighting, 8k.", language="text")
            with p2:
                st.write("🎥 **Video**")
                st.code(f"AI Video, {durasi}, {user_description}, walking in {lokasi}, consistent face, clear sandals detail, 4k.", language="text")
            st.markdown('</div>', unsafe_allow_html=True)
                       
