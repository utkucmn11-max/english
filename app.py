import streamlit as st
import random
import json
import os

# Sayfa Ayarları
st.set_page_config(page_title="1000 Kelime Master", page_icon="📖", layout="centered")

# --- KELİME YÜKLEME ---
def load_words():
    # Eğer words.json varsa oradan oku, yoksa örnek liste oluştur
    if os.path.exists('words.json'):
        with open('words.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return [{"en": "Example", "tr": "Örnek", "hint": "Dosya bulunamadı uyarısı."}]

if 'words' not in st.session_state:
    st.session_state.words = load_words()

# --- STATE YÖNETİMİ ---
if 'current_word' not in st.session_state:
    st.session_state.current_word = random.choice(st.session_state.words)
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'show_hint' not in st.session_state:
    st.session_state.show_hint = False
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'is_correct' not in st.session_state:
    st.session_state.is_correct = None

def next_word():
    st.session_state.current_word = random.choice(st.session_state.words)
    st.session_state.show_hint = False
    st.session_state.answered = False
    st.session_state.is_correct = None
    st.rerun()

# --- ARAYÜZ ---
st.title("📖 1000 Kelime Öğrenme Platformu")
st.write(f"Hoş geldin Utku! Temel seviyeden uzmanlığa... ✨")

st.metric("Puanın", st.session_state.score)
mode = st.selectbox("Çalışma Modu", ["EN -> TR", "TR -> EN"])

st.divider()

word = st.session_state.current_word
target_question = word['en'] if mode == "EN -> TR" else word['tr']
correct_answer = word['tr'] if mode == "EN -> TR" else word['en']

st.markdown(f"<h1 style='text-align: center; color: #4A90E2;'>{target_question}</h1>", unsafe_allow_html=True)

# İpucu
if not st.session_state.answered:
    if st.session_state.show_hint:
        st.info(f"💡 İpucu: {word['hint']}")
    else:
        if st.button("İpucu Al"):
            st.session_state.show_hint = True
            st.rerun()

# Cevap Formu
with st.form(key='quiz_form', clear_on_submit=True):
    # Yanlış veya Doğru fark etmeksizin cevap verildiyse kutu kilitlenir
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

# Cevap Sonucu ve Bekleme Ekranı
if st.session_state.answered:
    if st.session_state.is_correct:
        st.success(f"HARİKASIN! 🎉 Cevap: {correct_answer}")
        st.balloons()
    else:
        # Doğru cevabı burada gösteriyoruz
        st.error(f"YANLIŞ! ❌ Doğru Cevap: {correct_answer.upper()}")
        st.warning("Yukarıdaki kutu kilitlendi. Doğruyu incele ve devam et.")
    
    if st.button("Sıradaki Kelime ➡️"):
        next_word()
