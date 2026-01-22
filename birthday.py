import streamlit as st
import time
import os
import base64

# --- IMPORT FOR RAIN ANIMATION ---
try:
    from streamlit_extras.let_it_rain import rain
except ImportError:
    st.error("Please run: pip install streamlit-extras in your terminal first!")
    st.stop()

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Happy Birthday Ayesha!",
    page_icon="❤️",
    layout="wide"
)

# --- HELPER FUNCTION: CONVERT IMAGE TO BASE64 ---
# This is necessary to show local images inside HTML flip cards
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# --- SESSION STATE ---
if 'kisses' not in st.session_state:
    st.session_state['kisses'] = 0
if 'letter_open' not in st.session_state:
    st.session_state['letter_open'] = False
if 'batman_active' not in st.session_state:
    st.session_state['batman_active'] = False

# --- CUSTOM CSS (FLIP CARD MAGIC) ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;600&family=Playfair+Display:ital@0;1&display=swap');

        /* Background */
        .stApp { background: linear-gradient(to bottom right, #fff0f3, #ffe6eb); }

        /* Headings */
        h1 { font-family: 'Dancing Script', cursive; color: #ff4d6d; font-size: 3.5rem !important; text-align: center; }
        
        /* Button Style */
        .stButton button {
            background-color: #ff4d6d; color: white; border-radius: 30px;
            font-size: 18px; padding: 10px 20px; border: none; width: 100%;
            box-shadow: 0 5px 15px rgba(255, 77, 109, 0.3); transition: 0.3s;
        }
        .stButton button:hover { background-color: #ff758f; transform: scale(1.05); }
        
        /* --- FLIP CARD CSS --- */
        .flip-card {
            background-color: transparent;
            width: 100%;
            height: 300px; /* Adjust height of cards */
            perspective: 1000px;
            margin-bottom: 20px;
        }
        
        .flip-card-inner {
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            transition: transform 0.8s;
            transform-style: preserve-3d;
            border-radius: 15px;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        }
        
        /* The Flip Action (Hover for PC, Tap for Mobile) */
        .flip-card:hover .flip-card-inner {
            transform: rotateY(180deg);
        }
        
        .flip-card-front, .flip-card-back {
            position: absolute;
            width: 100%;
            height: 100%;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            border-radius: 15px;
        }
        
        .flip-card-front img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 15px;
        }
        
        .flip-card-back {
            background-color: #ffcad4; /* Pink back color */
            color: #590d22;
            transform: rotateY(180deg);
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            font-family: 'Playfair Display', serif;
            font-size: 1.1rem;
            line-height: 1.5;
            font-style: italic;
        }
        
        /* Timeline */
        .timeline-container { border-left: 4px solid #ff4d6d; padding-left: 20px; margin-left: 20px; }
        .timeline-item { position: relative; margin-bottom: 30px; background: white; padding: 15px; border-radius: 15px; }
        .timeline-year { font-weight: bold; color: #ff4d6d; font-size: 1.2rem; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.markdown("## ❤️ **Menu**")
page = st.sidebar.radio("Navigate:", ["🏠 Home", "📸 Our Memories", "💋 Send Kisses", "💌 The Sealed Letter"])
st.sidebar.markdown("---")
st.sidebar.markdown("### 🎵 **Our Song**")

if os.path.exists("song.mp3"):
    st.sidebar.audio(open("song.mp3", "rb").read(), format='audio/mp3')
else:
    st.sidebar.warning("Add 'song.mp3' to folder!")

# ================= PAGE 1: HOME =================
if page == "🏠 Home":
    rain(emoji="❤️", font_size=40, falling_speed=5, animation_length=3)
    st.title("Happy Birthday Meri Jaan! 🎂")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if os.path.exists("pic6.jpg"):
            st.image("pic6.jpg", caption="My Everything 👑")
        else:
            st.warning("Please add 'pic1.jpeg' to your folder.")
            
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: white; border-radius: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
            <h3>To the love of my life...</h3>
            <p>I built this entire app just for you. Every button, every photo, and every line of code is a piece of my heart iloveyou my jaanu baby.</p>
            <p><strong>👈 Use the menu to explore your gift!</strong></p>
        </div>
        """, unsafe_allow_html=True)

# ================= PAGE 2: MEMORIES (NOW WITH FLIP CARDS) =================
elif page == "📸 Our Memories":
    st.header("✨ The Story of Us ✨")
    st.info("💡 Tip: Hover over (or tap) the photos to read the story behind them!")
    
    tab1, tab2 = st.tabs(["📸 Gallery", "⏳ Our Journey"])
    
    with tab1:
        # --- DEFINE YOUR MEMORIES HERE ---
        # Modify the text below to match your real photos!
        memories = [
            {
                "img": "Pic1.jpeg", 
                "text": "I remember on these days we would hear each other's heartbeat and my heart beats so fast when I am with you, I just can't explain this feeling."
            },
            {
                "img": "pic7.jpg", 
                "text": "I kissed you for the first time on this day, it holds a very special place in my heart, seeing you wear my hoodie makes my heart bloom so much."
            },
            {
                "img": "Pic3.jpeg", 
                "text": "Our espresso date here you got me those gifts and I don't even have words to tell you how happy it made me, I am still over the moon."
            },
            {
                "img": "Pic4.jpeg", 
                "text": "Our first date after getting back together even though the brick sandwich was very eww but costa will always have a special place in my heart jaanu."
            }
        ]
        
        # Grid Layout
        col1, col2 = st.columns(2)
        
        # Loop through memories and create flip cards
        for index, memory in enumerate(memories):
            if os.path.exists(memory["img"]):
                # Convert image to Base64 so HTML can see it
                img_b64 = get_img_as_base64(memory["img"])
                
                # HTML Block for Flip Card
                card_html = f"""
                <div class="flip-card">
                  <div class="flip-card-inner">
                    <div class="flip-card-front">
                      <img src="data:image/jpeg;base64,{img_b64}" alt="Memory">
                    </div>
                    <div class="flip-card-back">
                      <p>{memory["text"]}</p>
                    </div>
                  </div>
                </div>
                """
                
                # Alternate columns
                if index % 2 == 0:
                    with col1:
                        st.markdown(card_html, unsafe_allow_html=True)
                else:
                    with col2:
                        st.markdown(card_html, unsafe_allow_html=True)
            else:
                st.warning(f"Missing {memory['img']}")

    with tab2:
        st.write("")
        timeline_data = [
            {"year": "2018", "title": "First Met", "desc": "First time I saw you, I was like she's really cute, didn't know you will be my everything."},
            {"year": "2020", "title": "Fell in love", "desc": "I knew you were the one, I fell in love with the prettiest girl in the world."},
            {"year": "2022", "title": "She Said Yes!", "desc": "We started dating, happiest days of my life."},
            {"year": "Today", "title": "Happy Birthday", "desc": "Celebrating the prettiest girl in the world."}
        ]
        html_code = '<div class="timeline-container">'
        for item in timeline_data:
            html_code += f"""
            <div class="timeline-item">
                <div class="timeline-year">{item['year']}</div>
                <strong>{item['title']}</strong><br>{item['desc']}
            </div>"""
        html_code += "</div>"
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2: st.markdown(html_code, unsafe_allow_html=True)

# ================= PAGE 3: KISSES (BATMAN JPEG & KITTY) =================
elif page == "💋 Send Kisses":
    st.header("💋 Kisses for Ayesha")
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 20px;">
        <h1 style="font-size: 60px !important; margin: 0;">{st.session_state['kisses']}</h1>
        <p>Kisses Collected</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3, 2, 3])
    with col2:
        if st.button("😘 Catch a Kiss!"):
            st.session_state['kisses'] += 1
            st.session_state['batman_active'] = True
            rain(emoji="💋", font_size=50, falling_speed=3, animation_length=2)
    
    if st.session_state['batman_active']:
        st.write("")
        st.write("")
        anim_col1, anim_col2 = st.columns([1, 1])
        
        with anim_col1:
            if os.path.exists("batman.jpeg"):
                st.markdown('<div style="display:flex; justify-content:flex-end;">', unsafe_allow_html=True)
                st.image("batman.jpeg", width=220) 
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("Please add 'batman.jpeg'")

        with anim_col2:
            if os.path.exists("kitty.jpeg"):
                st.markdown('<div style="display:flex; justify-content:flex-start;">', unsafe_allow_html=True)
                st.image("kitty.jpeg", width=200)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("Please add 'kitty.gif'")

# ================= PAGE 4: THE LETTER =================
elif page == "💌 The Sealed Letter":
    st.header("💌 A Message from My Heart")
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if not st.session_state['letter_open']:
            if os.path.exists("kitty_waiting.gif"):
                st.image("kitty_waiting.gif", width=250)
            else:
                st.info("Waiting for kitty_waiting.gif...")
            st.write("")
            if st.button("🔓 Break the Seal"):
                st.session_state['letter_open'] = True
                st.rerun()
        else:
            st.markdown("""
            <div style="background-color: white; padding: 40px; border-radius: 10px; border: 2px dashed #ff4d6d; box-shadow: 0 10px 25px rgba(0,0,0,0.1);">
                <h3 style="color: #ff4d6d; font-family: 'Dancing Script'; text-align: center;">My Dearest Jaanu,</h3>
                <br>
                <div style="font-family: 'Playfair Display', serif; color: #590d22; font-size: 1.3rem; line-height: 1.8; text-align: justify;">
                Happy Birthday to my jaanu maanu baby you have made me the happiest person alive.
                <br><br>
                Every day I fall more and more in love you mean the world to me, I am so so so so happy that we got back together and I love you more than anything else for making me the happiest person in this world I would give my whole world just to be wrapped around in your arms meri jaan.
                <br><br>
                I promise to always be your side and I promise you to love you more and more forever please please never leave me meri jaan.
                <br><br>
                Here is to another year of us, of memories, and of love.
                </div>
                <br>
                <h3 style="text-align: right; font-family: 'Dancing Script'; color: #ff4d6d;">Forever yours,<br>Umar</h3>
            </div>
            """, unsafe_allow_html=True)
            
            st.write("")
            if st.button("🎁 Where is my gift?"):
                rain(emoji="❤️", font_size=40, falling_speed=4, animation_length=5)
                st.success("Just wait till your birthday party! ❤️")
                time.sleep(5)
                if st.button("Seal it back"):
                    st.session_state['letter_open'] = False
                    st.rerun()
