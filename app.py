import streamlit as st
import random
import json
import os

# Sayfa Ayarları
st.set_page_config(
    page_title="Utku'nun Kelime Rehberi",
    page_icon="📝",
    layout="centered"
)

# --- KELİME YÜKLEME SİSTEMİ ---
def load_words():
    if os.path.exists('words.json'):
        try:
            with open('words.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                if data and isinstance(data, list):
                    return data
        except Exception as e:
            st.error(f"JSON Okuma Hatası: {e} ⚠️")
    
    return [
        ["Always", "Her zaman", "Hiç aksatmadan yapılanlar. ⏰", "A1"],
        ["Incredible", "İnanılmaz", "Büyüleyici durumlar için.", "B1"],
        ["Sovereignty", "Egemenlik", "Bağımsızlık sembolü.", "C1"]
    ]

all_words = load_words()

# --- STATE YÖNETİMİ ---
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'is_correct' not in st.session_state:
    st.session_state.is_correct = None
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'selected_level' not in st.session_state:
    st.session_state.selected_level = "Hepsi"

# --- YENİ: DÜĞME İLE SEVİYE SEÇİMİ (ANA SAYFA) ---
st.title("📖 Kelime Rehberi")
st.markdown("### 🎯 Bir Seviye Seçin")

# Yan yana düğmeler oluştur
levels = ["Hepsi", "A1", "A2", "B1", "B2"]
cols = st.columns(len(levels))

for i, lvl in enumerate(levels):
    # Aktif seviyeyi belirtmek için düğme stilini (isteğe bağlı) veya metni değiştirebilirsin
    label = f"⭐ {lvl}" if st.session_state.selected_level == lvl else lvl
    if cols[i].button(label, use_container_width=True):
        st.session_state.selected_level = lvl
        # Havuzu güncelle
        if lvl == "Hepsi":
            st.session_state.word_pool = all_words
        else:
            st.session_state.word_pool = [w for w in all_words if len(w) > 3 and w[3] == lvl]
        
        # Eğer boşsa varsayılana dön
        if not st.session_state.word_pool:
            st.warning(f"{lvl} seviyesinde kelime bulunamadı! ✨")
            st.session_state.word_pool = all_words
            
        random.shuffle(st.session_state.word_pool)
        st.session_state.current_index = 0
        st.session_state.answered = False
        st.rerun()

st.divider()

# Kelime havuzu başlangıçta yoksa oluştur
if 'word_pool' not in st.session_state:
    st.session_state.word_pool = all_words
    random.shuffle(st.session_state.word_pool)

def next_word():
    st.session_state.current_index += 1
    if st.session_state.current_index >= len(st.session_state.word_pool):
        random.shuffle(st.session_state.word_pool)
        st.session_state.current_index = 0
        st.toast("Seviye sonuna gelindi, yeniden karıştırıldı! 🔄")
    
    st.session_state.answered = False
    st.session_state.is_correct = None
    st.rerun()

# --- ÇALIŞMA EKRANI ---
current = st.session_state.word_pool[st.session_state.current_index]

col1, col2 = st.columns(2)
with col1:
    st.metric("Puan", st.session_state.score)
with col2:
    mode = st.selectbox("Çalışma Modu", ["EN -> TR", "TR -> EN"])

# Kelime Bilgileri
q_idx, a_idx = (0, 1) if mode == "EN -> TR" else (1, 0)
target_question = current[q_idx]
correct_answer = current[a_idx]
hint_text = current[2] if len(current) > 2 else "İpucu yok."
current_level = current[3] if len(current) > 3 else "Genel"

st.markdown(f"<p style='text-align: center; color: gray;'>Şu anki Seviye: <b>{st.session_state.selected_level}</b></p>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; color: #4A90E2;'>{target_question}</h1>", unsafe_allow_html=True)
st.info(f"💡 **İpucu:** {hint_text}")

# Cevap Formu
with st.form(key='quiz_form', clear_on_submit=True):
    user_ans = st.text_input("Cevabınız:", disabled=st.session_state.answered).strip().lower()
    submit_button = st.form_submit_button(label='Kontrol Et ✅', disabled=st.session_state.answered)

if submit_button:
    if user_ans:
        st.session_state.answered = True
        # Küçük bir tolerans: Cevap içinde geçiyorsa veya tam eşleşiyorsa
        if user_ans in correct_answer.lower() or correct_answer.lower() in user_ans:
            st.session_state.is_correct = True
            st.session_state.score += 10
        else:
            st.session_state.is_correct = False
        st.rerun()

# Sonuç Ekranı
if st.session_state.answered:
    if st.session_state.is_correct:
        st.success(f"Harika! Doğru cevap: **{correct_answer}** 🎉")
        st.balloons()
    else:
        st.error(f"Maalesef... Doğru cevap: **{correct_answer.upper()}** ❌")
    
    if st.button("Sıradaki Kelime ➡️"):
        next_word()
