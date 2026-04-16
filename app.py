import streamlit as st
import random

# Sayfa Ayarları
st.set_page_config(page_title="İngilizce Kelime Öğren", page_icon="📝", layout="centered")

# --- 100 TEMEL KELİME HAVUZU ---
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
        {"en": "Kitchen", "tr": "Mutfak", "hint": "Yemek yapılan yer. 🔪"},
        {"en": "Answer", "tr": "Cevap", "hint": "Soruya verilen karşılık. 💬"},
        {"en": "Believe", "tr": "İnanmak", "hint": "Doğru olduğunu düşünmek. 🙏"},
        {"en": "Bridge", "tr": "Köprü", "hint": "Yolları bağlayan yapı. 🌉"},
        {"en": "Choose", "tr": "Seçmek", "hint": "Karar vermek. 👉"},
        {"en": "Dangerous", "tr": "Tehlikeli", "hint": "Zarar verebilecek durumlar. 🚨"},
        {"en": "Different", "tr": "Farklı", "hint": "Aynı olmayan. 🌈"},
        {"en": "Early", "tr": "Erken", "hint": "Vaktinden önce. 🌅"},
        {"en": "Famous", "tr": "Ünlü", "hint": "Tanınan kişi. 🌟"},
        {"en": "Garden", "tr": "Bahçe", "hint": "Evin dışındaki yeşil alan. 🏡"},
        {"en": "Hungry", "tr": "Aç", "hint": "Yemek yeme isteği. 🍔"},
        # ... (Diğer kelimeler buraya eklenebilir)
    ]

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
st.title("📝 Kelime Öğrenme Platformu")
st.write(f"Efendim hoş geldin Utku! Yanlış yaparsan doğrusunu görüp öğrenebilirsin. ✨")

st.metric("Skorun", st.session_state.score)
mode = st.selectbox("Mod Seçin", ["EN -> TR", "TR -> EN"], key="mode_selection")

st.divider()

word = st.session_state.current_word
target_question = word['en'] if mode == "EN -> TR" else word['tr']
correct_answer = word['tr'] if mode == "EN -> TR" else word['en']

st.markdown(f"<h1 style='text-align: center; color: #4A90E2;'>{target_question}</h1>", unsafe_allow_html=True)

# İpucu Bölümü
if not st.session_state.answered:
    if st.session_state.show_hint:
        st.info(f"💡 **İpucu:** {word['hint']}")
    else:
        if st.button("İpucu Ver 💡"):
            st.session_state.show_hint = True
            st.rerun()

# Cevap Formu
with st.form(key='quiz_form', clear_on_submit=True):
    user_ans = st.text_input("Cevabın:", disabled=st.session_state.answered).strip().lower()
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

# --- CEVAP GÖSTERİM ALANI ---
if st.session_state.answered:
    if st.session_state.is_correct:
        st.success(f"TEBRİKLER! 🎉 Doğru cevap: **{correct_answer}**")
        st.balloons()
    else:
        # Yanlış cevap durumunda doğrusunu göster
        st.error(f"YANLIŞ! ❌ Doğru cevap: **{correct_answer.upper()}**")
        st.info("Doğru cevabı incele ve hazır olduğunda diğer kelimeye geç. 💪")
    
    if st.button("Sıradaki Kelimeye Geç ➡️"):
        next_word()

st.divider()
st.caption("Not: Yanlış yaptığında kutucuk kilitlenir, böylece sadece doğru cevaba odaklanabilirsin. 🚀")
