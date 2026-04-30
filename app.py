import streamlit as st

st.set_page_config(page_title="AIini Engine Pro", layout="wide")

# CSS Custom untuk UI dan Konsistensi
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 12px; background: linear-gradient(90deg, #00C9FF, #92FE9D); color: black; border: none; font-weight: bold; height: 3rem; }
    .stTextArea textarea { background-color: #161b22; color: white; border: 1px solid #30363d; border-radius: 12px; }
    .copy-box { background-color: #1c2128; padding: 15px; border-radius: 10px; border-left: 5px solid #00C9FF; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

st.title("👗 AIini Chelsea: Influencer Engine")
st.caption("Mode Konsistensi Tinggi & Kontrol Durasi")

# --- SECTION 1: REFERENSI BERDAMPINGAN ---
st.write("### 🖼️ REFERENSI VISUAL")
col_char, col_cloth = st.columns(2)
with col_char:
    st.info("👤 **Karakter Utama**")
    up_char = st.file_uploader("Upload Wajah", label_visibility="collapsed", key="char")
with col_cloth:
    st.info("👗 **Outfit & Shoes**")
    up_cloth = st.file_uploader("Upload Pakaian", label_visibility="collapsed", key="cloth")

# --- SECTION 2: CHARACTER SHEET (UNTUK KONSISTENSI) ---
st.write("---")
st.write("### 👤 KOTAK KARAKTER UTAMA")
# Deskripsi dikunci untuk menjaga konsistensi wajah tirus/slender Chelsea
base_desc = "Aiini Chelsea, 20yo Indonesian girl, ultra-consistent face, slender face, thin jawline, long wavy black hair, neutral expression."
technical_fix = "High-fidelity skin, 8k, photorealistic, masterwork, maintain same facial features across all shots."

sheet_val = f"[CONSISTENCY SHEET]\nSubject: {base_desc}\nVisual: {technical_fix}\nView: Full Body Shot, showing footwear/sandals."
char_sheet = st.text_area("Character Consistency Master:", value=sheet_val, height=120)

# --- SECTION 3: LOKASI, ADEGAN, DURASI (BERDAMPINGAN) ---
st.write("---")
col_loc, col_act, col_dur = st.columns([1, 1, 1])

with col_loc:
    st.write("📍 **Lokasi**")
    lokasi = st.selectbox("Pilih Tempat:", [
        "Kamar Apartemen Mewah", 
        "Kamar Minimalis Aesthetic", 
        "Ruangan Polos (Studio)", 
        "Kafe Estetik", 
        "Jalanan Urban"
    ])

with col_act:
    st.write("🎬 **Adegan**")
    adegan_list = [
        "1. Berdiri Tenang (Full Body)",
        "2. Transisi Ganti Baju Cepat",
        "3. Berputar 360 Derajat",
        "4. Jalan ke Kamera (Catwalk)",
        "5. Duduk di Tepi Kasur",
        "6. Zoom ke Sepatu/Sandal",
        "7. Pose Influencer (Mirror)",
        "8. Transisi Kasual ke Formal",
        "9. Gerakan Lambat (Slowmo)",
        "10. Menoleh & Senyum"
    ]
    pilih_adegan = st.selectbox("Pilih Gerakan:", adegan_list)

with col_dur:
    st.write("⏱️ **Durasi**")
    durasi = st.select_slider("Durasi Video (Detik):", options=["5s", "10s", "15s", "30s", "60s"])

# --- SECTION 4: GENERATE OUTPUT ---
st.write("---")
if st.button("🚀 HASILKAN PROMPT KONSISTEN"):
    st.balloons()
    
    # Prompt Foto (Fokus pada Detail & Konsistensi)
    prompt_foto = f"RAW photo of {base_desc}, wearing outfit from reference, {lokasi}, {pilih_adegan}, full body, looking at camera, visible sandals/footwear, extreme detail, 8k, dslr, 85mm lens, --seed 1000"
    
    # Prompt Video (Fokus pada Gerakan & Durasi)
    prompt_video = f"Cinematic AI video, {durasi} duration, {base_desc}, {pilih_adegan}, in {lokasi}, consistent face identity, smooth motion, high-quality fabric physics, visible shoes, 4k, 60fps."

    out_foto, out_video = st.columns(2)
    with out_foto:
        st.subheader("📸 Prompt Gambar")
        st.code(prompt_foto, language="text")
        st.caption("Gunakan untuk generate base image (Midjourney/Leonardo)")
        
    with out_video:
        st.subheader("🎥 Prompt Video")
        st.code(prompt_video, language="text")
        st.caption(f"Gunakan untuk video {durasi} (Kling/Luma/Runway)")

    st.info("💡 **Tips Konsistensi:** Gunakan gambar hasil 'Prompt Gambar' sebagai *Image Reference* saat membuat video agar wajah tetap 100% sama.")
