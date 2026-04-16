import streamlit as st
import random

# Sayfa Ayarları
st.set_page_config(page_title="Temel İngilizce Öğren", page_icon="📝", layout="centered")

# --- TEMEL SEVİYE 100 KELİME ---
if 'words' not in st.session_state:
    st.session_state.words = [
        {"en": "Always", "tr": "Her zaman", "hint": "Hiç aksatmadan yapılan şeyler. ⏰"},
        {"en": "Beautiful", "tr": "Güzel", "hint": "Göze hoş gelen şeyler. ✨"},
        {"en": "Breakfast", "tr": "Kahvaltı", "hint": "Günün ilk öğünü. 🍳"},
        {"en": "Cheap", "tr": "Ucuz", "hint": "Fiyatı düşük olan. 🏷️"},
        {"en": "Difficult", "tr": "Zor", "hint": "Kolay olmayan. 🧩"},
        {"en": "Enough", "tr": "Yeterli", "hint": "Kafi, yeter. ✅"},
        {"en": "Friend", "tr": "Arkadaş", "hint": "Sevdiğimiz kişi. 🤝"},
        {"en": "Healthy", "tr": "Sağlıklı", "hint": "Vücudu iyi durumda olan. 🍎"},
        {"en": "Journey", "tr": "Yolculuk", "hint": "Bir yerden bir yere gitmek. ✈️"},
        {"en": "Kitchen", "tr": "Mutfak", "hint": "Yemek yapılan yer. 🔪"}
        # Buraya önceki listedeki diğer kelimeleri de ekleyebilirsin.
    ]

# --- STATE YÖNETİMİ ---
if 'current_word' not in st.session_state:
    st.session_state.current_word = random.choice(st.session_state.words)
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'show_hint' not in st.session_state:
    st.session_state.show_hint = False
if 'is_locked' not in st.session_state:
    st.session_state.is_locked = False # Yanlış cevapta formu kilitlemek için

def next_word():
    st.session_state.current_word = random.choice(st.session_state.words)
    st.session_state.show_hint = False
    st.session_state.is_locked = False
    st.rerun()

# --- ARAYÜZ ---
st.title("📝 Temel İngilizce Kelime Kartları")
st.write(f"Hoş geldin Utku! Kelimeleri tahmin etmeye çalış. 🚀")

st.metric("Skorun", st.session_state.score)
mode = st.selectbox("Mod Seçin", ["EN -> TR", "TR -> EN"], key="mode_selection")

st.divider()

word = st.session_state.current_word
target_question = word['en'] if mode == "EN -> TR" else word['tr']
correct_answer = word['tr'] if mode == "EN -> TR" else word['en']

st.markdown(f"<h1 style='text-align: center; color: #FF4B4B;'>{target_question}</h1>", unsafe_allow_html=True)

# İpucu Bölümü
if st.session_state.show_hint:
    st.info(f"💡 **İpucu:** {word['hint']}")
elif not st.session_state.is_locked:
    if st.button("İpucu Al"):
        st.session_state.show_hint = True
        st.rerun()

# Cevap Formu
with st.form(key='quiz_form', clear_on_submit=True):
    # Eğer cevap yanlışsa giriş alanını devre dışı bırakıyoruz (disabled)
    user_ans = st.text_input("Cevabın:", disabled=st.session_state.is_locked).strip().lower()
    submit_button = st.form_submit_button(label='Kontrol Et', disabled=st.session_state.is_locked)

if submit_button:
    # Esnek Kontrol: Cevap içinde geçiyor mu veya tam tersi (Ok/Okay kontrolü)
    if user_ans and (user_ans in correct_answer.lower() or correct_answer.lower() in user_ans):
        st.success(f"Tebrikler! Doğru: **{correct_answer}** 🎉")
        st.session_state.score += 10
        st.balloons()
        st.session_state.is_locked = True # Doğru bilince de yeni kelime beklesin
    else:
        st.error(f"Yanlış! Doğru cevap: **{correct_answer}** 😕")
        st.session_state.is_locked = True # Yanlış bilince kilitler

# Sadece Yeni Kelime Getir butonu çalışır durumda kalır
if st.session_state.is_locked:
    if st.button("Sıradaki Kelimeye Geç ➡️"):
        next_word()

st.divider()
st.caption("Not: 'Ok' yerine 'Okay' yazsanız da sistem kabul eder. Esnek cevap sistemi devrede! ⚡")
