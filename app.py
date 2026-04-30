import streamlit as st

# 1. Konfigurasi Dasar
st.set_page_config(page_title="AIini Influencer Hub", layout="wide")

# 2. CSS untuk Memaksa Tampilan HP Tetap Berdampingan
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    
    /* Memaksa 2 Kolom (Upload) Tetap Berdampingan di HP */
    [data-testid="column"] {
        width: 48% !important;
        flex: 1 1 48% !important;
        min-width: 48% !important;
    }
    
    /* Memaksa 3 Kolom (Scene, Lokasi, Durasi) Tetap Berdampingan di HP */
    .three-col [data-testid="column"] {
        width: 30% !important;
        flex: 1 1 30% !important;
        min-width: 30% !important;
    }

    .stButton>button { 
        width: 100%; border-radius: 12px; 
        background: linear-gradient(90deg, #00C9FF, #92FE9D); 
        color: black; border: none; font-weight: bold; height: 3.5rem;
    }
    
    .stTextArea textarea { background-color: #161b22; color: white; border: 1px solid #30363d; border-radius: 12px; }
    .scene-box { background-color: #1c2128; padding: 15px; border-radius: 10px; border: 1px solid #00C9FF; margin-bottom: 20px; }
    
    /* Ukuran teks label agar muat di layar sempit */
    label { font-size: 0.7rem !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.title("🎥 AIini Chelsea Engine")
st.caption("Fokus: Konsistensi Karakter & Aksesoris Full Body")

# --- BAGIAN 1: REFERENSI VISUAL (2 KOLOM) ---
st.write("### 🖼️ REFERENSI VISUAL")
col_char, col_outfit = st.columns(2)
with col_char:
    st.info("👤 **Karakter**")
    st.file_uploader("Upload Wajah", label_visibility="collapsed", key="u_char")
with col_outfit:
    st.info("👗 **Outfit**")
    st.file_uploader("Upload Baju", label_visibility="collapsed", key="u_out")

# --- BAGIAN 2: KOTAK ANALISIS (LOGIKA KOSONG) ---
st.write("---")
st.write("### 👤 KOTAK KARAKTER UTAMA")
if 'analysis' not in st.session_state:
    st.session_state.analysis = ""

if st.button("🪄 KLIK UNTUK ANALISIS CHARACTER SHEET"):
    # Pedoman Utama Konsistensi
    st.session_state.analysis = (
        "[MASTER CONSISTENCY]\n"
        "Name: Aiini Chelsea.\n"
        "Face: Slender, thin jawline, long wavy black hair.\n"
        "Mandate: Always full body, prioritize visible footwear/sandals.\n"
        "Quality: Photorealistic, 8k, high-fidelity."
    )

st.text_area("Pedoman Konsistensi:", value=st.session_state.analysis, height=130, placeholder="Kotak kosong. Klik tombol Analisis...")

# --- BAGIAN 3: SCENE, LOKASI, DURASI (3 KOLOM) ---
st.write("---")
st.markdown('<div class="three-col">', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.write("🔢 **Scene**")
    jumlah_scene = st.selectbox("Berapa:", list(range(1, 11)), key="s_count")
with c2:
    st.write("📍 **Lokasi**")
    pilih_lokasi = st.selectbox("Tempat:", ["Kamar Mewah", "Minimalis", "Polos", "Kafe", "Urban"], key="s_loc")
with c3:
    st.write("⏱️ **Durasi**")
    pilih_durasi = st.selectbox("Detik:", ["5s", "10s", "15s", "30s"], key="s_dur")
st.markdown('</div>', unsafe_allow_html=True)

# --- BAGIAN 4: GENERATE PROMPT ---
st.write("---")
if st.button("🚀 HASILKAN PROMPT"):
    if not st.session_state.analysis:
        st.error("Silakan klik 'Analisis Character Sheet' terlebih dahulu!")
    else:
        st.balloons()
        base_desc = "Aiini Chelsea, slender face, thin jawline, long wavy black hair"
        
        for i in range(1, jumlah_scene + 1):
            st.markdown(f'<div class="scene-box">', unsafe_allow_html=True)
            st.markdown(f"#### 🎬 SCENE {i} PROMPT")
            
            p_col1, p_col2 = st.columns(2)
            with p_col1:
                st.write("📸 **Gambar**")
                st.code(f"Full body photo, {base_desc}, outfit from reference, {pilih_lokasi}, scene {i} pose, visible sandals, 8k.", language="text")
            with p_col2:
                st.write("🎥 **Video**")
                st.code(f"AI Video, {pilih_durasi}, {base_desc}, action {i} at {pilih_lokasi}, consistent face, fabric physics, 4k.", language="text")
            st.markdown('</div>', unsafe_allow_html=True)
    
