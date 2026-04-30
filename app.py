import streamlit as st

st.set_page_config(page_title="AIini Influencer Hub", layout="wide")

# CSS untuk UI Profesional & Tombol Salin
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 12px; background: linear-gradient(90deg, #00C9FF, #92FE9D); color: black; border: none; font-weight: bold; height: 3.5rem; }
    .stTextArea textarea { background-color: #161b22; color: white; border: 1px solid #30363d; border-radius: 12px; }
    .copy-container { background-color: #1c2128; padding: 15px; border-radius: 10px; border: 1px solid #30363d; position: relative; }
    .stSelectbox [data-baseweb="select"] { background-color: #161b22; border-radius: 12px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 AIini Chelsea: Professional Influencer Engine")
st.caption("Fokus: Konsistensi Karakter, Detail Outfit & Full Body")

# --- 1. REFERENSI VISUAL (BERDAMPINGAN) ---
st.write("### 🖼️ REFERENSI VISUAL")
col_char, col_outfit = st.columns(2)
with col_char:
    st.info("👤 **Karakter**")
    up_char = st.file_uploader("Upload Wajah Utama", label_visibility="collapsed", key="char")
with col_outfit:
    st.info("👗 **Outfit**")
    up_outfit = st.file_uploader("Upload Pakaian & Sepatu", label_visibility="collapsed", key="outfit")

# --- 2. KOTAK KARAKTER UTAMA (DENGAN ANALISIS) ---
st.write("---")
st.write("### 👤 KOTAK KARAKTER UTAMA")

# State untuk menyimpan hasil analisis
if 'analysis_result' not in st.session_state:
    st.session_state.analysis_result = ""

if st.button("🪄 KLIK UNTUK ANALISIS CHARACTER SHEET"):
    # Logika simulasi analisis karakter dan outfit
    st.session_state.analysis_result = (
        "[PRIMARY CHARACTER SHEET]\n"
        "Identity: Aiini Chelsea, 20yo Indonesian girl.\n"
        "Face: Slender face, thin jawline, long wavy black hair, high cheekbones.\n"
        "Outfit Context: Integrating style from uploaded outfit reference.\n"
        "Visual Rule: Full body shot mandatory, emphasize footwear/sandals details, hyper-realistic texture."
    )

char_sheet = st.text_area(
    "Hasil Analisis (Pedoman Konsistensi):", 
    value=st.session_state.analysis_result, 
    height=150,
    placeholder="Klik tombol di atas untuk menganalisis gambar..."
)

# --- 3. SCENE, LOKASI, DURASI (TIGA KOLOM SEJAJAR) ---
st.write("---")
col_scene, col_loc, col_dur = st.columns(3)

with col_scene:
    st.write("🎬 **Scene**")
    scene_options = [f"Scene {i}: " + desc for i, desc in enumerate([
        "Full body pose standing", "Quick outfit swap transition", "360-degree rotation", 
        "Walking to camera", "Sitting on bed edge", "Close up on sandals/shoes", 
        "Influencer mirror selfie", "Casual to formal transition", "Slow motion aesthetic walk", 
        "Looking back and smiling"
    ], 1)]
    pilih_scene = st.selectbox("Pilih Adegan:", scene_options)

with col_loc:
    st.write("📍 **Lokasi**")
    pilih_lokasi = st.selectbox("Pilih Tempat:", [
        "Kamar Apartemen Mewah", "Kamar Minimalis Aesthetic", 
        "Ruangan Polos", "Kafe Estetik", "Jalanan Urban"
    ])

with col_dur:
    st.write("⏱️ **Durasi**")
    pilih_durasi = st.selectbox("Total Durasi Video:", ["5 Detik", "10 Detik", "15 Detik", "30 Detik"])

# --- 4. OUTPUT PROMPT (TERPISAH DENGAN ICON SALIN) ---
st.write("---")
if st.button("🚀 HASILKAN PROMPT"):
    if not st.session_state.analysis_result:
        st.warning("Mohon lakukan 'Analisis Character Sheet' terlebih dahulu agar prompt konsisten!")
    else:
        st.balloons()
        
        # Logika Prompt
        desc_base = "Aiini Chelsea, slender face, thin jawline, long wavy black hair"
        p_foto = f"Photorealistic image of {desc_base}, wearing outfit from reference, {pilih_lokasi}, {pilih_scene}, full body shot, visible sandals/footwear, 8k, highly detailed skin."
        p_video = f"Cinematic AI video, {pilih_durasi} duration, {desc_base}, {pilih_scene} at {pilih_lokasi}, seamless motion, consistent identity, focus on shoes detail, 4k, 60fps."

        out_f, out_v = st.columns(2)
        
        with out_f:
            st.subheader("📸 Prompt Gambar")
            st.code(p_foto, language="text")
            st.caption("📋 Klik icon di pojok kanan atas kotak untuk menyalin")
            
        with out_v:
            st.subheader("🎥 Prompt Video")
            st.code(p_video, language="text")
            st.caption("📋 Klik icon di pojok kanan atas kotak untuk menyalin")

st.info("💡 **Tips:** Pastikan 'Character Sheet' sudah terisi agar AI mengenali identitas Chelsea secara konsisten di setiap scene.")
        
