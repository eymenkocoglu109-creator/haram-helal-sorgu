import streamlit as st
import base64

# --- 1. ARKA PLAN TARİFİ (Bunu bir kez kopyalaman yeterli) ---
def emoji_yagmuru(emoji):
    # Bu kod ekranın üstünden seçtiğin emojiyi yağdırır
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
def arka_plan_yap(resim_dosyasi):
    
    with open(resim_dosyasi, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    
    # f-string karmaşasını önlemek için CSS'i dışarıda hazırlıyoruz
    css_kodlari = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap');
    
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: 50%;
        background-position: center;
        background-repeat: no-repeat;
    }}
    
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, input {{
        font-family: 'Cinzel', serif !important;
    }}

    .stTextInput {{
        text-align: center;
        padding-top: 20px;
    }}
    
    .stTextInput > div > div > input {{
        font-size: 30px !important;
        height: 80px !important;
        text-align: center !important;
        border-radius: 20px !important;
        border: 2px solid #D4AF37 !important;
    }}

    .stTextInput label {{
        font-size: 26px !important;
        justify-content: center !important;
        display: flex !important;
    }}

    .main .block-container {{
        background-color: rgba(255, 255, 255, 0.85);
        padding: 4rem;
        border-radius: 30px;
        max-width: 850px;
    }}
    </style>
    """
    st.markdown(css_kodlari, unsafe_allow_html=True)
    

# --- 2. UYGULAMA ---

# Önce arka planı yükle (Resim dosyanla aynı isim olmalı!)
try:
    arka_plan_yap('kabe.jpg')
except:
    st.warning("kabe.jpg dosyası bulunamadı, resimsiz devam ediliyor.")

st.title("🕋 Helal-Haram Sorgulama")

yasaklar = ["kötülük", "kumar", "alkol", "uyuşturucu", "hırsızlık", "yalan", "aldatma", "kıskançlık", "nefret", "şiddet"]
helaller = ["iyilik", "doğruluk", "adalet", "merhamet", "sevgi", "saygı", "yardımseverlik", "sabır", "hoşgörü", "dostluk"]

eylem = st.text_input("Sorgulamak istediğiniz eylemi girin:")

if eylem:
    eylem_temiz = eylem.lower().strip()
    st.markdown("---")
    if eylem_temiz in yasaklar:
        st.error(f"❌ {eylem.capitalize()} yasaktır.")
        emoji_yagmuru("❌")
    elif eylem_temiz in helaller:
        st.success(f"✅ {eylem.capitalize()} helaldir.")
        emoji_yagmuru("✅")
    else:
        st.info(f"❓ '{eylem}' hakkında bilgi bulunmamaktadır.")

