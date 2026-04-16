import streamlit as st
import random

# Sayfa Ayarları
st.set_page_config(page_title="C2 English Master", page_icon="🎓", layout="centered")

# --- KELİME HAVUZU ---
if 'words' not in st.session_state:
    st.session_state.words = [
        {"en": "Ubiquitous", "tr": "Her yerde bulunan", "hint": "Gözünüzü çevirdiğiniz her yerde olan, yaygın."},
        {"en": "Impeccable", "tr": "Kusursuz", "hint": "Hatasız, 'perfect' kelimesinin üst seviyesi."},
        {"en": "Eloquent", "tr": "Hitabeti güçlü", "hint": "Güzel ve etkileyici konuşan kişiler için kullanılır."},
        {"en": "Fathom", "tr": "Kavramak", "hint": "Bir şeyi tam olarak anlamak veya derinliğini ölçmek."},
        {"en": "Serendipity", "tr": "Mutlu tesadüf", "hint": "Beklenmedik anda gelen güzel şans."},
        {"en": "Pragmatic", "tr": "Gerçekçi", "hint": "Teoriden çok uygulamaya ve faydaya odaklanan."},
        {"en": "Ambiguous", "tr": "Belirsiz", "hint": "Net olmayan, iki farklı yöne çekilebilen."},
        {"en": "Resilient", "tr": "Dayanıklı", "hint": "Zorluklar karşısında çabuk toparlanan."}
    ]

# --- STATE YÖNETİMİ ---
if 'current_word' not in st.session_state:
    st.session_state.current_word = random.choice(st.session_state.words)
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'show_hint' not in st.session_state:
    st.session_state.show_hint = False
if 'answered_correctly' not in st.session_state:
    st.session_state.answered_correctly = False

# --- FONKSİYONLAR ---
def next_word():
    st.session_state.current_word = random.choice(st.session_state.words)
    st.session_state.show_hint = False
    st.session_state.answered_correctly = False
    # Formu sıfırlamak için rerun tetikliyoruz
    st.rerun()

# --- ARAYÜZ ---
st.title("🎓 C2 Level Vocabulary Master")
st.write(f"Hoş geldin Utku! Günlük akıcılık için kelime avına başlayalım. ✨")

# Skor ve Mod
col1, col2 = st.columns([1, 1])
with col1:
    st.metric("Skorun", st.session_state.score)
with col2:
    mode = st.selectbox("Mod Seçin", ["EN -> TR", "TR -> EN"], key="mode_selection")

st.divider()

# Kelime Bilgileri
word = st.session_state.current_word
target_question = word['en'] if mode == "EN -> TR" else word['tr']
correct_answer = word['tr'] if mode == "EN -> TR" else word['en']

st.markdown(f"<h1 style='text-align: center; color: #4A90E2;'>{target_question}</h1>", unsafe_allow_html=True)

# İpucu Bölümü
if st.session_state.show_hint:
    st.info(f"💡 **İpucu:** {word['hint']}")
else:
    if st.button("Bir ipucu verir misin?"):
        st.session_state.show_hint = True
        st.rerun()

# Cevap Formu
with st.form(key='quiz_form', clear_on_submit=True):
    user_ans = st.text_input("Cevabın nedir?").strip()
    submit_button = st.form_submit_button(label='Kontrol Et')

if submit_button:
    if user_ans.lower() == correct_answer.lower():
        st.success(f"Harikasın! 🎉 Doğru cevap: **{correct_answer}**")
        st.session_state.score += 10
        st.session_state.answered_correctly = True
        st.balloons()
    else:
        st.error(f"Üzgünüm, doğru cevap **{correct_answer}** olmalıydı. 🤔")

# Yeni Kelime Butonu (Her zaman görünür ve formun dışında)
if st.button("Yeni Kelime Getir 🔄"):
    next_word()
