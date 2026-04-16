import streamlit as st
import random
import json
import os

# Sayfa Ayarları
st.set_page_config(page_title="Utku'nun Kelime Rehberi", page_icon="📝", layout="centered")

# --- KELİME YÜKLEME SİSTEMİ ---
def load_words():
    if os.path.exists('words.json'):
        with open('words.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        # Dosya yoksa örnek liste (Hata almamak için)
        return [["Always", "Her zaman", "Hiç aksatmadan yapılanlar. ⏰"]]

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

# Mevcut Kelime Bilgileri
current = st.session_state.current_word
q_idx, a_idx = (0, 1) if mode == "EN -> TR" else (1, 0)
target_question = current[q_idx]
correct_answer = current[a_idx]
hint_text = current[2]

# Kelimeyi Göster
st.markdown(f"<h1 style='text-align: center; color: #4A90E2;'>{target_question}</h1>", unsafe_allow_html=True)

# --- İPUCU BÖLÜMÜ (Artık Önceden Görünüyor) ---
st.info(f"💡 **İpucu:** {hint_text}")

# Cevap Formu
with st.form(key='quiz_form', clear_on_submit=True):
    # Tahmin yaparken kutu açık, cevap verince kilitlenir
    user_ans = st.text_input("Tahminin:", disabled=st.session_state.answered).strip().lower()
    submit_button = st.form_submit_button(label='Kontrol Et', disabled=st.session_state.answered)

if submit_button:
    st.session_state.answered = True
    # Esnek Kontrol (ok/okay mantığı)
    if user_ans and (user_ans in correct_answer.lower() or correct_answer.lower() in user_ans):
        st.session_state.is_correct = True
        st.session_state.score += 10
    else:
        st.session_state.is_correct = False
    st.rerun()

# Sonuç ve Bekleme Ekranı
if st.session_state.answered:
    if st.session_state.is_correct:
        st.success(f"Tebrikler Utku! Doğru cevap: **{correct_answer}** 🎉")
        st.balloons()
    else:
        # Yanlış cevapta doğrusunu büyükçe gösterir
        st.error(f"Yanlış! Doğru cevap: **{correct_answer.upper()}** ❌")
        st.warning("Yukarıdaki kutu kilitlendi. Sıradaki kelimeye geçebilirsin.")
    
    if st.button("Sıradaki Kelimeye Geç ➡️"):
        next_word()

st.divider()
st.caption("İpucu her zaman yukarıda görünür, yanlış yaparsan kutu kilitlenir. 🚀")
