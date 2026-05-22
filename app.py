import streamlit as st
import pandas as pd
import pickle

# ── Page Setup ──────────────────────────────
st.set_page_config(page_title="YouTube Revenue Predictor", page_icon="🎬")

# ── Styling ──────────────────────────────────
st.markdown("""
    <style>
    /* 1. Background color of the whole app */
    .stApp {
        background-color: #fdf4ff;
    }

    /* 2. Title text color */
    h1, h2, h3 {
        color: #9333ea;
    }

    /* 3. Regular text color */
    p, label {
        color: #9333ea;
    }

    /* 4. predict button */
    .stButton > button {
        color: white;
        border-radius: 10px;
        font-size: 18px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# ── Load Model ───────────────────────────────
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('model_columns.pkl', 'rb') as f:
    model_columns = pickle.load(f)

# ── Title ────────────────────────────────────
st.title("🎬 YouTube Ad Revenue Predictor")
st.write("Fill in your video details and we'll predict how much ad revenue it can earn!")
st.divider()

# ── Input Fields ─────────────────────────────
st.header("📊 Video Performance")

# Two side by side columns
col1, col2 = st.columns(2)

with col1:
    views        = st.number_input("👁️ Views",                  min_value=0,   value=10000)
    likes        = st.number_input("👍 Likes",                  min_value=0,   value=1000)
    comments     = st.number_input("💬 Comments",               min_value=0,   value=250)

with col2:
    watch_time   = st.number_input("⏱️ Watch Time (minutes)",   min_value=0.0, value=37000.0)
    video_length = st.number_input("🎥 Video Length (minutes)", min_value=0.0, value=10.0)
    subscribers  = st.number_input("👥 Subscribers",            min_value=0,   value=500000)

st.divider()
st.header("🎯 Video Details")

col3, col4, col5 = st.columns(3)

with col3:
    category = st.selectbox("📁 Category",
        ['Education', 'Entertainment', 'Gaming', 'Lifestyle', 'Music', 'Tech'])
with col4:
    device = st.selectbox("📱 Device",
        ['Desktop', 'Mobile', 'TV', 'Tablet'])
with col5:
    country = st.selectbox("🌍 Country",
        ['AU', 'CA', 'DE', 'IN', 'UK', 'US'])

st.divider()

# ── Predict Button ───────────────────────────
if st.button("🔮 Predict Ad Revenue"):

    # Calculate engagement rate
    engagement_rate = (likes + comments) / views if views > 0 else 0

    # Build input dictionary
    input_data = {
        'views'               : views,
        'likes'               : likes,
        'comments'            : comments,
        'watch_time_minutes'  : watch_time,
        'video_length_minutes': video_length,
        'subscribers'         : subscribers,
        'engagement_rate'     : engagement_rate
    }

    # One-hot encode category, device, country
    for col in model_columns:
        if col.startswith('category_'):
            input_data[col] = 1 if col == f'category_{category}' else 0
        elif col.startswith('device_'):
            input_data[col] = 1 if col == f'device_{device}' else 0
        elif col.startswith('country_'):
            input_data[col] = 1 if col == f'country_{country}' else 0

    # Create dataframe and predict
    input_df   = pd.DataFrame([input_data])[model_columns]
    prediction = model.predict(input_df)[0]

    # Show results
    st.success(f"💰 Predicted Ad Revenue: ${prediction:.2f}")
    st.divider()

