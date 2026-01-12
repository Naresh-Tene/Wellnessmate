import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="WellnessMate",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    /* Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Noto+Sans+Telugu:wght@400;600&display=swap');
    html, body, * { font-family: 'Inter', system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; }
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #f8fbff 0%, #f3f8ff 60%, #ffffff 100%);
    }
    /* Centered readable width */
    .block-container {max-width: 1180px; padding-top: 1rem;}
    .main-header {
        text-align: center;
        padding: 2.5rem 0;
        background: linear-gradient(135deg, #eaf5ff 0%, #e3f1ff 100%);
        color: #0b1324;
        border-radius: 14px;
        margin-bottom: 2rem;
        box-shadow: 0 6px 16px rgba(31, 41, 55, 0.08);
        border: 1px solid #dbeafe;
        position: relative;
        overflow: hidden;
    }
    .main-header::after{
        content: "";
        position: absolute;
        right: -140px;
        top: -100px;
        width: 520px; height: 520px;
        background: radial-gradient(circle at 40% 40%, #93c5fd 0%, #60a5fa 42%, #3b82f6 70%, #1e40af 100%);
        border-radius: 50%;
        filter: blur(10px);
        opacity: .22;
    }
    .main-header::before{
        content: "";
        position: absolute;
        right: 160px; bottom: -140px;
        width: 260px; height: 260px;
        background: radial-gradient(circle at 50% 50%, #bfdbfe 0%, #93c5fd 70%);
        border-radius: 50%;
        opacity: .35;
    }
    
    .section-header {
        color: #0b1a3a;
        padding-bottom: 0.6rem;
        margin-top: 2rem;
        border-bottom: 0;
        position: relative;
    }
    .section-header::after{
        content: "";
        position:absolute; left:0; bottom:0;
        width: 140px; height: 6px; border-radius: 999px;
        background: linear-gradient(90deg, #60a5fa 0%, #3b82f6 60%, #1e40af 100%);
        box-shadow: 0 2px 10px rgba(59,130,246,.35);
    }
    
    .about-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 16px;
        border: 1px solid #e6ecff;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        margin: 1rem 0;
        /* removed blue side line */
    }
    .about-card:hover{ box-shadow: 0 10px 24px rgba(30,58,138,.12); transform: translateY(-2px); transition: all .22s ease; }
    .about-card h3 { margin-top: 0; font-size: 1.5rem; }
    
    .telugu-text {
        font-family: 'Noto Sans Telugu', 'Inter', sans-serif;
        color: #2c3e50;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    
    .disclaimer {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 8px;
        padding: 1rem;
        margin-top: 3rem;
        font-size: 0.9rem;
        color: #856404;
    }
    
    .chatbot-placeholder {
        background: linear-gradient(135deg, #eff6ff 0%, #e0f2fe 100%);
        color: #1e3a8a;
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        margin: 2rem 0;
        border: 1px solid #bfdbfe;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
        color: #0b1324;
        border: none;
        border-radius: 28px;
        padding: 0.6rem 1.4rem;
        font-weight: 600;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    /* Friendly check-list styling */
    .check-list { list-style: none; padding-left: 0; }
    .check-list li { position: relative; padding-left: 1.6rem; margin: 0.4rem 0; }
    .check-list li::before {
        content: "✓";
        position: absolute; left: 0; top: 0; color: #2563eb; font-weight: 700;
        background: #eff6ff; border-radius: 999px; width: 1.2rem; height: 1.2rem; display: inline-flex; align-items: center; justify-content: center; font-size: 0.8rem;
    }
    .tip-card { 
        background: linear-gradient(#ffffff, #ffffff) padding-box,
                    linear-gradient(135deg, #60a5fa, #3b82f6) border-box;
        border: 2px solid transparent; border-radius:16px; padding:1rem; 
        box-shadow:0 6px 14px rgba(2,6,23,0.06);
    }
    .tip-card h4 { margin-top:0; color:#0b1a3a; }
    .tip-card:hover{ transform: translateY(-3px); box-shadow:0 12px 24px rgba(2,6,23,0.10); transition: all .22s ease; }
    .muted { color:#6b7280; }

    /* AI Widget container polish */
    .ai-container { background:#ffffff; border:1px solid #e5edff; border-radius:16px; padding: 0.25rem; box-shadow:0 4px 12px rgba(0,0,0,0.06);}    

    /* Friendly footer message */
    .footer-cta { 
        background: #eef4ff; border:1px solid #dbeafe; border-radius:14px; 
        padding: 1rem 1.25rem; margin: 1.25rem 0 0; text-align:center;
    }
    .footer-cta .headline { color:#0b1a3a; font-weight:800; }
    .footer-cta .sub { color:#1e3a8a; opacity:.9; }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown("""
<div class="main-header">
    <h1 style="font-weight:800; letter-spacing:0.3px;">🏥 WellnessMate</h1>
    <p class="muted" style="font-size: 1.1rem; margin: 0;">Health and wellness guidance</p>
</div>
""", unsafe_allow_html=True)

# About Section
st.markdown('<h2 class="section-header">About WellnessMate</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="about-card">
        <h3>In English</h3>
        <p><strong>WellnessMate</strong> is your comprehensive bilingual health companion designed to provide 
        accessible health and wellness guidance. Our platform offers:</p>
        <ul class="check-list">
            <li>Basic health tips and wellness advice</li>
            <li>Nutrition and lifestyle recommendations</li>
            <li>Exercise and fitness guidance</li>
            <li>Mental health and stress management tips</li>
            <li>General health information and resources</li>
        </ul>
        <p><em>Please note: This application provides general health information only and should not 
        replace professional medical advice.</em></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="about-card">
        <h3>IN తెలుగు</h3>
        <p class="telugu-text"><strong>వెల్నెస్ మేట్</strong> అనేది మీ సమగ్ర ద్విభాషా ఆరోగ్య సహచరుడు, 
        అందుబాటులో ఉన్న ఆరోగ్య మరియు వెల్నెస్ మార్గదర్శకత్వాన్ని అందించడానికి రూపొందించబడింది. 
        మా ప్లాట్‌ఫారమ్ అందిస్తుంది:</p>
        <ul class="telugu-text">
            <li>ప్రాథమిక ఆరోగ్య చిట్కాలు మరియు వెల్నెస్ సలహాలు</li>
            <li>పోషకాహారం మరియు జీవనశైలి సిఫార్సులు</li>
            <li>వ్యాయామం మరియు ఫిట్‌నెస్ మార్గదర్శకత్వం</li>
            <li>మానసిక ఆరోగ్యం మరియు ఒత్తిడి నిర్వహణ చిట్కాలు</li>
            <li>సాధారణ ఆరోగ్య సమాచారం మరియు వనరులు</li>
        </ul>
        <p class="telugu-text"><em>దయచేసి గమనించండి: ఈ అప్లికేషన్ సాధారణ ఆరోగ్య సమాచారాన్ని మాత్రమే అందిస్తుంది 
        మరియు వృత్తిపరమైన వైద్య సలహాను భర్తీ చేయకూడదు.</em></p>
    </div>
    """, unsafe_allow_html=True)

# AI Health Assistant (Dify embed only)
st.markdown('<h2 class="section-header">🤖 AI Health Assistant</h2>', unsafe_allow_html=True)

try:
    dify_embed_code = """
    <div id="dify-chatbot" style="height: 600px; border: 1px solid #ddd; border-radius: 10px; overflow: hidden;">
        <iframe 
            src="https://udify.app/chat/IFFauWVSHpSpwgku"
            width="100%" 
            height="100%" 
            frameborder="0"
            style="border-radius: 10px;">
        </iframe>
    </div>
    """
    components.html(dify_embed_code, height=600)
except Exception as e:
    st.error(f"Chatbot widget could not be loaded: {str(e)}")

# Quick Health Tips Section
st.markdown('<h2 class="section-header">Quick Health Tips</h2>', unsafe_allow_html=True)

tips_col1, tips_col2, tips_col3 = st.columns(3)

with tips_col1:
    st.markdown("""
    <div class="tip-card">
        <h4>Nutrition</h4>
        <ul class="check-list">
            <li>Drink 8 glasses of water daily</li>
            <li>Eat 5 servings of fruits/vegetables</li>
            <li>Limit processed foods</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tips_col2:
    st.markdown("""
    <div class="tip-card">
        <h4>Exercise</h4>
        <ul class="check-list">
            <li>30 minutes daily activity</li>
            <li>Take regular breaks</li>
            <li>Stretch every hour</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tips_col3:
    st.markdown("""
    <div class="tip-card">
        <h4>Wellness</h4>
        <ul class="check-list">
            <li>Get 7–9 hours sleep</li>
            <li>Practice mindfulness</li>
            <li>Connect with others</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Friendly footer sentence
st.markdown("""
<div class="footer-cta">
  <div class="headline">“Type your illness/health problem in Telugu or English – I’ll guide you with care.”</div>
  <div class="sub">I am not a doctor. This is only basic guidance, your Health Friend.</div>
  
</div>
""", unsafe_allow_html=True)

# Footer removed per request

# Sidebar for additional features
with st.sidebar:
    st.markdown("### 🎯 Quick Navigation")
    st.markdown("""
    - [About](#about-wellnessmate)
    - [Health Tips](#quick-health-tips)
    - [AI Assistant](#ai-health-assistant)
    """)
    
    st.markdown("### 📞 Emergency Resources")
    st.markdown("""
    **Emergency:** 911 (US) / 108 (India)
    
    **Mental Health:**
    - National Suicide Prevention: 988
    - Crisis Text Line: Text HOME to 741741
    """)
    
    st.markdown("### 🔗 Useful Links")
    st.markdown("""
    - [CDC Health Tips](https://www.cdc.gov)
    - [WHO Health Advice](https://www.who.int)
    - [Mental Health Resources](https://www.mentalhealth.gov)
    """)

