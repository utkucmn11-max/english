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
    return [["Always", "Her zaman", "Hiç aksatmadan yapılanlar. ⏰"]]

# Kelimeleri sadece bir kez yükle ve karıştır
if 'word_pool' not in st.session_state:
    full_pool = load_words()
    random.shuffle(full_pool) # İlk başta karıştırıyoruz 🃏
    st.session_state.word_pool = full_pool
    st.session_state.current_index = 0 # Kaçıncı kelimede olduğumuzu tutar

# --- STATE YÖNETİMİ ---
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'is_correct' not in st.session_state:
    st.session_state.is_correct = None

def next_word():
    # Bir sonraki kelimeye geç
    st.session_state.current_index += 1
    
    # Eğer listedeki tüm kelimeler bittiyse, listeyi tekrar karıştır ve başa dön
    if st.session_state.current_index >= len(st.session_state.word_pool):
        random.shuffle(st.session_state.word_pool)
        st.session_state.current_index = 0
        st.toast("Tüm kelimeler bitti, liste yeniden karıştırıldı! 🔄", icon="🎯")

    st.session_state.answered = False
    st.session_state.is_correct = None
    st.rerun()

# --- ARAYÜZ ---
st.title("📖 Kelime Öğrenme Platformu")

# Kelime sayısını gösteren küçük bir bilgi
total_w = len(st.session_state.word_pool)
current_w = st.session_state.current_index + 1
st.caption(f"Kelime: {current_w} / {total_w} (Tekrar etmeden ilerliyor 🚀)")

st.metric("Skorun", st.session_state.score)
mode = st.selectbox("Mod Seçin", ["EN -> TR", "TR -> EN"])

st.divider()

# Mevcut Kelimeyi İndekse Göre Al
current = st.session_state.word_pool[st.session_state.current_index]
q_idx, a_idx = (0, 1) if mode == "EN -> TR" else (1, 0)
target_question = current[q_idx]
correct_answer = current[a_idx]
hint_text = current[2]

st.markdown(f"<h1 style='text-align: center; color: #4A90E2;'>{target_question}</h1>", unsafe_allow_html=True)
st.info(f"💡 **İpucu:** {hint_text}")

# Cevap Formu
with st.form(key='quiz_form', clear_on_submit=True):
    user_ans = st.text_input("Tahminin:", disabled=st.session_state.answered).strip().lower()
    submit_button = st.form_submit_button(label='Kontrol Et', disabled=st.session_state.answered)

if submit_button:
    if user_ans:
        st.session_state.answered = True
        if user_ans in correct_answer.lower() or correct_answer.lower() in user_ans:
            st.session_state.is_correct = True
            st.session_state.score += 10
        else:
            st.session_state.is_correct = False
        st.rerun()

# Sonuç Ekranı
if st.session_state.answered:
    if st.session_state.is_correct:
        st.success(f"Tebrikler Utku! Doğru cevap: **{correct_answer}** 🎉")
        st.balloons()
    else:
        st.error(f"Yanlış! Doğru cevap: **{correct_answer.upper()}** ❌")
        st.warning("Kutu kilitlendi. Hazır olduğunda sıradakine geç.")
    
    if st.button("Sıradaki Kelimeye Geç ➡️"):
        next_word()

st.divider()
