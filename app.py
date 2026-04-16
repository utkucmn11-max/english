import streamlit as st
import random

# Sayfa Ayarları
st.set_page_config(page_title="C2 English Master", page_icon="🎓", layout="centered")

# --- KELİME HAVUZU ---
if 'words' not in st.session_state:
    st.session_state.words = [
        {"en": "Always", "tr": "Her zaman", "hint": "Hiç aksatmadan yapılan şeyler için kullanılır. ⏰"},
        {"en": "Beautiful", "tr": "Güzel", "hint": "Göze hoş gelen şeyler için söylenir. ✨"},
        {"en": "Between", "tr": "Arasında", "hint": "İki şeyin ortasında olma durumu. ↕️"},
        {"en": "Breakfast", "tr": "Kahvaltı", "hint": "Günün ilk öğünü. 🍳"},
        {"en": "Busy", "tr": "Meşgul", "hint": "Yapacak çok işi olan kişi. 📞"},
        {"en": "Careful", "tr": "Dikkatli", "hint": "Hata yapmamaya çalışan, tedbirli. ⚠️"},
        {"en": "Cheap", "tr": "Ucuz", "hint": "Fiyatı düşük olan, pahalı olmayan. 🏷️"},
        {"en": "Clean", "tr": "Temiz", "hint": "Kirli olmayan, pak. 🧼"},
        {"en": "Country", "tr": "Ülke", "hint": "Türkiye, İngiltere gibi toprak parçaları. 🌍"},
        {"en": "Dangerous", "tr": "Tehlikeli", "hint": "Zarar verebilecek durumlar. 🚨"},
        {"en": "Daughter", "tr": "Kız evlat", "hint": "Bir ailenin kız çocuğu. 👧"},
        {"en": "Different", "tr": "Farklı", "hint": "Aynı olmayan, başka. 🌈"},
        {"en": "Difficult", "tr": "Zor", "hint": "Yapması kolay olmayan. 🧩"},
        {"en": "Early", "tr": "Erken", "hint": "Vaktinden önce veya sabahın ilk saatleri. 🌅"},
        {"en": "Enough", "tr": "Yeterli", "hint": "Kafi, daha fazlasına gerek yok. ✅"},
        {"en": "Expensive", "tr": "Pahalı", "hint": "Fiyatı yüksek olan. 💰"},
        {"en": "Famous", "tr": "Ünlü", "hint": "Herkes tarafından tanınan. 🌟"},
        {"en": "Fast", "tr": "Hızlı", "hint": "Yavaş olmayan, süratli. ⚡"},
        {"en": "Floor", "tr": "Yer / Kat", "hint": "Bastığımız zemin veya binanın katı. 🏢"},
        {"en": "Friend", "tr": "Arkadaş", "hint": "Sevdiğimiz ve güvendiğimiz kişi. 🤝"},
        {"en": "Garden", "tr": "Bahçe", "hint": "Evin dışındaki yeşil alan. 🏡"},
        {"en": "Healthy", "tr": "Sağlıklı", "hint": "Vücudu iyi durumda olan. 🍎"},
        {"en": "Helpful", "tr": "Yardımsever", "hint": "Başkalarına yardım etmeyi seven. 👋"},
        {"en": "Hungry", "tr": "Aç", "hint": "Yemek yeme isteği olan. 🍔"},
        {"en": "Important", "tr": "Önemli", "hint": "Değeri yüksek, önceliği olan. 🔑"},
        {"en": "Island", "tr": "Ada", "hint": "Etrafı suyla çevrili kara parçası. 🏝️"},
        {"en": "Journey", "tr": "Yolculuk", "hint": "Bir yerden bir yere gitme süreci. ✈️"},
        {"en": "Kitchen", "tr": "Mutfak", "hint": "Yemek yapılan yer. 🔪"},
        {"en": "Laugh", "tr": "Gülmek", "hint": "Komik bir şeye verilen tepki. 😂"},
        {"en": "Learn", "tr": "Öğrenmek", "hint": "Yeni bir bilgi edinmek. 📚"},
        {"en": "Leave", "tr": "Ayrılmak", "hint": "Bir yerden çıkıp gitmek. 🚪"},
        {"en": "Listen", "tr": "Dinlemek", "hint": "Kulağını vererek duymaya çalışmak. 🎧"},
        {"en": "Lucky", "tr": "Şanslı", "hint": "İşi rast giden kişi. 🍀"},
        {"en": "Market", "tr": "Pazar / Market", "hint": "Alışveriş yapılan yer. 🛒"},
        {"en": "Mistake", "tr": "Hata", "hint": "Yanlış yapılan şey. ❌"},
        {"en": "Mountain", "tr": "Dağ", "hint": "Çok yüksek yer şekli. 🏔️"},
        {"en": "Neighbor", "tr": "Komşu", "hint": "Yan evde oturan kişi. 🏠"},
        {"en": "Never", "tr": "Asla", "hint": "Hiçbir zaman. 🚫"},
        {"en": "Often", "tr": "Sık sık", "hint": "Çok kez yapılan. 🔄"},
        {"en": "Outside", "tr": "Dışarıda", "hint": "İçerinin zıttı. 🌳"},
        {"en": "Parent", "tr": "Ebeveyn", "hint": "Anne veya baba. 👨‍👩‍👧"},
        {"en": "People", "tr": "İnsanlar", "hint": "Kişilerin çoğul hali. 👥"},
        {"en": "Place", "tr": "Yer", "hint": "Mekan, konum. 📍"},
        {"en": "Pocket", "tr": "Cep", "hint": "Kıyafette eşya konulan yer. 👖"},
        {"en": "Quiet", "tr": "Sessiz", "hint": "Gürültüsüz ortam. 🤫"},
        {"en": "Ready", "tr": "Hazır", "hint": "Tamamlanmış, bekleyen. 🏁"},
        {"en": "Remember", "tr": "Hatırlamak", "hint": "Unutmamak, akla getirmek. 🧠"},
        {"en": "Rich", "tr": "Zengin", "hint": "Çok parası olan. 💎"},
        {"en": "River", "tr": "Nehir", "hint": "Akan su kütlesi. 🌊"},
        {"en": "Share", "tr": "Paylaşmak", "hint": "Bölüşmek. 🍕"},
        {"en": "Simple", "tr": "Basit", "hint": "Karmaşık olmayan, kolay. 💡"},
        {"en": "Sleepy", "tr": "Uykulu", "hint": "Uyumak isteyen kişi. 🥱"},
        {"en": "Smile", "tr": "Gülümsemek", "hint": "Mutluluk ifadesi. 😊"},
        {"en": "Sometimes", "tr": "Bazen", "hint": "Ara sıra. ⏳"},
        {"en": "Street", "tr": "Sokak", "hint": "Evlerin önündeki yol. 🛣️"},
        {"en": "Strong", "tr": "Güçlü", "hint": "Kuvvetli. 💪"},
        {"en": "Thirsty", "tr": "Susamış", "hint": "Su içmek isteyen. 💧"},
        {"en": "Ticket", "tr": "Bilet", "hint": "Otobüs veya sinema için gerekli kağıt. 🎟️"},
        {"en": "Together", "tr": "Birlikte", "hint": "Beraberce. 👨‍👩‍👦"},
        {"en": "Travel", "tr": "Seyahat etmek", "hint": "Gezmek, yeni yerler görmek. 🌍"},
        {"en": "Understand", "tr": "Anlamak", "hint": "Bir şeyi kavramak. ✅"},
        {"en": "Until", "tr": "Kadar", "hint": "Belli bir zamana dek. 🕒"},
        {"en": "Vacation", "tr": "Tatil", "hint": "Dinlenmek için gidilen zaman. 🏖️"},
        {"en": "Village", "tr": "Köy", "hint": "Şehirden küçük yerleşim yeri. 🏡"},
        {"en": "Visit", "tr": "Ziyaret etmek", "hint": "Birine veya bir yere gitmek. 👋"},
        {"en": "Wait", "tr": "Beklemek", "hint": "Zamanın geçmesini beklemek. ⏳"},
        {"en": "Weather", "tr": "Hava durumu", "hint": "Güneşli, yağmurlu gibi durumlar. ☀️"},
        {"en": "Weekly", "tr": "Haftalık", "hint": "Haftada bir olan. 🗓️"},
        {"en": "Window", "tr": "Pencere", "hint": "Evin dışarıya açılan camı. 🪟"},
        {"en": "Winter", "tr": "Kış", "hint": "En soğuk mevsim. ❄️"},
        {"en": "Worker", "tr": "İşçi", "hint": "Çalışan kişi. 👷"},
        {"en": "World", "tr": "Dünya", "hint": "Üzerinde yaşadığımız gezegen. 🌏"},
        {"en": "Write", "tr": "Yazmak", "hint": "Kağıda not düşmek. ✍️"},
        {"en": "Young", "tr": "Genç", "hint": "Yaşlı olmayan. 👶"},
        {"en": "Answer", "tr": "Cevap", "hint": "Soruya verilen karşılık. 💬"},
        {"en": "Believe", "tr": "İnanmak", "hint": "Bir şeyin doğru olduğunu düşünmek. 🙏"},
        {"en": "Bottle", "tr": "Şişe", "hint": "Su koyduğumuz kap. 🧴"},
        {"en": "Bridge", "tr": "Köprü", "hint": "Yolları birbirine bağlayan yapı. 🌉"},
        {"en": "Change", "tr": "Değiştirmek", "hint": "Farklı hale getirmek. 🔄"},
        {"en": "Choose", "tr": "Seçmek", "hint": "Karar vermek. 👉"},
        {"en": "Cloud", "tr": "Bulut", "hint": "Gökyüzündeki beyaz kümeler. ☁️"},
        {"en": "Company", "tr": "Şirket", "hint": "İş yeri. 🏢"},
        {"en": "Create", "tr": "Oluşturmak", "hint": "Yaratmak, yapmak. ✨"},
        {"en": "Dinner", "tr": "Akşam yemeği", "hint": "Günün son büyük öğünü. 🍽️"},
        {"en": "Dream", "tr": "Rüya", "hint": "Uyurken görülen şeyler. 😴"},
        {"en": "Everywhere", "tr": "Her yer", "hint": "Tüm mekanlar. 🗺️"},
        {"en": "Experience", "tr": "Deneyim", "hint": "Tecrübe. 🎓"},
        {"en": "Feeling", "tr": "Duygu", "hint": "His. ❤️"},
        {"en": "Follow", "tr": "Takip etmek", "hint": "Arkadan gelmek veya izlemek. 👣"},
        {"en": "Future", "tr": "Gelecek", "hint": "Daha yaşanmamış zaman. 🚀"},
        {"en": "History", "tr": "Tarih", "hint": "Geçmişte olan olaylar. 📜"},
        {"en": "Imagine", "tr": "Hayal etmek", "hint": "Zihinde canlandırmak. 🌈"},
        {"en": "Knowledge", "tr": "Bilgi", "hint": "Öğrenilen şeylerin bütünü. 💡"},
        {"en": "Memory", "tr": "Hafıza", "hint": "Anı, hatırlanan şey. 🖼️"},
        {"en": "Nature", "tr": "Doğa", "hint": "Yeşillik, hayvanlar ve çevre. 🌿"},
        {"en": "Possible", "tr": "Mümkün", "hint": "Olabilir, ihtimal dahilinde. ✅"},
        {"en": "Reason", "tr": "Sebep", "hint": "Neden. ❓"},
        {"en": "Success", "tr": "Başarı", "hint": "Hedefe ulaşma durumu. 🏆"},
        {"en": "Thought", "tr": "Düşünce", "hint": "Fikir. 💭"},
        {"en": "Victory", "tr": "Zafer", "hint": "Kazanma, başarı. ✌️"}
    
    
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
