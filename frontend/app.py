import streamlit as st
import time
from typing import Dict, List
import base64


def load_custom_css():
    """Load custom CSS for modern styling"""
    st.markdown("""
    <style>
    /* Main app styling */
    .main {
        padding-top: 1rem;
    }
    
    /* Custom button styling */
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Title styling */
    .title-gradient {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 3rem;
        line-height: 1.6;
    }
    
    /* Section headers */
    .section-header {
        color: #424242;
        font-size: 1.5rem;
        font-weight: 600;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e1e8ed;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Persona cards */
    .persona-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #667eea;
    }
    
    .host-card {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        border-left: 4px solid #ff8a80;
    }
    
    .guest-card {
        background: linear-gradient(135deg, #e0c3fc 0%, #9bb5ff 100%);
        border-left: 4px solid #7c4dff;
    }
    
    /* Debate transcript styling */
    .debate-turn {
        background: #ffffff;
        padding: 1.5rem;
        margin: 0.75rem 0;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
        border-left: 4px solid #e3f2fd;
        transition: all 0.3s ease;
    }
    
    .debate-turn:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.12);
    }
    
    .speaker-name {
        font-weight: 600;
        color: #1976d2;
        margin-bottom: 0.75rem;
        font-size: 1.1rem;
    }
    
    .speaker-text {
        color: #333;
        line-height: 1.6;
        font-size: 1rem;
    }
    
    /* Input section styling */
    .input-section {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    }
    
    /* Audio player styling */
    .audio-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        text-align: center;
        color: white;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
    }
    
    /* Loading spinner */
    .loading-container {
        text-align: center;
        padding: 3rem;
        color: #667eea;
    }
    
    /* Form styling */
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e1e8ed;
        padding: 0.75rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
    }
    
    /* Custom containers */
    .config-container {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        margin: 1rem 0;
    }
    
    .host-container {
        background: linear-gradient(135deg, #fff5f5 0%, #fed7d7 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #fc8181;
        margin: 1rem 0;
    }
    
    .guest-container {
        background: linear-gradient(135deg, #f0fff4 0%, #c6f6d5 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #68d391;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)


def simulate_debate_generation(podcast_details: Dict) -> Dict:
    """
    Simulate the debate generation process.
    In a real implementation, this would call your OpenAI backend.
    """
    topic = podcast_details.get("topic", "a fascinating topic")
    host = podcast_details["host"]
    guests = podcast_details["guests"]
    
    # Simulate processing time
    time.sleep(2)
    
    # Generate mock response
    response = {
        "host": {
            "name": host["name"],
            "style": host["style"]
        },
        "guests": [
            {
                "name": guests[0]["name"],
                "stance": f"Advocates for {topic} from {guests[0]['company']} perspective with {guests[0]['characteristic']} approach",
                "company": guests[0]["company"] 
            },
            {
                "name": guests[1]["name"],
                "stance": f"Presents alternative viewpoint on {topic} from {guests[1]['company']} with {guests[1]['characteristic']} style",
                "company": guests[1]["company"]
            }
        ],
        "script": [
            {"speaker": "host", "text": f"Welcome everyone to today's debate on '{topic}'. I'm {host['name']}, and I'll be moderating this discussion with my {host['style'].lower()} approach."},
            {"speaker": "guest1", "text": f"Thank you for having me. I'm {guests[0]['name']} from {guests[0]['company']}. I believe {topic} represents a crucial turning point that requires careful consideration of all stakeholders involved."},
            {"speaker": "guest2", "text": f"I appreciate being here as well. I'm {guests[1]['name']} from {guests[1]['company']}. While I respect my colleague's perspective, I see {topic} as an opportunity for innovation and positive change."},
            {"speaker": "host", "text": f"{guests[0]['name']}, could you elaborate on why you think {topic} requires such careful consideration?"},
            {"speaker": "guest1", "text": f"Absolutely. When we examine {topic}, we must consider the long-term implications. The {guests[0]['characteristic']} approach I bring suggests we need robust frameworks and ethical guidelines before moving forward."},
            {"speaker": "host", "text": f"{guests[1]['name']}, how do you respond to those concerns about moving too quickly?"},
            {"speaker": "guest2", "text": f"I understand the caution, but I believe a {guests[1]['characteristic']} stance is what's needed here. {topic} offers unprecedented opportunities, and excessive hesitation could mean missing crucial windows for positive impact."},
            {"speaker": "host", "text": f"Both perspectives raise important points. {guests[0]['name']}, what would you say to those who argue that caution might lead to missed opportunities?"},
            {"speaker": "guest1", "text": f"That's a fair question. I'm not advocating for inaction, but rather for measured progress. We can pursue {topic} while simultaneously building the necessary safeguards and ethical frameworks."},
            {"speaker": "guest2", "text": f"And I'd argue that some of the best safeguards come from real-world implementation and learning. We can't anticipate every challenge from the sidelines."},
            {"speaker": "host", "text": f"This has been a fascinating discussion. Both {guests[0]['name']} and {guests[1]['name']} have provided valuable insights on {topic}. Thank you both for this enlightening debate."}
        ]
    }
    
    return response


def create_audio_player_html(has_audio: bool = False) -> str:
    """Create HTML for audio player"""
    if has_audio:
        return """
        <div class="audio-container">
            <h3>🎧 Generated Audio Podcast</h3>
            <p>Your AI-generated debate is ready to listen!</p>
            <audio controls style="width: 100%; margin-top: 1rem;">
                <source src="placeholder.mp3" type="audio/mpeg">
                Your browser does not support the audio element.
            </audio>
        </div>
        """
    else:
        return """
        <div class="audio-container">
            <h3>🎧 Audio Generation</h3>
            <p>Audio generation is not yet implemented, but the transcript is ready below!</p>
        </div>
        """


def main():
    """Main Streamlit application"""
    
    # Load custom CSS
    load_custom_css()
    
    # =====================================
    # HEADER SECTION
    # =====================================
    
    # Logo and title section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            st.image("static/logo.png", width=120, use_container_width=False)
        except:
            # Fallback emoji if logo doesn't exist
            st.markdown("<div style='text-align: center; font-size: 4rem; margin: 1rem 0;'>🎭</div>", unsafe_allow_html=True)
    
    # Main title with gradient
    st.markdown('<h1 class="title-gradient">AI Debate Generator</h1>', unsafe_allow_html=True)
    
    # Subtitle description
    st.markdown("""
    <p class="subtitle">
        Generate engaging AI-powered debates on any topic with customizable personas.<br>
        Create thoughtful discussions between expert hosts and knowledgeable guests.
    </p>
    """, unsafe_allow_html=True)
    
    # =====================================
    # INPUT CONFIGURATION SECTION
    # =====================================
    
    st.markdown('<div class="section-header">🎯 Design Your Perfect Debate</div>', unsafe_allow_html=True)
    
    # Topic selection with creative suggestions
    st.markdown("### 💡 What's sparking debate today?")
    
    # Predefined topic suggestions
    suggested_topics = [
        "The Impact of AI on Future Employment",
        "Should Social Media Platforms Regulate Free Speech?",
        "Universal Basic Income: Economic Revolution or Utopian Dream?",
        "Climate Change: Individual vs Corporate Responsibility",
        "The Future of Remote Work in a Post-Pandemic World",
        "Cryptocurrency: Digital Gold or Speculative Bubble?",
        "Gene Editing: Medical Miracle or Playing God?",
        "Space Colonization: Humanity's Next Chapter or Costly Fantasy?"
    ]
    
    col1, col2 = st.columns([3, 1])
    with col1:
        # Topic input with suggestions
        topic = st.text_input(
            "🔥 Enter your debate topic or choose from suggestions below:",
            value="The Impact of AI on Future Employment",
            help="What controversial or thought-provoking topic would you like to explore?"
        )
    
    with col2:
        if st.button("🎲 Surprise Me!", help="Get a random topic suggestion"):
            import random
            topic = random.choice(suggested_topics)
            st.rerun()
    
    # Topic suggestions as clickable pills
    st.markdown("**💭 Popular debate topics:**")
    cols = st.columns(4)
    for i, suggestion in enumerate(suggested_topics[:4]):
        with cols[i % 4]:
            if st.button(f"💡 {suggestion[:25]}{'...' if len(suggestion) > 25 else ''}", 
                        key=f"topic_{i}", 
                        help=suggestion,
                        use_container_width=True):
                topic = suggestion
                st.rerun()
    
    # Show remaining suggestions in expandable section
    with st.expander("🔍 See more topic suggestions"):
        cols = st.columns(2)
        for i, suggestion in enumerate(suggested_topics[4:]):
            with cols[i % 2]:
                if st.button(f"💡 {suggestion}", key=f"topic_extra_{i}", use_container_width=True):
                    topic = suggestion
                    st.rerun()
    
    # Perspective with visual indicators
    st.markdown("### 🕰️ Choose your debate lens")
    perspective_options = {
        "Historical": {"emoji": "📚", "desc": "Learn from the past - examine historical precedents and lessons"},
        "Modern": {"emoji": "🚀", "desc": "Focus on current trends and contemporary viewpoints"},
        "Mixed": {"emoji": "🔄", "desc": "Blend historical wisdom with modern insights"}
    }
    
    perspective = st.radio(
        "How would you like to frame this debate?",
        options=list(perspective_options.keys()),
        format_func=lambda x: f"{perspective_options[x]['emoji']} {x} - {perspective_options[x]['desc']}",
        index=1,
        help="This affects how your AI participants will approach the topic"
    )
    
    st.markdown("---")
    
    # Enhanced Host Configuration
    st.markdown("### 🎙️ Craft Your Ideal Moderator")
    st.markdown("*The host sets the tone and guides the conversation*")
    
    # Host persona presets
    host_presets = {
        "Academic Scholar": {
            "name": "Dr. Elena Martinez",
            "style": "Balanced academic moderator with expertise in facilitating constructive dialogue",
            "emoji": "🎓"
        },
        "Investigative Journalist": {
            "name": "Marcus Johnson",
            "style": "Sharp, probing journalist who asks tough questions and seeks truth",
            "emoji": "📰"
        },
        "Diplomatic Mediator": {
            "name": "Ambassador Chen Wei",
            "style": "Calm, neutral mediator focused on finding common ground and understanding",
            "emoji": "🤝"
        },
        "Tech Visionary": {
            "name": "Dr. Aria Singh",
            "style": "Forward-thinking tech expert who bridges complex concepts for broad audiences",
            "emoji": "💡"
        }
    }
    
    col1, col2 = st.columns([1, 2])
    with col1:
        selected_host = st.selectbox(
            "🎭 Choose a host archetype:",
            options=list(host_presets.keys()),
            help="Select a pre-designed host personality or customize your own"
        )
        
        if st.button("🎯 Use This Host", key="use_preset_host"):
            host_name = host_presets[selected_host]["name"]
            host_style = host_presets[selected_host]["style"]
    
    with col2:
        st.markdown(f"**{host_presets[selected_host]['emoji']} Preview:** {host_presets[selected_host]['name']}")
        st.markdown(f"*{host_presets[selected_host]['style']}*")
    
    # Custom host inputs
    col1, col2 = st.columns(2)
    with col1:
        host_name = st.text_input(
            "🎤 Host Name:",
            value=host_presets[selected_host]["name"],
            help="Give your moderator a memorable name"
        )
    with col2:
        host_style = st.text_input(
            "🧠 Moderation Style:",
            value=host_presets[selected_host]["style"],
            help="Describe how your host approaches debates and conversations"
        )
    
    st.markdown("---")
    
    # Enhanced Guest Configuration with Personality Builder
    st.markdown("### 👥 Build Your Dream Team of Debaters")
    st.markdown("*Create compelling characters with opposing viewpoints*")
    
    # Guest archetypes for inspiration
    guest_archetypes = {
        "The Optimist": {"char": "Enthusiastic and future-focused", "emoji": "🌟"},
        "The Skeptic": {"char": "Cautious and evidence-based", "emoji": "🔍"},
        "The Revolutionary": {"char": "Bold and change-oriented", "emoji": "⚡"},
        "The Traditionalist": {"char": "Values-driven and conservative", "emoji": "🏛️"},
        "The Pragmatist": {"char": "Practical and solution-focused", "emoji": "🛠️"},
        "The Idealist": {"char": "Principled and vision-driven", "emoji": "💫"}
    }
    
    col1, col2 = st.columns(2)
    
    # Guest 1 Configuration
    with col1:
        st.markdown("#### 🎭 **First Debater**")
        
        # Archetype selector for Guest 1
        g1_archetype = st.selectbox(
            "Choose personality type:",
            options=list(guest_archetypes.keys()),
            key="g1_archetype",
            format_func=lambda x: f"{guest_archetypes[x]['emoji']} {x}"
        )
        
        guest1_name = st.text_input(
            "👤 Name:", 
            value="Dr. Michael Thompson",
            key="g1_name",
            help="Give them a professional-sounding name"
        )
        
        guest1_company = st.text_input(
            "🏢 Organization:", 
            value="Future of Work Institute",
            key="g1_company",
            help="Where do they work or what do they represent?"
        )
        
        guest1_characteristic = st.text_input(
            "⚡ Personality:", 
            value=guest_archetypes[g1_archetype]["char"],
            key="g1_char",
            help="What makes their debating style unique?"
        )
        
        # Visual preview
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); 
                    padding: 1rem; border-radius: 10px; margin: 0.5rem 0;">
            <strong>{guest_archetypes[g1_archetype]['emoji']} {guest1_name}</strong><br>
            <small>{guest1_company} • {guest1_characteristic}</small>
        </div>
        """, unsafe_allow_html=True)
    
    # Guest 2 Configuration
    with col2:
        st.markdown("#### 🎭 **Second Debater**")
        
        # Archetype selector for Guest 2
        g2_archetype = st.selectbox(
            "Choose personality type:",
            options=list(guest_archetypes.keys()),
            key="g2_archetype",
            format_func=lambda x: f"{guest_archetypes[x]['emoji']} {x}",
            index=2  # Default to a different archetype
        )
        
        guest2_name = st.text_input(
            "👤 Name:", 
            value="Prof. Sarah Kim",
            key="g2_name",
            help="Give them a professional-sounding name"
        )
        
        guest2_company = st.text_input(
            "🏢 Organization:", 
            value="AI Innovation Labs",
            key="g2_company",
            help="Where do they work or what do they represent?"
        )
        
        guest2_characteristic = st.text_input(
            "⚡ Personality:", 
            value=guest_archetypes[g2_archetype]["char"],
            key="g2_char",
            help="What makes their debating style unique?"
        )
        
        # Visual preview
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%); 
                    padding: 1rem; border-radius: 10px; margin: 0.5rem 0;">
            <strong>{guest_archetypes[g2_archetype]['emoji']} {guest2_name}</strong><br>
            <small>{guest2_company} • {guest2_characteristic}</small>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick randomize button for guests
    if st.button("🎲 Randomize Both Debaters", help="Generate random but compelling debater profiles"):
        import random
        # This would trigger a rerun with randomized values
        st.info("🎭 Click again to see your new random debaters!")
    
    st.markdown("---")
    
    # Enhanced AI Options with visual appeal
    st.markdown("### 🤖 AI Enhancement Options")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        use_openai = st.checkbox(
            "🧠 **GPT-Powered Content**", 
            value=True,
            help="Use advanced AI for more nuanced and intelligent responses"
        )
        if use_openai:
            st.success("🚀 Enhanced intelligence enabled!")
    
    with col2:
        generate_audio = st.checkbox(
            "🎵 **Audio Podcast**", 
            value=False,
            help="Generate lifelike speech for your debate (experimental)"
        )
        if generate_audio:
            st.info("🎧 Audio generation selected!")
    
    with col3:
        advanced_mode = st.checkbox(
            "⚙️ **Advanced Mode**", 
            value=False,
            help="More detailed arguments and longer responses"
        )
        if advanced_mode:
            st.warning("🔧 Advanced mode activated!")
    
    # Fun debate length slider
    debate_length = st.slider(
        "🕰️ **Debate Duration**",
        min_value=3,
        max_value=15,
        value=8,
        help="Number of exchanges between participants (more = longer debate)"
    )
    
    col1, col2 = st.columns([1, 3])
    with col1:
        if debate_length <= 5:
            st.markdown("⚡ **Quick & Punchy**")
        elif debate_length <= 10:
            st.markdown("🎯 **Balanced Discussion**")
        else:
            st.markdown("📚 **Deep Dive Analysis**")
    
    with col2:
        st.markdown(f"*Your debate will have approximately {debate_length} rounds of discussion*")
    
    # Generate button with excitement
    st.markdown("---")
    st.markdown("### 🚀 Ready to Create Magic?")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        generate_button = st.button(
            "✨ Generate My Epic Debate ✨", 
            use_container_width=True,
            help="Click to bring your debate to life with AI magic!"
        )
        
        if generate_button:
            st.balloons()  # Celebration effect
    
    # Quick preview of what will be generated
    with st.expander("🔮 What you'll get"):
        st.markdown(f"""
        **Your debate will include:**
        - 🎙️ **Moderator**: {host_name} with {host_style.lower()}
        - 👥 **Participants**: {guest1_name} vs {guest2_name}
        - 💬 **Topic**: {topic}
        - 🕰️ **Rounds**: ~{debate_length} exchanges
        - 📱 **Format**: Professional transcript + participant cards
        {"- 🎧 **Audio**: Generated speech version" if generate_audio else ""}
        {"- 🧠 **Enhanced**: GPT-powered responses" if use_openai else ""}
        """)
    
    # Add some motivational text
    if not generate_button:
        st.markdown("""
        <div style="text-align: center; color: #666; font-style: italic; margin: 1rem 0;">
            🎭 Configure your perfect debate above, then hit the magic button!
        </div>
        """, unsafe_allow_html=True)
    
    # =====================================
    # DEBATE GENERATION AND OUTPUT
    # =====================================
    
    if generate_button:
        # Prepare podcast details with enhanced parameters
        podcast_details = {
            "topic": topic,
            "perspective": perspective,
            "debate_length": debate_length,
            "advanced_mode": advanced_mode,
            "host": {
                "name": host_name,
                "style": host_style
            },
            "guests": [
                {
                    "name": guest1_name,
                    "company": guest1_company,
                    "characteristic": guest1_characteristic,
                    "archetype": g1_archetype
                },
                {
                    "name": guest2_name,
                    "company": guest2_company,
                    "characteristic": guest2_characteristic,
                    "archetype": g2_archetype
                }
            ],
            "use_openai": use_openai,
            "generate_audio": generate_audio
        }
        
        # Show loading spinner
        with st.spinner("🚀 Generating your AI-powered debate... This may take a moment."):
            # Generate debate content
            debate_content = simulate_debate_generation(podcast_details)
            
            # Store in session state
            st.session_state.debate_content = debate_content
            st.session_state.podcast_details = podcast_details
            st.session_state.generated = True
    
    # =====================================
    # OUTPUT DISPLAY SECTION
    # =====================================
    
    if hasattr(st.session_state, 'generated') and st.session_state.generated:
        content = st.session_state.debate_content
        details = st.session_state.podcast_details
        
        st.markdown("---")
        
        # Audio player (if requested)
        if details.get("generate_audio", False):
            audio_html = create_audio_player_html(has_audio=False)  # Set to True when audio is implemented
            st.markdown(audio_html, unsafe_allow_html=True)
        
        # Participants section
        st.markdown('<div class="section-header">👥 Meet Your Debate Participants</div>', unsafe_allow_html=True)
        
        # Host card
        st.markdown(f'''
        <div class="persona-card host-card">
            <h3>🎙️ Moderator: {content["host"]["name"]}</h3>
            <p><strong>Moderation Style:</strong> {content["host"]["style"]}</p>
        </div>
        ''', unsafe_allow_html=True)
        
        # Guest cards
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f'''
            <div class="persona-card guest-card">
                <h3>🗣️ {content["guests"][0]["name"]}</h3>
                <p><strong>Company:</strong> {content["guests"][0]["company"]}</p>
                <p><strong>Stance:</strong> {content["guests"][0]["stance"]}</p>
            </div>
            ''', unsafe_allow_html=True)
        
        with col2:
            st.markdown(f'''
            <div class="persona-card guest-card">
                <h3>🗣️ {content["guests"][1]["name"]}</h3>
                <p><strong>Company:</strong> {content["guests"][1]["company"]}</p>
                <p><strong>Stance:</strong> {content["guests"][1]["stance"]}</p>
            </div>
            ''', unsafe_allow_html=True)
        
        # Debate transcript
        st.markdown('<div class="section-header">💬 Debate Transcript</div>', unsafe_allow_html=True)
        
        for turn in content['script']:
            # Determine speaker name
            if turn["speaker"] == "host":
                speaker_name = content["host"]["name"]
            elif turn["speaker"] == "guest1":
                speaker_name = content["guests"][0]["name"]
            else:
                speaker_name = content["guests"][1]["name"]
            
            # Display the turn
            st.markdown(f'''
            <div class="debate-turn">
                <div class="speaker-name">{speaker_name}:</div>
                <div class="speaker-text">{turn["text"]}</div>
            </div>
            ''', unsafe_allow_html=True)
        
        # Action buttons
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if st.button("🔄 Generate New Debate", use_container_width=True):
                # Clear session state
                if 'debate_content' in st.session_state:
                    del st.session_state.debate_content
                if 'podcast_details' in st.session_state:
                    del st.session_state.podcast_details
                if 'generated' in st.session_state:
                    del st.session_state.generated
                st.rerun()
        
        with col3:
            # Prepare transcript for download
            transcript_text = f"Debate Topic: {details['topic']}\n"
            transcript_text += f"Perspective: {details['perspective']}\n\n"
            transcript_text += "PARTICIPANTS:\n"
            transcript_text += f"Moderator: {content['host']['name']} ({content['host']['style']})\n"
            transcript_text += f"Guest 1: {content['guests'][0]['name']} from {content['guests'][0]['company']}\n"
            transcript_text += f"Guest 2: {content['guests'][1]['name']} from {content['guests'][1]['company']}\n\n"
            transcript_text += "TRANSCRIPT:\n\n"
            
            for turn in content["script"]:
                if turn["speaker"] == "host":
                    speaker = content["host"]["name"]
                elif turn["speaker"] == "guest1":
                    speaker = content["guests"][0]["name"]
                else:
                    speaker = content["guests"][1]["name"]
                transcript_text += f"{speaker}: {turn['text']}\n\n"
            
            st.download_button(
                "📁 Download Transcript",
                data=transcript_text,
                file_name=f"debate_transcript_{details['topic'].replace(' ', '_').lower()}.txt",
                mime="text/plain",
                use_container_width=True
            )


if __name__ == "__main__":
    main()