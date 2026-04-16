import streamlit as st
import random
import json
import os

# Sayfa Ayarları
st.set_page_config(page_title="Kelime Kartları", page_icon="📝", layout="centered")

# --- KELİME YÜKLEME SİSTEMİ ---
def load_words():
    if os.path.exists('words.json'):
        try:
            with open('words.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                if data and isinstance(data, list):
                    return data
        except Exception as e:
            st.error(f"JSON Okuma Hatası: {e}")
    # Dosya yoksa veya hatalıysa boş kalmasın
    return [["Always", "Her zaman", "Hiç aksatmadan yapılanlar. ⏰"]]

# Kelimeleri yükle ve karıştır
if 'word_pool' not in st.session_state:
    st.session_state.word_pool = load_words()
    random.shuffle(st.session_state.word_pool)
    st.session_state.current_index = 0

# --- STATE YÖNETİMİ ---
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'is_correct' not in st.session_state:
    st.session_state.is_correct = None

def next_word():
    st.session_state.current_index += 1
    # Liste bittiyse başa dön ve karıştır
    if st.session_state.current_index >= len(st.session_state.word_pool):
        random.shuffle(st.session_state.word_pool)
        st.session_state.current_index = 0
        st.toast("Liste bitti, yeniden karıştırıldı! 🔄")
    
    st.session_state.answered = False
    st.session_state.is_correct = None
    st.rerun()

# --- ARAYÜZ ---
st.title("📖 Kelime Rehberi")

# Hata Veren Kritik Bölge (Düzeltildi)
try:
    current = st.session_state.word_pool[st.session_state.current_index]
except IndexError:
    st.session_state.current_index = 0
    current = st.session_state.word_pool[0]

st.metric("Skor", st.session_state.score)
mode = st.selectbox("Mod Seçin", ["EN -> TR", "TR -> EN"])

st.divider()

# Kelime Bilgileri (JSON Yapısına Uygun)
q_idx, a_idx = (0, 1) if mode == "EN -> TR" else (1, 0)
target_question = current[q_idx]
correct_answer = current[a_idx]
hint_text = current[2] if len(current) > 2 else "İpucu bulunamadı."

st.markdown(f"<h1 style='text-align: center; color: #4A90E2;'>{target_question}</h1>", unsafe_allow_html=True)
st.info(f"💡 **İpucu:** {hint_text}")

# Cevap Formu
with st.form(key='quiz_form', clear_on_submit=True):
    user_ans = st.text_input("Tahminin:", disabled=st.session_state.answered).strip().lower()
    submit_button = st.form_submit_button(label='Kontrol Et', disabled=st.session_state.answered)

if submit_button:
    if user_ans:
        st.session_state.answered = True
        # Küçük harf ve esnek kontrol
        if user_ans in correct_answer.lower() or correct_answer.lower() in user_ans:
            st.session_state.is_correct = True
            st.session_state.score += 10
        else:
            st.session_state.is_correct = False
        st.rerun()

# Sonuç Ekranı
if st.session_state.answered:
    if st.session_state.is_correct:
        st.success(f"Tebrikler! Doğru cevap: **{correct_answer}** 🎉")
        st.balloons()
    else:
        st.error(f"Yanlış! Doğru cevap: **{correct_answer.upper()}** ❌")
    
    if st.button("Sıradaki Kelime ➡️"):
        next_word()
