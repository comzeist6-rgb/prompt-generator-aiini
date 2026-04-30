import streamlit as st

st.set_page_config(page_title="AIini Influencer Hub", layout="wide")

# CSS Sakti untuk memaksa kolom tetap berdampingan di HP
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    
    /* Memaksa kolom upload dan menu tetap berdampingan di HP */
    [data-testid="column"] {
        width: 48% !important;
        flex: 1 1 48% !important;
        min-width: 48% !important;
    }
    
    /* Khusus untuk baris Lokasi & Durasi agar jadi 3 kolom kecil */
    .three-col [data-testid="column"] {
        width: 30% !important;
        flex: 1 1 30% !important;
        min-width: 30% !important;
    }

    .stButton>button { width: 100%; border-radius: 12px; background: linear-gradient(90deg, #00C9FF, #92FE9D); color: black; border: none; font-weight: bold; height: 3.5rem; }
    .stTextArea textarea { background-color: #161b22; color: white; border: 1px solid #30363d; border-radius: 12px; }
    .scene-box { background-color: #1c2128; padding: 15px; border-radius: 10px; border: 1px solid #00C9FF; margin-bottom: 20px; }
    
    /* Mengecilkan teks label agar muat berdampingan */
    label { font-size: 0.8rem !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 AIini Chelsea Engine")
st.caption("Edisi Force Side-by-Side (Tampilan Berdampingan)")

# --- 1. REFERENSI VISUAL (DIPAKSA BERDAMPINGAN) ---
st.write("### 🖼️ REFERENSI VISUAL")
col_char, col_outfit = st.columns(2)
with col_char:
    st.info("👤 **Karakter**")
    st.file_uploader("Wajah", label_visibility="collapsed", key="char")
with col_outfit:
    st.info("👗 **Outfit**")
    st.file_uploader("Baju/Sepatu", label_visibility="collapsed", key="outfit")

# --- 2. KOTAK KARAKTER UTAMA ---
st.write("---")
st.write("### 👤 KOTAK KARAKTER UTAMA")
if 'sheet_data' not in st.session_state:
    st.session_state.sheet_data = ""

if st.button("🪄 KLIK UNTUK ANALISIS CHARACTER SHEET"):
    st.session_state.sheet_data = (
        "[PRIMARY SHEET]\n"
        "Name: Aiini Chelsea. \n"
        "Features: Slender face, thin jawline, wavy black hair.\n"
        "Mandate: Full body, focus on footwear/sandals."
    )

st.text_area("Pedoman Konsistensi:", value=st.session_state.sheet_data, height=130, placeholder="Klik tombol di atas...")

# --- 3. JUMLAH SCENE, LOKASI, DURASI (TIGA KOLOM SEJAJAR) ---
st.write("---")
st.markdown('<div class="three-col">', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.write("🔢 **Scene**")
    jumlah_scene = st.selectbox("Total:", list(range(1, 11)), key="sc")
with c2:
    st.write("📍 **Lokasi**")
    pilih_lokasi = st.selectbox("Tempat:", ["Kamar Mewah", "Minimalis", "Polos", "Kafe", "Urban"], key="lc")
with c3:
    st.write("⏱️ **Durasi**")
    pilih_durasi = st.selectbox("Detik:", ["5s", "10s", "15s", "30s"], key="dr")
st.markdown('</div>', unsafe_allow_html=True)

# --- 4. OUTPUT PROMPT ---
st.write("---")
if st.button("🚀 HASILKAN PROMPT"):
    if not st.session_state.sheet_data:
        st.error("Klik tombol 'Analisis' dulu!")
    else:
        st.balloons()
        base = "Aiini Chelsea, slender face, thin jawline, long wavy black hair"
        for i in range(1, jumlah_scene + 1):
            st.markdown(f'<div class="scene-box">', unsafe_allow_html=True)
            st.markdown(f"#### 🎬 SCENE {i}")
            out_f, out_v = st.columns(2)
            with out_f:
                st.code(f"Full body shot, {base}, outfit from ref, {pilih_lokasi}, scene {i}, sandals detail, 8k.", language="text")
            with out_v:
                st.code(f"AI Video, {pilih_durasi}, {base}, action {i}, at {pilih_lokasi}, consistent face, 4k.", language="text")
            st.markdown('</div>', unsafe_allow_html=True)
            
