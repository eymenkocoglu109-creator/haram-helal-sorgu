import streamlit as st
import base64

def emoji_yagmuru(emoji):
    st.markdown(
        f"""
        <div class="emoji-container">
            <style>
                .emoji {{
                    position: fixed;
                    top: -50px;
                    font-size: 24px;
                    animation: fall 3s linear infinite;
                    z-index: 9999;
                }}
                @keyframes fall {{
                    to {{
                        transform: translateY(105vh);
                    }}
                }}
            </style>
            {"".join([f'<div class="emoji" style="left: {__import__("random").randint(0, 100)}%; animation-delay: {__import__("random").random() * 3}s;">{emoji}</div>' for _ in range(30)])}
        </div>
        """,
        unsafe_allow_html=True
    )
# 'base64' importuna artık gerek yok, istersen silebilirsin.

def arka_plan_yap(resim_dosyasi):
    # Dosyayı okuyup koda çeviriyoruz
    with open(resim_dosyasi, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    
    css_kodlari = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap');
    
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    }}
    
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, input {{
        font-family: 'Cinzel', serif !important;
    }}

    .main .block-container {{
        background-color: rgba(255, 255, 255, 0.85);
        padding: 3rem;
        border-radius: 30px;
        max-width: 850px;
        margin-top: 50px;
    }}
    </style>
    """
    st.markdown(css_kodlari, unsafe_allow_html=True)

# --- 2. UYGULAMA ---

# Önce arka planı yükle (Resim dosyanla aynı isim olmalı!)
# --- 2. UYGULAMA ---

# Yeni arka plan resminin linkini buraya tanımlıyoruz (Daha sağlam olması için)
# --- 2. UYGULAMA ---

# Explorer'daki dosya adın 'kudüs.jpg' olduğu için aynısını yazıyoruz
try:
    arka_plan_yap('kudüs.jpg')
except Exception as e:
    st.error(f"Resim yüklenemedi! Dosya adının 'kudüs.jpg' olduğundan emin ol. Hata: {e}")


# Fonksiyonu, bu linkle çağırıyoruz.
arka_plan_yap("kudüs.jpg")

st.title("🚫 BOYKOT SORGULAMA")


boykot = ["cocacola", "pepsi", "starbucks", "akmina", "aquafına", "7up", "cappy", "damla", "fanta", "sprite", "lipton", "redbull", "monster", "erikli", "hayat", "fruko", "actıvıa", "sırma", "lipton", "doğadan", "powerade", "fruko", "nescafe", "sırma", "nestle", "tropicana", "yedigün", "evian", "alpro", "pellegrıno", "algida", "bounty", "cheetos", "calve", "crunch", "çerezza", "danette", "doritos", "falım","first","hellmanns","kitkat","kent","knorr","kelloggs","danette","danone","m&ms","milka","mars","missbon","oreo","milkyway","pringles","polo","olips","rocco","ruffles","sana","nestle","axe","clear","dove","ipana","signal","cif","prill","finish","omo","danino","yumoş","rinso","persil","vim","aptamil","prima",]
boykotdeğil = ["ülker","içim","torku","niğde gazozu","lc waikiki","mavi","koton","vestel","beko","flo","inci","polaris","istikbal","yataş","bellona","eti","pınar","uludağ","beypazarı","sek","sütaş","çaykur","doğuş","tat","dimes","abc","peros","bingo","porçöz","papia","a101","bim","şok","hakmar","filli boya","casper","reeder","sunny","kumtel","greyder","aytaç","superfresh"]

eylem = st.text_input("Sorgulamak istediğiniz eylemi girin:")

if eylem:
    eylem_temiz = eylem.lower().strip()
    st.markdown("---")
    if eylem_temiz in boykot:
        st.error(f"❌ {eylem.capitalize()} boykot listesinde.")
        emoji_yagmuru("❌")
    elif eylem_temiz in boykotdeğil:
        st.success(f"✅ {eylem.capitalize()} boykot listesinde değil.")
        emoji_yagmuru("✅")
    else:
        st.info(f"❓ '{eylem}' hakkında bilgi bulunmamaktadır.")



