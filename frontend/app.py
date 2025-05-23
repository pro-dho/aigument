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
    
    host = podcast_details["host"]
    guests = podcast_details["guests"]
    topic = host["topic"]
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
            st.image("static/logo.png")
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
    
    st.markdown('<div class="section-header">⚙️ Configure Your Debate</div>', unsafe_allow_html=True)
    
    # Topic input with quick suggestions
    topic = st.text_input(
        "🎯 What topic should they debate?", 
        value="The Impact of AI on Future Employment",
        placeholder="Enter any topic you'd like to explore...",
        help="Choose something controversial or thought-provoking"
    )
    
    # Quick topic suggestions
    suggestions = [
        "Climate Change Solutions", "Future of Remote Work", "Universal Basic Income", 
        "Social Media Regulation", "Space Exploration Priorities", "Gene Editing Ethics"
    ]
    
    st.markdown("**💡 Popular topics:**")
    cols = st.columns(3)
    for i, suggestion in enumerate(suggestions):
        with cols[i % 3]:
            if st.button(suggestion, key=f"topic_{i}", use_container_width=True):
                topic = suggestion
                st.rerun()
    
    st.markdown("---")
    
    # Simple perspective choice
    perspective = st.radio(
        "🔍 **Debate Style:**",
        ["Modern", "Historical", "Mixed"],
        horizontal=True,
        help="How should they approach this topic?"
    )
    
    st.markdown("---")
    
    # Host Configuration - Simplified
    st.markdown("### 🎙️ Your Moderator")
    col1, col2 = st.columns(2)
    with col1:
        host_name = st.text_input("Name", value="Dr. Sarah Chen", placeholder="e.g., Dr. Sarah Chen")
    with col2:
        host_style = st.selectbox(
            "Style", 
            [
                "Balanced and professional",
                "Sharp and challenging", 
                "Calm and diplomatic",
                "Energetic and engaging"
            ]
        )
    
    st.markdown("---")
    
    # Guest Configuration - Simplified
    st.markdown("### 👥 Your Debaters")
    
    col1, col2 = st.columns(2)
    
    # Guest 1
    with col1:
        st.markdown("**Debater 1**")
        guest1_name = st.text_input("Name", value="Prof. Michael Chen", key="g1_name", placeholder="e.g., Prof. Michael Chen")
        guest1_company = st.text_input("Organization", value="Tech Research Institute", key="g1_company", placeholder="Where they work")
        guest1_type = st.selectbox("Personality", ["Analytical", "Optimistic", "Cautious", "Bold"], key="g1_type")
    
    # Guest 2  
    with col2:
        st.markdown("**Debater 2**")
        guest2_name = st.text_input("Name", value="Dr. Lisa Rodriguez", key="g2_name", placeholder="e.g., Dr. Lisa Rodriguez")
        guest2_company = st.text_input("Organization", value="Policy Think Tank", key="g2_company", placeholder="Where they work")
        guest2_type = st.selectbox("Personality", ["Passionate", "Practical", "Skeptical", "Visionary"], key="g2_type", index=1)
    
    st.markdown("---")
    
    # Simple options
    st.markdown("### 🤖 Options")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        use_openai = st.checkbox("🧠 Enhanced AI", value=True, help="Better, more nuanced responses")
    with col2:
        generate_audio = st.checkbox("🎵 Audio Version", help="Generate speech (experimental)")
    with col3:
        debate_length = st.selectbox("Length", ["Short", "Medium", "Long"], index=1)
    
    # Generate button - Simple and clean
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        generate_button = st.button("✨ Generate Debate", use_container_width=True, type="primary")
    
    # =====================================
    # DEBATE GENERATION AND OUTPUT
    # =====================================
    
    if generate_button:
        # Prepare podcast details
        podcast_details = {
            "host": {
                "name": host_name,
            "topic": topic,
            },
            "guests": [
                {
                    "name": guest1_name,
                    "company": guest1_company,
                    "characteristic": guest1_type
                },
                {
                    "name": guest2_name,
                    "company": guest2_company,
                    "characteristic": guest2_type
                }
            ]
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