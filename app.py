import streamlit as st
import random
import json
import os

# Sayfa Ayarları
st.set_page_config(page_title="Utku'nun Kelime Rehberi", page_icon="📝", layout="centered")

# --- KELİME YÜKLEME SİSTEMİ ---
def load_words():
    # Dosya yoksa hata vermemesi için boş bir liste döndürür
    if os.path.exists('words.json'):
        with open('words.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        # Dosya bulunamazsa yedek liste
        return [["Example", "Örnek", "JSON dosyası bulunamadı!"]]

if 'word_pool' not in st.session_state:
    st.session_state.word_pool = load_words()

# --- STATE YÖNETİMİ ---
if 'current_word' not in st.session_state:
    st.session_state.current_word = random.choice(st.session_state.word_pool)
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'is_correct' not in st.session_state:
    st.session_state.is_correct = None

def next_word():
    st.session_state.current_word = random.choice(st.session_state.word_pool)
    st.session_state.answered = False
    st.session_state.is_correct = None
    st.rerun()

# --- ARAYÜZ ---
st.title("📖 Kelime Öğrenme Platformu")
st.metric("Skorun", st.session_state.score)
mode = st.selectbox("Mod Seçin", ["EN -> TR", "TR -> EN"])

st.divider()

# Kelime Bilgileri
current = st.session_state.current_word
q_idx, a_idx = (0, 1) if mode == "EN -> TR" else (1, 0)
target_question = current[q_idx]
correct_answer = current[a_idx]

st.markdown(f"<h1 style='text-align: center;'>{target_question}</h1>", unsafe_allow_html=True)

# Cevap Formu
with st.form(key='quiz_form', clear_on_submit=True):
    # Kilitlenme özelliği devrede
    user_ans = st.text_input("Tahminin:", disabled=st.session_state.answered).strip().lower()
    submit_button = st.form_submit_button(label='Kontrol Et', disabled=st.session_state.answered)

if submit_button:
    st.session_state.answered = True
    if user_ans and (user_ans in correct_answer.lower() or correct_answer.lower() in user_ans):
        st.session_state.is_correct = True
        st.session_state.score += 10
    else:
        st.session_state.is_correct = False
    st.rerun()

# Sonuç ve Bekleme Ekranı
if st.session_state.answered:
    if st.session_state.is_correct:
        st.success(f"Tebrikler! Doğru cevap: **{correct_answer}** 🎉")
        st.balloons()
    else:
        st.error(f"Yanlış! Doğru cevap: **{correct_answer.upper()}** ❌")
        st.info(f"💡 İpucu: {current[2]}")
    
    if st.button("Sıradaki Kelime ➡️"):
        next_word()
