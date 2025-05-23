import streamlit as st

# -------------------- MOCK DEBATE LOGIC --------------------

def generate_topic():
    return "Should AI be open-sourced?"

def generate_personas(topic, guest_type):
    return (
        {"name": "Ada", "style": "neutral, thoughtful"},
        {"name": "Elon Musk", "stance": "Pro open-source AI"},
        {"name": "Timnit Gebru", "stance": "Skeptical of open-source AI without safeguards"}
    )

def generate_debate_script(topic, host, guest1, guest2):
    return [
        {"speaker": host["name"], "text": f"Welcome to AIGUMENT. Today’s debate: {topic}"},
        {"speaker": guest1["name"], "text": "AI should be open — knowledge belongs to humanity."},
        {"speaker": guest2["name"], "text": "Without controls, open AI causes real harm."},
        {"speaker": host["name"], "text": "Let’s dig into those positions..."},
    ]

# -------------------- STREAMLIT UI --------------------

st.set_page_config(page_title="AIGUMENT", page_icon="🎙️", layout="wide")

st.markdown("""
<style>
    .aigument-title {
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 0;
    }
    .aigument-subtitle {
        font-size: 18px;
        color: #666;
        margin-bottom: 20px;
    }
    .speaker-label {
        font-weight: bold;
        color: #4f8bf9;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="aigument-title">🎙️ AIGUMENT</p>', unsafe_allow_html=True)
st.markdown('<p class="aigument-subtitle">Where historical and modern minds collide in AI-generated debates.</p>', unsafe_allow_html=True)

# Step 1: Topic Input
st.subheader("🧠 Step 1: Choose Your Topic")
topic = st.text_input("Enter a debate topic:", placeholder="e.g. Should AI be open-sourced?")

col1, col2 = st.columns([1, 2])
with col1:
    if st.button("🎲 Generate Random Topic"):
        topic = generate_topic()
with col2:
    if topic:
        st.success(f"Topic selected: *{topic}*")

if not topic:
    st.stop()

# Step 2: Guest Type
st.subheader("👥 Step 2: Select Participants")
guest_type = st.radio("Who should join the debate?", ["Historical", "Modern", "Mixed"], index=0)

# Step 3: Generate Debate
if st.button("🔮 Generate Debate"):
    with st.spinner("Generating personas and simulating the debate..."):
        host, guest1, guest2 = generate_personas(topic, guest_type)
        script = generate_debate_script(topic, host, guest1, guest2)

    # Display Participants
    st.markdown("---")
    st.subheader("🎭 Debate Participants")

    st.markdown(f"<span class='speaker-label'>Host:</span> {host['name']} — *{host['style']}*", unsafe_allow_html=True)
    st.markdown(f"<span class='speaker-label'>Guest 1:</span> {guest1['name']} — *{guest1['stance']}*", unsafe_allow_html=True)
    st.markdown(f"<span class='speaker-label'>Guest 2:</span> {guest2['name']} — *{guest2['stance']}*", unsafe_allow_html=True)

    # Display Transcript
    st.markdown("---")
    st.subheader("🗣️ Debate Transcript")

    for entry in script:
        st.markdown(f"<span class='speaker-label'>{entry['speaker']}:</span> {entry['text']}", unsafe_allow_html=True)

    st.markdown("---")
    st.success("Debate generated successfully!")
