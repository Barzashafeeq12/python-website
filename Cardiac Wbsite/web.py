import streamlit as st
st.set_page_config(page_title="Cardiac Health & Instruments | Pakistan", page_icon="❤️", layout="wide")

# Custom colorful background CSS
st.markdown("""
    <style>
    /* Colorful gradient background */
    body {
        background: linear-gradient(to right, #ff9a9e, #fad0c4, #fad0c4);
        background-attachment: fixed;
    }
    /* Make main container transparent */
    .stApp {
        background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
        background-size: cover;
        background-attachment: fixed;
    }
    /* Section Header style */
    .section-header {
        background: rgba(255, 255, 255, 0.7);
        padding: 10px;
        border-radius: 10px;
        font-weight: bold;
        font-size: 28px;
        color: #B80000;
        margin-top: 20px;
        text-align: center;
    }
    /* Different sections */
    .diagnostic-section {
        background: rgba(215, 236, 255, 0.8);
        padding: 10px;
        border-radius: 10px;
        font-size: 24px;
        color: #004080;
        margin-top: 20px;
        text-align: center;
    }
    .treatment-section {
        background: rgba(255, 250, 205, 0.8);
        padding: 10px;
        border-radius: 10px;
        font-size: 24px;
        color: #666600;
        margin-top: 20px;
        text-align: center;
    }
    .challenges-section {
        background: rgba(255, 218, 185, 0.8);
        padding: 10px;
        border-radius: 10px;
        font-size: 24px;
        color: #A0522D;
        margin-top: 20px;
    }
    .success-section {
        background: rgba(224, 187, 228, 0.8);
        padding: 10px;
        border-radius: 10px;
        font-size: 24px;
        color: #6A0DAD;
        margin-top: 20px;
    }
    /* Footer style */
    footer {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)

st.title("❤️ How to Solve Cardiac Problems and Instruments Needed in Hospitals of Pakistan")
st.markdown("""
---
🏥 **Welcome!**  
In this guide, we'll explore cardiac diseases, challenges in Pakistan, and the **essential medical instruments** hospitals need for better heart care.  
---
""")

# Introduction
st.markdown('<div class="section-header">🫀 What are Cardiac Problems?</div>', unsafe_allow_html=True)
st.write("""
 Cardiac problems refer to diseases or disorders related to the heart and the blood vessels.These 
problems can range from mild conditions to serious, life-threatening issues. They can affect the heart's 
structure, function, or rhythm and may lead to impaired blood flow to various organs and tissues in the body.
These can lead to serious health issues and death if not diagnosed and treated properly.  
***Common cardiac issues include:***
- ❤️ Heart Attacks (Myocardial Infarction)
- ⚡ Arrhythmias (irregular heart rhythms)
- 🫀 Heart Failure
- 🩸 Hypertension (High Blood Pressure)
- 🏥 Valvular Heart Diseases
- 🧬 Congenital Heart Defects

**In Pakistan**, cardiovascular disease (CVD) is responsible for 1 in every 4 deaths.
""")

st.markdown("---")


st.markdown('<div class="diagnostic-section">🔎 Instruments for Diagnosing Cardiac Problems</div>', unsafe_allow_html=True)
st.write("""
Modern hospitals require accurate diagnostic equipment to detect heart issues early and efficiently.
""")

st.subheader("🖥️ 1. Electrocardiogram (ECG/EKG)")
st.write("""
Records the heart’s electrical activity. Detects:
- Irregular rhythms
- Previous heart attacks
- Electrical conduction abnormalities
""")

st.subheader("🖥️ 2. Echocardiogram")
st.write("""
Ultrasound imaging that shows:
- Heart structure
- Valve functions
- Blood flow within the heart
""")

st.subheader("🩺 3. Stethoscope")
st.write("""
A basic but crucial tool used to:
- Listen to heart sounds
- Detect murmurs or valve abnormalities
""")

st.subheader("🧪 4. Angiography")
st.write("""
X-ray imaging to examine:
- Blockages in coronary arteries
- Aneurysms
- Vessel malformations
""")

st.subheader("📊 5. Cardiac Monitor (Telemetry)")
st.write("""
Continuously monitors:
- Heart rate
- Rhythm
- Blood pressure
- Oxygen saturation
""")

st.markdown("---")

st.markdown('<div class="treatment-section">🛠️ Life-saving Instruments for Cardiac Treatment</div>', unsafe_allow_html=True)
st.write("""
Once diagnosed, hospitals need immediate access to treatment tools.
""")

st.subheader("⚡ 1. Defibrillator (AED/Manual)")
st.write("""
- Delivers electric shocks to restore normal heartbeat
- Essential for treating sudden cardiac arrest
""")

st.subheader("🕰️ 2. Pacemaker")
st.write("""
- Small device implanted under the skin
- Controls abnormal heart rhythms
""")

st.subheader("🔪 3. Coronary Artery Bypass Grafting (CABG) Equipment")
st.write("""
- Surgical tools used to bypass blocked coronary arteries
- Requires heart-lung machines, surgical instruments, and anesthesia equipment
""")

st.subheader("💉 4. Thrombolytic Agents and Catheters")
st.write("""
- Medications and catheters used to dissolve blood clots
- Critical during heart attacks to restore blood flow
""")

st.subheader("🚑 5. Emergency Response Tools")
st.write("""
- Portable Oxygen Tanks
- Suction Machines
- Mobile Cardiac Monitors
""")

st.markdown("---")

st.markdown('<div class="challenges-section">🇵🇰 Challenges Facing Cardiac Care in Pakistan</div>', unsafe_allow_html=True)
st.write("""
Despite progress, many hospitals in Pakistan face challenges:
- 🏥 Limited Access to advanced cardiac facilities in rural areas
- 🧑‍⚕️ Shortage of Trained Cardiologists and Nurses
- 📉 Insufficient Funding for modern equipment
- 📢 Lack of Public Awareness about preventive heart care
- 🍔 Unhealthy Lifestyles: Smoking, obesity, lack of exercise
""")
st.markdown("---")

st.markdown('<div class="success-section">🏆 Success Stories: Progress in Pakistani Cardiac Health</div>', unsafe_allow_html=True)
st.write("""
- Major cities like Karachi, Lahore, and Islamabad now have internationally accredited cardiac centers.
- Initiatives like free cardiac camps and mobile heart clinics are expanding.
- Organizations are promoting heart health awareness through seminars and social media campaigns.
""")

st.markdown("---")

# Future Vision
st.markdown('<div class="section-header">🔮 Vision for the Future</div>', unsafe_allow_html=True)
st.write("""
To further improve cardiac care in Pakistan:
- Equipments every major district hospital with ECG and Defibrillator machines
- Increase specialized training programs for cardiac care
- Launch national heart health awareness campaigns
- Partner with international health organizations for funding and expertise
""")

st.markdown("---")

st.markdown("""
## 🩺 Take Charge of Your Heart Health Today!
> Visit a cardiologist regularly, eat healthy, stay active, and spread awareness about heart care!  
> **Together, we can save lives. ❤️**
""")

st.markdown("---")

st.markdown("""
---
<div style="text-align: center; padding-top: 20px;">
    <h4 style="color: #FF4B4B;">Made by <strong>Barza Shafeeq ur Rehman</strong></h4>
    <p style="color: grey ; center">Crafted with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)

