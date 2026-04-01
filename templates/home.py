import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="🔥 FWI Prediction App",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ===================== CUSTOM CSS =====================
st.markdown("""
<style>
/* -------- ANIMATED GRADIENT BACKGROUND -------- */
.stApp {
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab, #f7971e, #ffd200);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}

@keyframes gradientBG {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* -------- FLOATING PARTICLES -------- */
.stApp::before {
    content: '';
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background:
        radial-gradient(circle at 20% 80%, rgba(255,255,255,0.08) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(255,255,255,0.08) 0%, transparent 50%),
        radial-gradient(circle at 40% 40%, rgba(255,255,255,0.05) 0%, transparent 40%),
        radial-gradient(circle at 60% 60%, rgba(255,255,255,0.05) 0%, transparent 40%);
    pointer-events: none;
    z-index: 0;
}

/* -------- 3D TITLE CARD -------- */
.title-3d {
    text-align: center;
    padding: 40px 20px;
    background: rgba(0, 0, 0, 0.35);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 25px;
    margin-bottom: 30px;
    box-shadow:
        0 20px 60px rgba(0,0,0,0.4),
        0 0 40px rgba(255,107,107,0.2),
        inset 0 1px 0 rgba(255,255,255,0.1);
    transform: perspective(1000px) rotateX(2deg);
    transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);
}
.title-3d:hover {
    transform: perspective(1000px) rotateX(0deg) translateY(-5px);
    box-shadow:
        0 30px 80px rgba(0,0,0,0.5),
        0 0 60px rgba(255,107,107,0.3),
        inset 0 1px 0 rgba(255,255,255,0.2);
}
.title-3d h1 {
    color: #fff;
    font-size: 3rem;
    text-shadow:
        0 0 20px rgba(255,107,107,0.8),
        0 0 40px rgba(255,107,107,0.4),
        0 4px 8px rgba(0,0,0,0.3);
    margin: 0;
    letter-spacing: 2px;
}
.title-3d p {
    color: rgba(255,255,255,0.85);
    font-size: 1.15rem;
    margin-top: 10px;
    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
}

/* -------- 3D METRIC ICON CARDS -------- */
.icon-card {
    background: rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 20px;
    padding: 20px 10px;
    text-align: center;
    box-shadow:
        0 15px 35px rgba(0,0,0,0.3),
        inset 0 1px 0 rgba(255,255,255,0.1);
    transform: perspective(800px) rotateY(0deg) translateZ(0);
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1);
}
.icon-card:hover {
    transform: perspective(800px) rotateY(5deg) translateZ(20px) translateY(-8px);
    box-shadow:
        0 25px 50px rgba(0,0,0,0.4),
        0 0 30px rgba(255,255,255,0.1),
        inset 0 1px 0 rgba(255,255,255,0.2);
}
.icon-card .emoji {
    font-size: 2.5rem;
    display: block;
    margin-bottom: 8px;
    filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
}
.icon-card .label {
    color: rgba(255,255,255,0.9);
    font-weight: 600;
    font-size: 0.95rem;
    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
}
.icon-card.temp  { border-bottom: 3px solid #ff6b6b; }
.icon-card.humid { border-bottom: 3px solid #48dbfb; }
.icon-card.wind  { border-bottom: 3px solid #feca57; }
.icon-card.rain  { border-bottom: 3px solid #54a0ff; }

/* -------- 3D FORM CARD -------- */
.form-3d {
    background: rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 25px;
    padding: 35px;
    margin: 20px 0;
    box-shadow:
        0 20px 60px rgba(0,0,0,0.35),
        0 0 0 1px rgba(255,255,255,0.05),
        inset 0 1px 0 rgba(255,255,255,0.1);
    transform: perspective(1200px) rotateX(1deg);
    transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);
}
.form-3d:hover {
    transform: perspective(1200px) rotateX(0deg) translateY(-3px);
    box-shadow:
        0 30px 80px rgba(0,0,0,0.45),
        0 0 0 1px rgba(255,255,255,0.08),
        inset 0 1px 0 rgba(255,255,255,0.15);
}
.form-3d h3 {
    color: #fff;
    text-shadow: 0 2px 8px rgba(0,0,0,0.3);
}

/* -------- INPUT FIELDS -------- */
.stNumberInput > div > div > input {
    background: rgba(255,255,255,0.08) !important;
    color: #fff !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 12px !important;
    padding: 12px !important;
    box-shadow:
        inset 0 2px 4px rgba(0,0,0,0.2),
        0 1px 0 rgba(255,255,255,0.05) !important;
    transition: all 0.3s ease !important;
}
.stNumberInput > div > div > input:focus {
    border-color: #ff6b6b !important;
    box-shadow:
        inset 0 2px 4px rgba(0,0,0,0.2),
        0 0 15px rgba(255,107,107,0.4),
        0 0 30px rgba(255,107,107,0.1) !important;
}

/* Select box */
.stSelectbox > div > div {
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 12px !important;
    box-shadow:
        inset 0 2px 4px rgba(0,0,0,0.2),
        0 1px 0 rgba(255,255,255,0.05) !important;
}
.stSelectbox > div > div > div {
    color: #fff !important;
}

/* Labels */
.stNumberInput label, .stSelectbox label {
    color: rgba(255,255,255,0.9) !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    text-shadow: 0 1px 3px rgba(0,0,0,0.3);
}

/* -------- 3D NEON BUTTON -------- */
.stFormSubmitButton > button {
    width: 100%;
    background: linear-gradient(135deg, #ff6b6b, #ee5a24, #f368e0, #ff6b6b) !important;
    background-size: 300% 300% !important;
    animation: btnGradient 4s ease infinite !important;
    color: white !important;
    border: none !important;
    border-radius: 15px !important;
    height: 4em !important;
    font-size: 1.2rem !important;
    font-weight: 800 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    box-shadow:
        0 10px 30px rgba(238,90,36,0.4),
        0 0 20px rgba(255,107,107,0.2),
        inset 0 1px 0 rgba(255,255,255,0.2) !important;
    transform: perspective(500px) translateZ(0);
    transition: all 0.3s cubic-bezier(0.23, 1, 0.32, 1) !important;
}
.stFormSubmitButton > button:hover {
    transform: perspective(500px) translateZ(10px) translateY(-3px) !important;
    box-shadow:
        0 20px 40px rgba(238,90,36,0.5),
        0 0 40px rgba(255,107,107,0.3),
        inset 0 1px 0 rgba(255,255,255,0.3) !important;
}
.stFormSubmitButton > button:active {
    transform: perspective(500px) translateZ(-5px) translateY(2px) !important;
}

@keyframes btnGradient {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* -------- 3D RESULT BOX -------- */
.result-3d {
    text-align: center;
    padding: 35px;
    background: rgba(0,0,0,0.35);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 25px;
    margin-top: 25px;
    box-shadow:
        0 20px 60px rgba(0,0,0,0.4),
        0 0 50px rgba(46,213,115,0.2),
        inset 0 1px 0 rgba(255,255,255,0.1);
    transform: perspective(1000px) rotateX(2deg);
    animation: resultPopIn 0.6s cubic-bezier(0.23, 1, 0.32, 1);
}
.result-3d:hover {
    transform: perspective(1000px) rotateX(0deg) translateY(-5px);
}
.result-3d h2 {
    color: #2ed573;
    font-size: 1.8rem;
    text-shadow:
        0 0 20px rgba(46,213,115,0.6),
        0 0 40px rgba(46,213,115,0.3);
    margin: 0 0 10px 0;
}
.result-3d .result-value {
    font-size: 3.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #2ed573, #7bed9f, #2ed573);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shineText 3s linear infinite;
}
.result-3d .result-sub {
    color: rgba(255,255,255,0.7);
    font-size: 1rem;
    margin-top: 5px;
}

@keyframes resultPopIn {
    0%   { opacity:0; transform: perspective(1000px) rotateX(15deg) translateY(40px) scale(0.9); }
    100% { opacity:1; transform: perspective(1000px) rotateX(2deg) translateY(0) scale(1); }
}
@keyframes shineText {
    0%   { background-position: 0% center; }
    100% { background-position: 200% center; }
}

/* -------- PROFESSIONAL SUCCESS BANNER -------- */
.success-banner {
    display: flex;
    align-items: center;
    gap: 15px;
    padding: 20px 25px;
    background: rgba(46, 213, 115, 0.12);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(46, 213, 115, 0.25);
    border-left: 4px solid #2ed573;
    border-radius: 15px;
    margin-top: 20px;
    box-shadow:
        0 10px 30px rgba(0, 0, 0, 0.2),
        0 0 20px rgba(46, 213, 115, 0.1);
    animation: bannerSlideIn 0.5s cubic-bezier(0.23, 1, 0.32, 1);
}
.success-banner .check-circle {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: linear-gradient(135deg, #2ed573, #7bed9f);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    box-shadow:
        0 4px 15px rgba(46, 213, 115, 0.4),
        0 0 20px rgba(46, 213, 115, 0.2);
    animation: pulseCheck 2s ease-in-out infinite;
}
.success-banner .check-circle svg {
    width: 28px;
    height: 28px;
}
.success-banner .banner-text h4 {
    color: #2ed573;
    margin: 0;
    font-size: 1.1rem;
    text-shadow: 0 0 10px rgba(46, 213, 115, 0.3);
}
.success-banner .banner-text p {
    color: rgba(255,255,255,0.7);
    margin: 4px 0 0 0;
    font-size: 0.9rem;
}

@keyframes pulseCheck {
    0%, 100% { transform: scale(1); box-shadow: 0 4px 15px rgba(46,213,115,0.4); }
    50%      { transform: scale(1.08); box-shadow: 0 6px 25px rgba(46,213,115,0.6); }
}
@keyframes bannerSlideIn {
    0%   { opacity: 0; transform: translateX(-30px); }
    100% { opacity: 1; transform: translateX(0); }
}

/* -------- STATUS TIMELINE -------- */
.status-timeline {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0;
    margin: 25px 0 10px 0;
    animation: timelineFadeIn 0.8s ease;
}
.status-step {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
}
.status-dot {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    font-weight: 700;
    z-index: 2;
}
.status-dot.completed {
    background: linear-gradient(135deg, #2ed573, #7bed9f);
    color: #fff;
    box-shadow: 0 0 15px rgba(46, 213, 115, 0.5);
}
.status-label {
    color: rgba(255,255,255,0.75);
    font-size: 0.75rem;
    margin-top: 8px;
    text-align: center;
    white-space: nowrap;
}
.status-line {
    width: 80px;
    height: 3px;
    background: linear-gradient(90deg, #2ed573, #7bed9f);
    margin: 0 -1px;
    margin-bottom: 22px;
    box-shadow: 0 0 8px rgba(46, 213, 115, 0.3);
    border-radius: 2px;
}

@keyframes timelineFadeIn {
    0%   { opacity: 0; transform: translateY(15px); }
    100% { opacity: 1; transform: translateY(0); }
}

/* -------- RISK BADGE -------- */
.risk-badge {
    display: inline-block;
    padding: 6px 18px;
    border-radius: 30px;
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-top: 10px;
    animation: badgePop 0.4s cubic-bezier(0.23, 1, 0.32, 1);
}
.risk-low {
    background: rgba(46, 213, 115, 0.2);
    color: #2ed573;
    border: 1px solid rgba(46, 213, 115, 0.4);
    box-shadow: 0 0 15px rgba(46, 213, 115, 0.2);
}
.risk-moderate {
    background: rgba(254, 202, 87, 0.2);
    color: #feca57;
    border: 1px solid rgba(254, 202, 87, 0.4);
    box-shadow: 0 0 15px rgba(254, 202, 87, 0.2);
}
.risk-high {
    background: rgba(255, 107, 107, 0.2);
    color: #ff6b6b;
    border: 1px solid rgba(255, 107, 107, 0.4);
    box-shadow: 0 0 15px rgba(255, 107, 107, 0.2);
}
.risk-extreme {
    background: rgba(238, 90, 36, 0.2);
    color: #ee5a24;
    border: 1px solid rgba(238, 90, 36, 0.4);
    box-shadow: 0 0 15px rgba(238, 90, 36, 0.3);
    animation: badgePop 0.4s cubic-bezier(0.23,1,0.32,1), extremePulse 1.5s ease-in-out infinite;
}

@keyframes badgePop {
    0%   { transform: scale(0.5); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
}
@keyframes extremePulse {
    0%, 100% { box-shadow: 0 0 15px rgba(238,90,36,0.3); }
    50%      { box-shadow: 0 0 30px rgba(238,90,36,0.6); }
}

/* -------- SUMMARY CARDS -------- */
.summary-card {
    background: rgba(0,0,0,0.3);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 15px;
    padding: 15px;
    text-align: center;
    box-shadow:
        0 10px 30px rgba(0,0,0,0.25),
        inset 0 1px 0 rgba(255,255,255,0.08);
    transform: perspective(600px) rotateX(2deg);
    transition: all 0.3s ease;
    margin-bottom: 10px;
}
.summary-card:hover {
    transform: perspective(600px) rotateX(0deg) translateY(-5px) scale(1.02);
    box-shadow: 0 15px 40px rgba(0,0,0,0.35);
}
.summary-card .s-emoji { font-size: 1.5rem; }
.summary-card .s-value {
    color: #fff;
    font-size: 1.3rem;
    font-weight: 700;
    margin: 5px 0;
    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
}
.summary-card .s-label {
    color: rgba(255,255,255,0.6);
    font-size: 0.8rem;
}

/* -------- NEON DIVIDER -------- */
.neon-divider {
    border: 0;
    height: 2px;
    background: linear-gradient(to right,
        transparent,
        rgba(255,107,107,0.6),
        rgba(243,104,224,0.6),
        rgba(72,219,251,0.6),
        transparent);
    margin: 25px 0;
    box-shadow: 0 0 10px rgba(243,104,224,0.3);
}

/* -------- SECTION HEADER -------- */
.section-header {
    color: #fff;
    font-size: 1.5rem;
    font-weight: 700;
    text-shadow: 0 2px 8px rgba(0,0,0,0.3);
    margin: 15px 0 10px 0;
}

/* -------- SIDEBAR -------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0c0c1d, #1a1a3e, #2d1b69) !important;
    border-right: 1px solid rgba(255,255,255,0.05);
}
section[data-testid="stSidebar"] .stMarkdown h2 {
    color: #ff6b6b !important;
    text-shadow: 0 0 15px rgba(255,107,107,0.5);
}
section[data-testid="stSidebar"] .stMarkdown p,
section[data-testid="stSidebar"] .stMarkdown li {
    color: #c0c0c0 !important;
}

.sidebar-box {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 15px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.2);
}
.sidebar-box h3 {
    color: #f368e0 !important;
    text-shadow: 0 0 10px rgba(243,104,224,0.4);
    margin-top: 0;
}
.sidebar-box p, .sidebar-box li {
    color: rgba(255,255,255,0.75) !important;
    font-size: 0.9rem;
}

/* -------- STREAMLIT METRICS OVERRIDE -------- */
[data-testid="stMetricValue"] {
    color: #fff !important;
    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
}
[data-testid="stMetricLabel"] {
    color: rgba(255,255,255,0.7) !important;
}

/* -------- HIDE DEFAULT STREAMLIT -------- */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# ===================== HELPER: RISK LEVEL =====================
def get_risk_level(fwi):
    if fwi < 5:
        return "Low", "risk-low", "🟢"
    elif fwi < 15:
        return "Moderate", "risk-moderate", "🟡"
    elif fwi < 30:
        return "High", "risk-high", "🔴"
    else:
        return "Extreme", "risk-extreme", "🔥"


# ===================== SIDEBAR =====================
with st.sidebar:
    st.markdown("""
    <div class="sidebar-box">
        <h3>🔥 About FWI</h3>
        <p>The <strong>Fire Weather Index</strong> system is a globally 
        recognized weather-based system used to estimate wildfire danger.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-box">
        <h3>📊 Parameters</h3>
        <ul>
            <li>🌡️ <strong>Temperature</strong> – Noon temp (°C)</li>
            <li>💧 <strong>RH</strong> – Relative Humidity (%)</li>
            <li>🌬️ <strong>Ws</strong> – Wind Speed (km/h)</li>
            <li>🌧️ <strong>Rain</strong> – 24h rainfall (mm)</li>
            <li>📊 <strong>FFMC</strong> – Fine Fuel Moisture Code</li>
            <li>📊 <strong>DMC</strong> – Duff Moisture Code</li>
            <li>📊 <strong>ISI</strong> – Initial Spread Index</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-box">
        <h3>🛠️ Tech Stack</h3>
        <p>🐍 Python &nbsp;|&nbsp; 🎈 Streamlit &nbsp;|&nbsp; 🤖 Scikit-Learn</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-box">
        <h3>⚠️ Risk Levels</h3>
        <ul>
            <li>🟢 <strong>Low</strong> – FWI &lt; 5</li>
            <li>🟡 <strong>Moderate</strong> – FWI 5–15</li>
            <li>🔴 <strong>High</strong> – FWI 15–30</li>
            <li>🔥 <strong>Extreme</strong> – FWI &gt; 30</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center; margin-top:20px;">
        <p style="color:rgba(255,255,255,0.4); font-size:0.85rem;">
            Made with ❤️ &amp; 🔥
        </p>
    </div>
    """, unsafe_allow_html=True)


# ===================== TITLE =====================
st.markdown("""
<div class="title-3d">
    <h1>🔥 FWI Prediction</h1>
    <p>Enter weather parameters to predict the Fire Weather Index</p>
</div>
""", unsafe_allow_html=True)


# ===================== METRIC ICON CARDS =====================
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown("""
    <div class="icon-card temp">
        <span class="emoji">🌡️</span>
        <span class="label">Temperature</span>
    </div>
    """, unsafe_allow_html=True)
with m2:
    st.markdown("""
    <div class="icon-card humid">
        <span class="emoji">💧</span>
        <span class="label">Humidity</span>
    </div>
    """, unsafe_allow_html=True)
with m3:
    st.markdown("""
    <div class="icon-card wind">
        <span class="emoji">🌬️</span>
        <span class="label">Wind</span>
    </div>
    """, unsafe_allow_html=True)
with m4:
    st.markdown("""
    <div class="icon-card rain">
        <span class="emoji">🌧️</span>
        <span class="label">Rain</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<hr class="neon-divider">', unsafe_allow_html=True)


# ===================== FORM =====================
st.markdown('<div class="form-3d">', unsafe_allow_html=True)
st.markdown('<p class="section-header">📋 Input Parameters</p>', unsafe_allow_html=True)

with st.form("fwi_form"):
    col1, col2 = st.columns(2)

    with col1:
        temp  = st.number_input("🌡️ Temperature (°C)",  min_value=-50.0, max_value=60.0,  value=25.0, step=0.1)
        rh    = st.number_input("💧 RH (%)",             min_value=0.0,   max_value=100.0, value=50.0, step=0.1)
        ws    = st.number_input("🌬️ Wind Speed (km/h)",  min_value=0.0,   max_value=200.0, value=10.0, step=0.1)
        rain  = st.number_input("🌧️ Rain (mm)",          min_value=0.0,   max_value=500.0, value=0.0,  step=0.1)
        ffmc  = st.number_input("📊 FFMC",               min_value=0.0,   max_value=200.0, value=85.0, step=0.1)

    with col2:
        dmc     = st.number_input("📊 DMC",              min_value=0.0,   max_value=500.0, value=25.0, step=0.1)
        isi     = st.number_input("📊 ISI",              min_value=0.0,   max_value=100.0, value=5.0,  step=0.1)
        classes = st.selectbox("🏷️ Classes", ["Fire 🔥", "Not Fire ✅"])
        region  = st.selectbox("📍 Region",  [0, 1])

    st.markdown('<hr class="neon-divider">', unsafe_allow_html=True)
    submit_button = st.form_submit_button(label="🔮  PREDICT FWI")

st.markdown('</div>', unsafe_allow_html=True)


# ===================== PREDICTION =====================
if submit_button:

    # ---- Progress Bar ----
    progress_placeholder = st.empty()
    status_text = st.empty()

    progress_bar = progress_placeholder.progress(0)
    steps = [
        (20, "📥 Collecting input data..."),
        (45, "⚙️ Preprocessing features..."),
        (70, "🤖 Running ML model..."),
        (90, "📊 Generating results..."),
        (100, "✅ Prediction complete!"),
    ]
    for pct, msg in steps:
        status_text.markdown(
            f"<p style='color:rgba(255,255,255,0.8); font-size:0.95rem; "
            f"text-shadow:0 1px 3px rgba(0,0,0,0.4);'>{msg}</p>",
            unsafe_allow_html=True,
        )
        progress_bar.progress(pct)
        time.sleep(0.5)

    progress_placeholder.empty()
    status_text.empty()

    # ---------- YOUR MODEL CODE HERE ----------
    # classes_enc = 1 if classes == "Fire 🔥" else 0
    # result = model.predict([[temp, rh, ws, rain, ffmc, dmc, isi, classes_enc, region]])[0]
    result = 15.42  # Placeholder
    # -------------------------------------------

    risk_label, risk_class, risk_icon = get_risk_level(result)

    # ---- Status Timeline ----
    st.markdown(f"""
    <div class="status-timeline">
        <div class="status-step">
            <div class="status-dot completed">📥</div>
            <div class="status-label">Input</div>
        </div>
        <div class="status-line"></div>
        <div class="status-step">
            <div class="status-dot completed">⚙️</div>
            <div class="status-label">Process</div>
        </div>
        <div class="status-line"></div>
        <div class="status-step">
            <div class="status-dot completed">🤖</div>
            <div class="status-label">Model</div>
        </div>
        <div class="status-line"></div>
        <div class="status-step">
            <div class="status-dot completed">✅</div>
            <div class="status-label">Result</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---- Result Card ----
    st.markdown(f"""
    <div class="result-3d">
        <h2>✅ FWI Prediction Result</h2>
        <div class="result-value">{result}</div>
        <p class="result-sub">Based on the provided weather parameters</p>
        <div style="margin-top:15px;">
            <span class="risk-badge {risk_class}">{risk_icon} {risk_label} Risk</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---- Professional Success Banner ----
    st.markdown(f"""
    <div class="success-banner">
        <div class="check-circle">
            <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3"
                 stroke-linecap="round" stroke-linejoin="round">
                <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
        </div>
        <div class="banner-text">
            <h4>Prediction Completed Successfully</h4>
            <p>Model executed in 2.5s · Confidence: High · Risk Level: {risk_label}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="neon-divider">', unsafe_allow_html=True)
    st.markdown('<p class="section-header">📊 Input Summary</p>', unsafe_allow_html=True)

    # ---- Summary Cards ----
    data = [
        ("🌡️", f"{temp} °C",  "Temperature"),
        ("💧", f"{rh} %",      "Humidity"),
        ("🌬️", f"{ws} km/h",   "Wind Speed"),
        ("🌧️", f"{rain} mm",   "Rain"),
        ("📊", f"{ffmc}",      "FFMC"),
        ("📊", f"{dmc}",       "DMC"),
        ("📊", f"{isi}",       "ISI"),
        ("🏷️", f"{classes}",   "Class"),
        ("📍", f"{region}",    "Region"),
    ]

    for row_start in range(0, len(data), 3):
        cols = st.columns(3)
        for idx, col in enumerate(cols):
            if row_start + idx < len(data):
                emoji, val, lbl = data[row_start + idx]
                col.markdown(f"""
                <div class="summary-card">
                    <div class="s-emoji">{emoji}</div>
                    <div class="s-value">{val}</div>
                    <div class="s-label">{lbl}</div>
                </div>
                """, unsafe_allow_html=True)