import streamlit as st
import google.generativeai as genai

# إعدادات الصفحة
st.set_page_config(
    page_title="AURYN | نظام الوقاية الاستباقية", 
    page_icon="🧬", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS صارم لإجبار Streamlit على التصميم
st.markdown("""
    <style>
    /* خلفية الموقع */
    .stApp {
        background-color: #050810;
        color: #ffffff !important;
    }
    
    /* تصميم البطاقات (Cards) بألوان مختلفة */
    .card-purple {
        background: linear-gradient(145deg, #1e1b4b 0%, #0f172a 100%);
        border: 2px solid #8b5cf6;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 5px 15px rgba(139, 92, 246, 0.2);
        height: 100%;
    }
    
    .card-blue {
        background: linear-gradient(145deg, #083344 0%, #0f172a 100%);
        border: 2px solid #06b6d4;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 5px 15px rgba(6, 182, 212, 0.2);
        height: 100%;
    }

    .card-green {
        background: linear-gradient(145deg, #064e3b 0%, #0f172a 100%);
        border: 2px solid #10b981;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 5px 15px rgba(16, 185, 129, 0.2);
        height: 100%;
    }

    /* العناوين داخل البطاقات */
    .card-title {
        text-align: center;
        color: #ffffff;
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 20px;
        border-bottom: 1px solid rgba(255,255,255,0.2);
        padding-bottom: 10px;
    }

    /* إجبار لون النص في كل مكان على الأبيض */
    .stMarkdown, p, label, .stRadio label, .stSlider label {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    /* 
      الزر المركزي الضخم
    */
    .stButton > button {
        width: 100% !important; /* يأخذ عرض العمود كامل */
        padding: 25px !important; /* ارتفاع الزر */
        background: linear-gradient(90deg, #ec4899, #8b5cf6, #3b82f6) !important;
        color: white !important;
        font-size: 2rem !important; /* حجم الخط ضخم */
        font-weight: 900 !important;
        border-radius: 50px !important;
        border: 2px solid rgba(255, 255, 255, 0.5) !important;
        transition: transform 0.3s ease !important;
    }
    .stButton > button:hover {
        transform: scale(1.02);
    }
    
    /* الشارات البيضاوية */
    .badges-container {
        display: flex;
        justify-content: center;
        gap: 15px;
        flex-wrap: wrap;
        margin-bottom: 40px;
        margin-top: 10px;
    }
    .badge {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid rgba(56, 189, 248, 0.4);
        padding: 10px 25px;
        border-radius: 50px;
        font-weight: bold;
        color: #e0f2fe;
    }
    </style>
""", unsafe_allow_html=True)

# الهيدر والشارات
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <h1 style="background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 3rem;">نظام أورين (AURYN) 🧬</h1>
    <p style="color: #94a3b8; font-size: 1.2rem; max-width: 800px; margin: 0 auto;">المنصة الطبية الأولى للوقاية الاستباقية. حلل مؤشراتك الحيوية، تنبأ بالخطر، واحمِ جهازك العصبي بترددات ذكية قبل حدوث النوبة.</p>
</div>
<div class="badges-container">
    <div class="badge">🚀 دقة تحليل عالية</div>
    <div class="badge">🧠 ذكاء اصطناعي فوري</div>
    <div class="badge">🎧 بروتوكول ترددات نشط</div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("### ⚙️ إعدادات المطور")
api_key = st.sidebar.text_input("مفتاح Gemini API:", type="password")

# البطاقات - استخدمنا حاويات (Containers) داخل الأعمدة لإجبار الألوان
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card-purple"><div class="card-title">🧠 المؤشرات العصبية</div>', unsafe_allow_html=True)
    # حيلة لإصلاح اتجاه السلايدر: نتركه بالانجليزي ونضع العنوان فوقه بالعربي
    st.write("مستوى التوتر الفسيولوجي (HRV)")
    stress = st.slider("Stress Level", 1, 10, 5, label_visibility="collapsed")
    st.write("ساعات النوم (الراحة العصبية)")
    sleep = st.slider("Sleep Hours", 0, 12, 7, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card-blue"><div class="card-title">💧 الحيوية والترطيب</div>', unsafe_allow_html=True)
    st.write("مستوى ترطيب الجسم")
    hydration = st.slider("Hydration Level", 1, 10, 8, label_visibility="collapsed")
    st.write("مستوى الطاقة العامة")
    vitality = st.slider("Vitality Level", 1, 10, 8, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card-green"><div class="card-title">☁️ العوامل البيئية</div>', unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    weather = st.radio("هل يوجد انخفاض مفاجئ في الضغط الجوي؟", ["لا", "نعم"])
    st.write("<br>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# حيلة لمركزة الزر وجعله ضخماً (وضعه داخل عمود وسطي كبير)
_, col_center, _ = st.columns([1, 4, 1]) # العمود الوسطي هو الأكبر

with col_center:
    if st.button("🚀 ابدأ التحليل واكتشف حالة جهازك العصبي", use_container_width=True):
        if not api_key:
            st.error("⚠️ يرجى فتح القائمة الجانبية وإدخال مفتاح API أولاً.")
        else:
            try:
                genai.configure(api_key=api_key)
                system_instruction = """
                أنت نظام أورين (AURYN) الطبي المتقدم. حلل خطر الإصابة بنوبة شقيقة بناءً على المدخلات.
                إذا كان هناك خطر (توتر عالي ونوم/ترطيب قليل)، اكتب في نهاية الرد: [ACTION]: TRIGGER_THERAPY
                اكتب تقريراً طبياً منسقاً واحترافياً.
                """
                model = genai.GenerativeModel('gemini-3.6-flash', system_instruction=system_instruction)
                prompt = f"التوتر: {stress}, النوم: {sleep}, الترطيب: {hydration}, الحيوية: {vitality}, طقس سيء: {weather}"
                
                with st.spinner('🔄 AURYN يقوم بتحليل البيانات...'):
                    response = model.generate_content(prompt)
                
                st.markdown("### 📋 النتيجة والتشخيص:")
                st.success(response.text)
                
                if "[ACTION]: TRIGGER_THERAPY" in response.text or stress >= 7 or sleep <= 4 or hydration <= 3:
                    st.error("🚨 تحذير: تم تفعيل بروتوكول الترددات الحيوية لمنع النوبة.")
                    
                    s_col1, s_col2, s_col3 = st.columns(3)
                    with s_col1:
                        st.markdown('<div style="text-align:center;"><h4>🎧 تردد Alpha</h4></div>', unsafe_allow_html=True)
                        st.audio("m.1.mp3")
                    with s_col2:
                        st.markdown('<div style="text-align:center;"><h4>🎧 تردد Theta</h4></div>', unsafe_allow_html=True)
                        st.audio("m.2.mp3")
                    with s_col3:
                        st.markdown('<div style="text-align:center;"><h4>🎧 مرحلة التثبيت</h4></div>', unsafe_allow_html=True)
                        st.audio("m.3.mp3")
                else:
                    st.info("✅ حالتك ممتازة.")
            except Exception as e:
                st.error(f"حدث خطأ: {e}")