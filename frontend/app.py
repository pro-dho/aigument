import streamlit as st
import random
import time

# Custom CSS for modern styling
def load_css():
    st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    
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
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
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
        height: 120px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .debate-turn {
        background: #ffffff;
        padding: 1rem 1.5rem;
        margin: 0.5rem 0;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        border-left: 3px solid #e3f2fd;
    }
    
    .speaker-name {
        font-weight: 600;
        color: #1976d2;
        margin-bottom: 0.5rem;
    }
    
    .title-gradient {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .section-header {
        color: #424242;
        font-size: 1.5rem;
        font-weight: 600;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e1e8ed;
    }
    </style>
    """, unsafe_allow_html=True)

# Mock backend function to generate debate content
def generate_debate_content(topic, perspective):
    """
    Mock function that simulates API call to generate debate personas and script
    """
    
    # Mock host personas
    hosts = [
        {"name": "Dr. Sarah Chen", "style": "Academic moderator with expertise in balanced discourse"},
        {"name": "Marcus Williams", "style": "Professional journalist known for incisive questioning"},
        {"name": "Prof. Elena Rodriguez", "style": "Philosophy professor who encourages deep thinking"}
    ]
    
    # Mock guest templates based on perspective
    guest_templates = {
        "Historical": [
            {"name": "Dr. James Historical", "stance": f"Traditional historical perspective on {topic}"},
            {"name": "Prof. Mary Conservative", "stance": f"Classical interpretation of {topic}"}
        ],
        "Modern": [
            {"name": "Alex Progressive", "stance": f"Contemporary progressive view on {topic}"},
            {"name": "Jordan Innovation", "stance": f"Tech-forward approach to {topic}"}
        ],
        "Mixed": [
            {"name": "Dr. Emma Traditionalist", "stance": f"Time-tested principles regarding {topic}"},
            {"name": "Sam Modernist", "stance": f"Innovative solutions for {topic}"}
        ]
    }
    
    # Generate debate script templates
    script_templates = {
        "Historical": [
            f"Welcome everyone. Today we're discussing {topic} from various perspectives.",
            f"Dr. Historical, let's start with the traditional viewpoint. How has {topic} been approached historically?",
            f"Well, historically speaking, {topic} has always been grounded in established principles that have stood the test of time. We shouldn't rush to abandon what has worked for generations.",
            f"Prof. Conservative, do you agree with that assessment?",
            f"Absolutely. The wisdom of the past provides us with a solid foundation. When it comes to {topic}, we must respect the lessons learned by those who came before us.",
            f"Thank you both. This gives us a solid foundation for understanding the traditional perspective on {topic}."
        ],
        "Modern": [
            f"Welcome to today's discussion on {topic}. We're exploring cutting-edge perspectives.",
            f"Alex, you advocate for a progressive approach. What's your take on {topic}?",
            f"Thanks for having me. I believe {topic} requires us to embrace change and innovation. The old ways simply aren't sufficient for today's challenges.",
            f"Jordan, you focus on technological solutions. How does innovation factor into {topic}?",
            f"Technology is revolutionizing everything, including {topic}. We need to leverage data, AI, and modern tools to create better outcomes than ever before.",
            f"Fascinating perspectives. It's clear that modern approaches to {topic} prioritize innovation and adaptability."
        ],
        "Mixed": [
            f"Today we're examining {topic} through both traditional and modern lenses.",
            f"Dr. Traditionalist, let's hear the case for established approaches to {topic}.",
            f"Traditional methods have proven their worth over time. With {topic}, we need stability and proven strategies rather than untested experiments.",
            f"Sam, you disagree. What's the modern counter-argument?",
            f"While tradition has value, we can't ignore new evidence and better methods. {topic} demands that we evolve and improve upon past approaches.",
            f"This tension between tradition and innovation is exactly what makes {topic} such a compelling subject for debate."
        ]
    }
    
    # Select random personas and appropriate script
    host = random.choice(hosts)
    guests = guest_templates[perspective]
    script = script_templates[perspective]
    
    return {
        "host": host,
        "guests": guests,
        "script": script
    }

def main():
    # Load custom CSS
    load_css()
    
    # App title with logo and gradient
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            st.image("static/logo.png", width=150, use_container_width=False)
        except:
            # Fallback if logo doesn't exist
            st.markdown("🎭")
    
    st.markdown('<h1 class="title-gradient">AI Debate Generator</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #666; font-size: 1.1rem; margin-bottom: 3rem;">Generate engaging debates on any topic with AI-powered personas</p>', unsafe_allow_html=True)
    
    # Input section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        topic = st.text_input(
            "🎯 Enter your debate topic:",
            placeholder="e.g., Artificial Intelligence in Education, Climate Change Solutions...",
            help="Choose any topic you'd like to explore through debate"
        )
    
    with col2:
        perspective = st.radio(
            "🔍 Choose perspective:",
            ["Historical", "Modern", "Mixed"],
            help="Select the type of viewpoints for your debate"
        )
    
    # Generate button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        generate_clicked = st.button("✨ Generate Debate", use_container_width=True)
    
    # Generate and display content
    if generate_clicked and topic:
        with st.spinner("🤖 Generating your custom debate..."):
            time.sleep(1.5)  # Simulate API call delay
            
            try:
                content = generate_debate_content(topic, perspective)
                
                # Store in session state to persist
                st.session_state.debate_content = content
                st.session_state.topic = topic
                st.session_state.perspective = perspective
                
            except Exception as e:
                st.error(f"Error generating content: {str(e)}")
                return
    
    # Display generated content if available
    if hasattr(st.session_state, 'debate_content'):
        content = st.session_state.debate_content
        
        st.markdown('<div class="section-header">👥 Meet Your Debate Participants</div>', unsafe_allow_html=True)
        
        # Display host
        st.markdown(f'''
        <div class="persona-card host-card">
            <h3>🎙️ Moderator: {content["host"]["name"]}</h3>
            <p><strong>Style:</strong> {content["host"]["style"]}</p>
        </div>
        ''', unsafe_allow_html=True)
        
        # Display guests
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f'''
            <div class="persona-card guest-card">
                <h3>🗣️ Guest 1: {content["guests"][0]["name"]}</h3>
                <p><strong>Stance:</strong> {content["guests"][0]["stance"]}</p>
            </div>
            ''', unsafe_allow_html=True)
        
        with col2:
            st.markdown(f'''
            <div class="persona-card guest-card">
                <h3>🗣️ Guest 2: {content["guests"][1]["name"]}</h3>
                <p><strong>Stance:</strong> {content["guests"][1]["stance"]}</p>
            </div>
            ''', unsafe_allow_html=True)
        
        # Display debate script
        st.markdown('<div class="section-header">💬 Debate Transcript</div>', unsafe_allow_html=True)
        
        speakers = [content["host"]["name"]] + [guest["name"] for guest in content["guests"]]
        
        for i, turn in enumerate(content["script"]):
            if i == 0:
                speaker = content["host"]["name"]
            elif i % 2 == 1:
                speaker = content["host"]["name"]
            else:
                # Alternate between guests for responses
                speaker = speakers[1 + ((i-2) // 2) % 2]
            
            st.markdown(f'''
            <div class="debate-turn">
                <div class="speaker-name">{speaker}:</div>
                <p>{turn}</p>
            </div>
            ''', unsafe_allow_html=True)
        
        # Action buttons
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("🔄 Generate New Debate", use_container_width=True):
                if hasattr(st.session_state, 'debate_content'):
                    del st.session_state.debate_content
                st.rerun()
        
        with col3:
            st.download_button(
                label="📁 Download Transcript",
                data=f"Debate Topic: {st.session_state.topic}\nPerspective: {st.session_state.perspective}\n\n" +
                     f"Moderator: {content['host']['name']}\nStyle: {content['host']['style']}\n\n" +
                     "\n".join([f"{speakers[i%len(speakers)]}: {turn}" for i, turn in enumerate(content['script'])]),
                file_name=f"debate_{st.session_state.topic.lower().replace(' ', '_')}.txt",
                mime="text/plain"
            )
    
    elif generate_clicked and not topic:
        st.warning("⚠️ Please enter a topic to generate a debate!")
    
    # Footer
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center; color: #999; font-size: 0.9rem;">Built with Streamlit • Generate unlimited debates on any topic</p>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()