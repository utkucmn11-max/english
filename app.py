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
        {"en": "Ubiquitous", "tr": "Her yerde bulunan", "hint": "Gözünüzü çevirdiğiniz her yerde olan, yaygın."},
        {"en": "Impeccable", "tr": "Kusursuz", "hint": "Hatasız, 'perfect' kelimesinin üst seviyesi."},
        {"en": "Eloquent", "tr": "Hitabeti güçlü", "hint": "Güzel ve etkileyici konuşan kişiler için kullanılır."},
        {"en": "Fathom", "tr": "Kavramak", "hint": "Bir şeyi tam olarak anlamak veya derinliğini ölçmek."},
        {"en": "Serendipity", "tr": "Mutlu tesadüf", "hint": "Beklenmedik anda gelen güzel şans."},
        {"en": "Pragmatic", "tr": "Gerçekçi", "hint": "Teoriden çok uygulamaya ve faydaya odaklanan."},
        {"en": "Ambiguous", "tr": "Belirsiz", "hint": "Net olmayan, iki farklı yöne çekilebilen."},
        {"en": "Resilient", "tr": "Dayanıklı", "hint": "Zorluklar karşısında çabuk toparlanan."},
        {"en": "Ephemeral", "tr": "Kısa ömürlü", "hint": "Çok kısa süren, geçici (Örn: Kelebeğin ömrü)."},
        {"en": "Tenacious", "tr": "Azimli", "hint": "Vazgeçmeyen, bir şeye sıkı sıkıya bağlı kalan."},
        {"en": "Benevolent", "tr": "Hayırsever", "hint": "İyiliksever, başkalarına yardım etmeyi seven."},
        {"en": "Enigma", "tr": "Bilmecemsi", "hint": "Anlaşılması güç, gizemli durum veya kişi."},
        {"en": "Infallible", "tr": "Hata yapmaz", "hint": "Asla yanılmayan, kusursuz işleyen."},
        {"en": "Mitigate", "tr": "Hafifletmek", "hint": "Bir acıyı veya sorunu daha az şiddetli hale getirmek."},
        {"en": "Obsolete", "tr": "Modası geçmiş", "hint": "Artık kullanılmayan, eski tip."},
        {"en": "Plausible", "tr": "Akla yatkın", "hint": "İnanılabilir, mantıklı görünen."},
        {"en": "Scrupulous", "tr": "Titiz", "hint": "Çok dikkatli, ahlaki kurallara çok bağlı."},
        {"en": "Venerable", "tr": "Muhterem", "hint": "Yaşından veya bilgeliğinden dolayı saygı duyulan."},
        {"en": "Alacrity", "tr": "İsteklilik", "hint": "Bir şeyi yapmaya karşı duyulan büyük heves ve hız."},
        {"en": "Anomaly", "tr": "Anormallik", "hint": "Genel kuralın dışındaki sapma."},
        {"en": "Capricious", "tr": "Değişken", "hint": "Keyfi kararlar veren, sağı solu belli olmayan."},
        {"en": "Diligence", "tr": "Çalışkanlık", "hint": "Bir işi özenle ve sabırla yapma durumu."},
        {"en": "Exacerbate", "tr": "Kötüleştirmek", "hint": "Mevcut bir sorunu daha da berbat hale getirmek."},
        {"en": "Fastidious", "tr": "Titiz", "hint": "Zor beğenen, detaylara aşırı önem veren."},
        {"en": "Garrulous", "tr": "Geveze", "hint": "Özellikle önemsiz konularda çok konuşan."},
        {"en": "Haughty", "tr": "Kibirli", "hint": "Başkalarını küçümseyen, kendini çok üstün gören."},
        {"en": "Inherent", "tr": "Doğasında olan", "hint": "Bir şeyin temel yapısında bulunan, ayrılmaz."},
        {"en": "Juxtaposition", "tr": "Yan yana koyma", "hint": "Zıtlık yaratmak için iki şeyi bitişik yerleştirme."},
        {"en": "Lethargic", "tr": "Uyuşuk", "hint": "Enerjisi düşük, uykulu ve hareketsiz."},
        {"en": "Meticulous", "tr": "Özenli", "hint": "Hata yapmamak için çok dikkatli ve detaycı davranan."},
        {"en": "Nefarious", "str": "Haince", "hint": "Çok kötü, ahlaksızca veya suç teşkil eden."},
        {"en": "Ostentatious", "tr": "Gösterişli", "hint": "Hava atmak için yapılan, şatafatlı."},
        {"en": "Pensive", "tr": "Düşünceli", "hint": "Hüzünlü veya derin bir şekilde düşüncelere dalmış."},
        {"en": "Quaint", "tr": "Antika ve şirin", "hint": "Eski moda ama çekici ve güzel."},
        {"en": "Reticent", "tr": "Sessiz", "hint": "Duygularını ve düşüncelerini paylaşmayan, çekingen."},
        {"en": "Sycophant", "tr": "Yalaka", "hint": "Çıkar sağlamak için başkalarına aşırı dalkavukluk yapan."},
        {"en": "Taciturn", "tr": "Az konuşan", "hint": "Yapı olarak sessiz, pek konuşmayan."},
        {"en": "Uncanny", "tr": "Esrarengiz", "hint": "Tuhaf, ürkütücü derecede olağanüstü."},
        {"en": "Vindictive", "tr": "Kin tutan", "hint": "İntikam peşinde koşan, bağışlamayan."},
        {"en": "Wary", "tr": "İhtiyatlı", "hint": "Tedbirli, tehlikelere karşı uyanık."},
        {"en": "Zeal", "tr": "Şevk", "hint": "Bir amaç uğruna duyulan büyük tutku."},
        {"en": "Amiable", "tr": "Cana yakın", "hint": "Dost canlısı, hoşsohbet kişi."},
        {"en": "Candid", "tr": "Samimi", "hint": "Dürüst, içten ve sakınmadan konuşan."},
        {"en": "Docile", "tr": "Uysal", "hint": "Kolay yönetilen, söz dinleyen."},
        {"en": "Frivolous", "tr": "Ciddiyetsiz", "hint": "Önemsiz, boş işlerle uğraşan."},
        {"en": "Incite", "tr": "Kışkırtmak", "hint": "Birini kötü bir şey yapmaya teşvik etmek."},
        {"en": "Luminous", "tr": "Işıltılı", "hint": "Karanlıkta parlayan, ışık yayan."},
        {"en": "Nostalgia", "tr": "Özlem", "hint": "Geçmişe duyulan duygusal bağlılık."},
        {"en": "Ornate", "tr": "Süslü", "hint": "Aşırı dekore edilmiş, karmaşık desenli."},
        {"en": "Precocious", "tr": "Erken gelişmiş", "hint": "Yaşına göre zekası çok ilerde olan (Çocuklar için)."},
        {"en": "Reciprocal", "tr": "Karşılıklı", "hint": "Her iki tarafın da birbirine aynı şekilde davrandığı."},
        {"en": "Spontaneous", "tr": "Anlık", "hint": "Planlanmadan, kendiliğinden gelişen."},
        {"en": "Versatile", "tr": "Çok yönlü", "hint": "Birçok farklı işi yapabilen veya alana uyum sağlayan."},
        {"en": "Abstain", "tr": "Sakınmak", "hint": "Bir şeyi yapmaktan veya tüketmekten kaçınmak."},
        {"en": "Boisterous", "tr": "Gürültülü", "hint": "Enerjik, neşeli ama biraz fazla gürültülü."},
        {"en": "Collaborate", "tr": "İşbirliği yapmak", "hint": "Ortak bir amaç için beraber çalışmak."},
        {"en": "Deviate", "tr": "Sapmak", "hint": "Ana yoldan veya kuraldan dışarı çıkmak."},
        {"en": "Emulate", "tr": "Örnek almak", "hint": "Birini takdir edip onun gibi olmaya çalışmak."},
        {"en": "Fortuitous", "tr": "Tesadüfi", "hint": "Şans eseri olan, planlanmamış."},
        {"en": "Gregarious", "tr": "Sokulgan", "hint": "İnsanlarla vakit geçirmeyi seven, sosyal."},
        {"en": "Inevitable", "tr": "Kaçınılmaz", "hint": "Olması kesin olan, engellenemez."},
        {"en": "Lucid", "tr": "Berrak", "hint": "Anlaşılması çok kolay, net (Zihin veya anlatım)."},
        {"en": "Mundane", "tr": "Sıradan", "hint": "Dünyevi, heyecansız, günlük işler."},
        {"en": "Novice", "tr": "Acemi", "hint": "Bir işte yeni olan, deneyimsiz."},
        {"en": "Obstinate", "tr": "İnatçı", "hint": "Fikrini değiştirmemekte direnen."},
        {"en": "Perudent", "tr": "Sağduyulu", "hint": "Geleceği düşünerek hareket eden, akıllıca."},
        {"en": "Quell", "tr": "Yatıştırmak", "hint": "Bir isyanı veya korkuyu bastırmak."},
        {"en": "Reclusive", "tr": "İnzivada", "hint": "Toplumdan uzak tek başına yaşayan."},
        {"en": "Sovereign", "tr": "Egemen", "hint": "Kendi kendini yöneten, bağımsız güç."},
        {"en": "Transient", "tr": "Geçici", "hint": "Kısa süreli kalan, kalıcı olmayan."},
        {"en": "Uphold", "tr": "Savunmak", "hint": "Bir kararı veya yasayı desteklemek, sürdürmek."},
        {"en": "Vigilant", "tr": "Uyanık", "hint": "Tehlikelere karşı her an tetikte olan."},
        {"en": "Witty", "tr": "Hazırcevap", "hint": "Zekice ve komik şakalar yapan."},
        {"en": "Yearn", "tr": "Hasret çekmek", "hint": "Bir şeyi çok şiddetli arzulamak."},
        {"en": "Abundant", "tr": "Bol", "hint": "Gereğinden fazla miktarda olan."},
        {"en": "Belligerent", "tr": "Kavgacı", "hint": "Saldırgan, savaşa meyilli."},
        {"en": "Complacent", "tr": "Halinden memnun", "hint": "Gereğinden fazla özgüvenli, gelişime kapalı."},
        {"en": "Dormant", "tr": "Uykuda", "hint": "Aktif olmayan ama ölmemiş (Örn: Yanardağ)."},
        {"en": "Enthrall", "tr": "Büyülemek", "hint": "Tüm dikkati üzerine çekip hayran bırakmak."},
        {"en": "Fickle", "tr": "Maymun iştahlı", "hint": "Sürekli fikir değiştiren, sadık olmayan."},
        {"en": "Gratuitous", "tr": "Gereksiz", "hint": "Nedensiz yere yapılan, fazlalık."},
        {"en": "Hypocrisy", "tr": "İkiyüzlülük", "hint": "İnandığı gibi davranmama durumu."},
        {"en": "Inquisitive", "tr": "Meraklı", "hint": "Öğrenmeye ve soru sormaya hevesli."},
        {"en": "Lament", "tr": "Ağıt yakmak", "hint": "Bir kayıp için derin üzüntü duymak."},
        {"en": "Malleable", "tr": "Şekillenebilir", "hint": "Kolayca etkilenebilen veya bükülebilen."},
        {"en": "Nonchalant", "tr": "Kayıtsız", "hint": "Aşırı rahat, soğukkanlı ve umursamaz."},
        {"en": "Obscure", "tr": "Belirsiz", "hint": "Tanınmamış veya anlaşılması zor."},
        {"en": "Pensive", "tr": "Dalgın", "hint": "Derin düşüncelere dalmış, biraz hüzünlü."},
        {"en": "Quintessential", "tr": "Mükemmel örnek", "hint": "Bir şeyin en tipik ve saf örneği olan."},
        {"en": "Rampant", "tr": "Şahlanmış", "hint": "Kontrolsüzce yayılan (Örn: Hastalık)."},
        {"en": "Stoic", "tr": "Metanetli", "hint": "Acılara karşı duygularını belli etmeden dayanan."},
        {"en": "Trivial", "tr": "Ivır zıvır", "hint": "Çok küçük, önemsiz detaylar."},
        {"en": "Ubiquity", "tr": "Yaygınlık", "hint": "Her yerde bulunma durumu."},
        {"en": "Vociferous", "tr": "Yaygaracı", "hint": "Fikirlerini bağırarak, gürültülü ifade eden."},
        {"en": "Wanderlust", "tr": "Gezgin ruh", "hint": "Dünyayı gezme konusundaki güçlü arzu."},
        {"en": "Xenophobia", "tr": "Yabancı korkusu", "hint": "Farklı olanlara veya yabancılara duyulan nefret/korku."},
        {"en": "Yield", "tr": "Ürün vermek", "hint": "Hem verim sağlamak hem de boyun eğmek."},
        {"en": "Zenith", "tr": "Zirve", "hint": "Bir şeyin ulaştığı en yüksek nokta."}
    
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
