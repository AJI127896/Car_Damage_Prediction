import streamlit as st
from model_helper import predict
import time

from warnings import filterwarnings

filterwarnings("ignore")
# Page Config
st.set_page_config(
    page_title="Vehicle Damage Detection",
    page_icon="🚗",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown(
    """
    <style>
        .stFileUploader div { 
            border-radius: 10px; 
            padding: 10px;
        }
        .stButton>button {
            border-radius: 8px;
            background-color: #4CAF50;
            color: white;
            padding: 8px 16px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stInfo {
            font-weight: bold;
            font-size: 18px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.title("🚘 Vehicle Damage Detection")
st.write("Upload an image, and our AI model will predict whether car is damaged or not.")

# File Upload
uploaded_file = st.file_uploader("📤 Upload an image (JPG/PNG)", type=["jpg", "png"])

if uploaded_file:
    # Display Uploaded Image
    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(uploaded_file, caption="📸 Uploaded Image", use_container_width =True)

    # Add some spacing
    st.markdown("<br>", unsafe_allow_html=True)

    # Predict Button
    if st.button("🔍 Detect Damage"):
        with st.spinner("Analyzing image... 🔄"):
            time.sleep(1)  # Simulating processing time
            prediction = predict(image_path)

        # Display Prediction
        st.info(f"Prediction: {prediction}")

# Footer
st.markdown("<br><hr><center>🚀 Built with ❤️ in Streamlit</center>", unsafe_allow_html=True)

