import streamlit as st
import random

# Sayfa Ayarları
st.set_page_config(page_title="C2 English Master", page_icon="🎓", layout="centered")

# --- KELİME HAVUZU (Örnek 1000 kelimeye genişletilebilir) ---
if 'words' not in st.session_state:
    st.session_state.words = [
        {"en": "Ubiquitous", "tr": "Her yerde bulunan", "hint": "Gözünüzü çevirdiğiniz her yerde olan, yaygın (Örn: Akıllı telefonlar)."},
        {"en": "Impeccable", "tr": "Kusursuz", "hint": "Hatasız, tertemiz, 'perfect' kelimesinin çok daha üst seviyesi."},
        {"en": "Eloquent", "tr": "Hitabeti güçlü", "hint": "Güzel ve etkileyici konuşan kişiler için kullanılır."},
        {"en": "Fathom", "tr": "Kavramak", "hint": "Bir derinliği ölçmek veya bir şeyi tam olarak anlamak."},
        {"en": "Serendipity", "tr": "Mutlu tesadüf", "hint": "Aranmadığı halde bulunan çok güzel şeylerin durumu."},
        {"en": "Pragmatic", "tr": "Gerçekçi", "hint": "Teoriden çok uygulamaya ve faydaya odaklanan yaklaşım."},
        {"en": "Ambiguous", "tr": "Belirsiz", "hint": "Birden fazla anlama gelebilen, net olmayan durumlar."},
        {"en": "Resilient", "tr": "Dayanıklı", "hint": "Zorluklar karşısında çabuk toparlanan, esnek güç."}
    ]

# --- STATE YÖNETİMİ ---
if 'current_word' not in st.session_state:
    st.session_state.current_word = random.choice(st.session_state.words)
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'show_hint' not in st.session_state:
    st.session_state.show_hint = False
if 'mode' not in st.session_state:
    st.session_state.mode = "EN -> TR"

# --- FONKSİYONLAR ---
def next_word():
    st.session_state.current_word = random.choice(st.session_state.words)
    st.session_state.show_hint = False
    st.session_state.user_answer = ""

# --- ARAYÜZ ---
st.title("🎓 C2 Level Vocabulary Master")
st.write(f"Hoş geldin Utku! C2 seviyesinde uzmanlaşmak için doğru yerdesin. ✨")

# Skor ve Mod Seçimi
col1, col2 = st.columns([1, 1])
with col1:
    st.metric("Skorun", st.session_state.score)
with col2:
    st.session_state.mode = st.selectbox("Mod Seçin", ["EN -> TR", "TR -> EN"])

st.divider()

# Kelime Kartı
word = st.session_state.current_word
target_question = word['en'] if st.session_state.mode == "EN -> TR" else word['tr']
correct_answer = word['tr'] if st.session_state.mode == "EN -> TR" else word['en']

st.markdown(f"<h1 style='text-align: center; color: #4A90E2;'>{target_question}</h1>", unsafe_allow_html=True)

# İpucu Bölümü
if st.session_state.show_hint:
    st.info(f"💡 **İpucu:** {word['hint']}")
else:
    if st.button("Bir ipucu verir misin?"):
        st.session_state.show_hint = True
        st.rerun()

# Cevap Alanı
user_ans = st.text_input("Cevabın nedir?", key="user_answer").strip()

if st.button("Kontrol Et"):
    if user_ans.lower() == correct_answer.lower():
        st.success(f"Harikasın! 🎉 Doğru cevap: **{correct_answer}**")
        st.session_state.score += 10
        st.balloons()
        # Bir sonraki kelimeye geçmek için buton
        if st.button("Sıradaki Kelime ➡️"):
            next_word()
            st.rerun()
    else:
        st.error("Üzgünüm, bu pek doğru değil. Tekrar dene veya ipucuna bak! 🤔")

st.divider()
if st.button("Yeni Kelime Getir 🔄"):
    next_word()
    st.rerun()