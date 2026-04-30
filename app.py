import streamlit as st

st.set_page_config(page_title="AIini Influencer Hub", layout="wide")

# CSS Custom
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 12px; background: linear-gradient(90deg, #00C9FF, #92FE9D); color: black; border: none; font-weight: bold; height: 3.5rem; }
    .stTextArea textarea { background-color: #161b22; color: white; border: 1px solid #30363d; border-radius: 12px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎥 AIini Chelsea: Professional Influencer Engine")
st.caption("Fokus: Penentuan Jumlah Scene, Lokasi & Durasi")

# --- 1. REFERENSI VISUAL (BERDAMPINGAN) ---
st.write("### 🖼️ REFERENSI VISUAL")
col_char, col_outfit = st.columns(2)
with col_char:
    st.info("👤 **Karakter**")
    st.file_uploader("Karakter Utama", label_visibility="collapsed", key="char")
with col_outfit:
    st.info("👗 **Outfit**")
    st.file_uploader("Pakaian & Sepatu", label_visibility="collapsed", key="outfit")

# --- 2. KOTAK KARAKTER UTAMA ---
st.write("---")
st.write("### 👤 KOTAK KARAKTER UTAMA")
if 'sheet_data' not in st.session_state:
    st.session_state.sheet_data = ""

if st.button("🪄 KLIK UNTUK ANALISIS CHARACTER SHEET"):
    st.session_state.sheet_data = (
        "[CONSISTENCY MASTER SHEET]\n"
        "● Persona: Aiini Chelsea, young Indonesian influencer.\n"
        "● Facial Identity: Slender face, thin jawline, long wavy black hair.\n"
        "● Mandate: Full body framing, high-detail focus on footwear (sandals/shoes)."
    )

st.text_area("Pedoman Konsistensi:", value=st.session_state.sheet_data, height=120, placeholder="Klik tombol di atas...")

# --- 3. SCENE (JUMLAH), LOKASI, DURASI (BERDAMPINGAN) ---
st.write("---")
col_sc, col_lc, col_dr = st.columns(3)

with col_sc:
    st.write("🔢 **Jumlah Scene**")
    # Sekarang ini untuk menentukan MAU BERAPA SCENE (1-10)
    jumlah_scene = st.selectbox("Mau Berapa Scene?", list(range(1, 11)))

with col_lc:
    st.write("📍 **Lokasi**")
    pilih_lokasi = st.selectbox("Pilih Tempat:", ["Kamar Apartemen Mewah", "Kamar Minimalis Aesthetic", "Ruangan Polos", "Kafe Modern", "Jalanan Urban"])

with col_dr:
    st.write("⏱️ **Durasi**")
    pilih_durasi = st.selectbox("Durasi per Video:", ["5 Detik", "10 Detik", "15 Detik", "30 Detik"])

# --- 4. OUTPUT PROMPT ---
st.write("---")
if st.button("🚀 HASILKAN PROMPT"):
    if not st.session_state.sheet_data:
        st.error("Lakukan analisis terlebih dahulu!")
    else:
        st.balloons()
        base_chelsea = "Aiini Chelsea, slender face, thin jawline, long wavy black hair"
        
        # Output looping berdasarkan JUMLAH SCENE yang dipilih
        st.subheader(f"✅ Hasil untuk {jumlah_scene} Scene")
        
        for i in range(1, jumlah_scene + 1):
            with st.expander(f"KLIK UNTUK MELIHAT PROMPT SCENE {i}", expanded=(i==1)):
                col_f, col_v = st.columns(2)
                with col_f:
                    st.markdown(f"**📸 Prompt Gambar (Scene {i})**")
                    st.code(f"Full body photo of {base_chelsea}, wearing outfit from reference, scene {i} variation, {pilih_lokasi}, highly detailed footwear, 8k.", language="text")
                with col_v:
                    st.markdown(f"**🎥 Prompt Video (Scene {i})**")
                    st.code(f"Cinematic video, {pilih_durasi} duration, {base_chelsea}, scene {i} action, at {pilih_lokasi}, seamless motion, 4k.", language="text")

st.info(f"Aplikasi akan menghasilkan {jumlah_scene} variasi prompt yang berbeda untuk menjaga alur konten Anda.")
