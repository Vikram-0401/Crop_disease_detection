import streamlit as st
import tensorflow as tf
import numpy as np
import google.generativeai as genai
import os
from PIL import Image
import sqlite3
from datetime import datetime

# Import configuration
try:
    from config import GOOGLE_API_KEY
except ImportError:
    # Fallback to environment variable if config file is not available
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "AIzaSyC9ofeMhsLxxB6pw6bENBZUPlveLY_osz0")

# Configure Google Generative AI
genai.configure(api_key=GOOGLE_API_KEY)
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

model2 = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config={
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    },
    system_instruction="You are a helpful personal assistant chatbot",
)

chat = model2.start_chat()

def chat_with_me(question):
    try:
        response = chat.send_message(question)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_plant_disease_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions)  # return index of max element

# Database setup
def init_db():
    conn = sqlite3.connect('disease_history.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY,
            image_path TEXT,
            prediction TEXT,
            timestamp TEXT
        )''')
    conn.commit()
    conn.close()

def insert_record(image_path, prediction):
    conn = sqlite3.connect('disease_history.db')
    c = conn.cursor()
    c.execute('''INSERT INTO history (image_path, prediction, timestamp)
                 VALUES (?, ?, ?)''', (image_path, prediction, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def fetch_records():
    conn = sqlite3.connect('disease_history.db')
    c = conn.cursor()
    c.execute('SELECT * FROM history ORDER BY timestamp DESC')
    records = c.fetchall()
    conn.close()
    return records

# Initialize the database
init_db()

background_image_url = "https://th.bing.com/th/id/OIP.LAOaWuloBHvVV7ZQRBwcowHaE7?rs=1&pid=ImgDetMain"

# Streamlit UI Setup
st.markdown(f"""
    <style>
    .main {{
        background-image: url('{background_image_url}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }}
    </style>
    """, unsafe_allow_html=True)

# Sidebar content above "Connect with Us"
st.sidebar.title("Dashboard")

app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Recognition", "Chat Support", "History"])

# Spacer to push "Connect with Us" to the bottom
st.sidebar.markdown("<br>" * 14, unsafe_allow_html=True)

# "Connect with Us" at the bottom inside the sidebar
st.sidebar.markdown("""
<div style="position: relative; bottom: 0; width: 100%; text-align: center;">
    <h4>Connect with Us</h4>
    <a href="https://github.com/Vikram-0401/Crop_disease_detection" target="_blank">
        <img src="https://img.icons8.com/material-outlined/24/ffffff/github.png" style="vertical-align: middle;"/>
    </a>
    <a href="https://www.linkedin.com/in/your-linkedin-profile/" target="_blank">
        <img src="https://img.icons8.com/material-outlined/24/ffffff/linkedin.png" style="vertical-align: middle;"/>
    </a>
    <a href="https://www.instagram.com/your-instagram-profile/" target="_blank">
        <img src="https://img.icons8.com/material-outlined/24/ffffff/instagram-new.png" style="vertical-align: middle;"/>
    </a>
</div>
""", unsafe_allow_html=True)

# Home Page
if app_mode == "Home":
    st.title("🌱 Plant Disease Detection System")
    st.markdown("""
    Welcome to our advanced Plant Disease Detection System! 
    
    This AI-powered application helps farmers and researchers identify plant diseases quickly and accurately.
    
    ### 🚀 Key Features:
    - **Instant Disease Detection**: Upload a plant image and get results in seconds
    - **AI-Powered Analysis**: Uses state-of-the-art machine learning models
    - **Comprehensive Database**: Covers 38 different plant disease classes
    - **Smart Chat Support**: Get expert advice through our AI chatbot
    
    ### 📱 How to Use:
    1. Go to **Disease Recognition** page
    2. Upload or capture an image of the plant
    3. Click **Predict** to analyze
    4. View results and get management recommendations
    
    ### 🧠 Supported Crops:
    - Apple, Corn, Grape, Orange, Peach, Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, Tomato, and more!
    
    Start by navigating to the **Disease Recognition** page in the sidebar!
    """)

# About Page
elif app_mode == "About":
    st.title("About Our System")
    st.markdown("""
    ### 🌟 Our Mission
    Our mission is to help in identifying plant diseases efficiently.
    Discover the future of plant disease detection! Upload a plant image, and our state-of-the-art system will rapidly evaluate it for any disease signs. 
    Partner with us to enhance crop health and secure a thriving harvest through innovative, precise analysis. Let's work together for healthier, more resilient plants.
    
    ### 🔬 How It Works
    1. **Upload Image**: Go to the Disease Recognition page and upload an image of a plant with suspected diseases.
    2. **Analysis**: Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Results**: View the results and recommendations for further action.
    
    ### 🎯 Why Choose Us?
    - **Accuracy**: Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
    - **User-Friendly**: Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient**: Receive results in seconds, allowing for quick decision-making.
    
    ### 📊 Dataset Information
    We use an enhanced dataset derived from an original collection, comprising approximately 87,000 RGB images of both healthy and diseased crop leaves. These images are meticulously categorized into 38 distinct classes, representing a wide array of crops and disease types.
    
    **Dataset Breakdown:**
    - Training Set: 70,295 images for model training.
    - Testing Set: 33 images for evaluating model performance.
    - Validation Set: 17,572 images to fine-tune and validate model accuracy.
    
    ### 🛠️ Technology Stack
    - **Frontend**: Streamlit for beautiful, interactive web interface
    - **Machine Learning**: TensorFlow/Keras for disease classification
    - **AI Chat**: Google Generative AI (Gemini) for intelligent support
    - **Database**: SQLite for storing prediction history
    - **Image Processing**: PIL and OpenCV for image handling
    
    ### 🌱 Recent Work
    - Successfully integrated Google Generative AI for providing chatbot support within the application.
    - Enhanced the machine learning model for better accuracy and faster predictions.
    - Improved user interface and experience.
    """)

# Disease Recognition Page
elif app_mode == "Disease Recognition":
    st.header("Disease Recognition")
    
    # Use camera input for image capture
    test_image = st.camera_input("Capture an Image:")
    
    # Use file uploader for dataset image input
    uploaded_image = st.file_uploader("Or choose an Image from your dataset:", type=["jpg", "jpeg", "png"])
    
    # Determine which image to use for prediction
    if test_image is not None:
        st.image(test_image, use_container_width=True)
        selected_image = test_image
    elif uploaded_image is not None:
        st.image(uploaded_image, use_container_width=True)
        selected_image = uploaded_image
    else:
        selected_image = None
    
    # Prediction button
    if st.button("Predict"):
        if selected_image is not None:
            with st.spinner("Analyzing image..."):
                result_index = model_prediction(selected_image)
                class_name = [
                    'Apple_Apple_scab', 'Apple_Black_rot', 'Apple_Cedar_apple_rust', 'Apple_healthy', 
                    'Blueberry_healthy', 'Cherry(including_sour)_Powdery_mildew', 
                    'Cherry(including_sour)healthy', 'Corn(maize)_Cercospora_leaf_spot Gray_leaf_spot', 
                    'Corn(maize)_Common_rust', 'Corn(maize)_Northern_Leaf_Blight', 'Corn(maize)_healthy', 
                    'Grape_Black_rot', 'Grape_Esca(Black_Measles)', 'Grape_Leaf_blight(Isariopsis_Leaf_Spot)', 
                    'Grape_healthy', 'Orange_Haunglongbing(Citrus_greening)', 'Peach_Bacterial_spot', 
                    'Peach_healthy', 'Pepper_bell_Bacterial_spot', 'Pepper_bell_healthy', 
                    'Potato_Early_blight', 'Potato_Late_blight', 'Potato_healthy', 
                    'Raspberry_healthy', 'Soybean_healthy', 'Squash_Powdery_mildew', 
                    'Strawberry_Leaf_scorch', 'Strawberry_healthy', 'Tomato_Bacterial_spot', 
                    'Tomato_Early_blight', 'Tomato_Late_blight', 'Tomato_Leaf_Mold', 
                    'Tomato_Septoria_leaf_spot', 'Tomato_Spider_mites Two-spotted_spider_mite', 
                    'Tomato_Target_Spot', 'Tomato_Tomato_Yellow_Leaf_Curl_Virus', 
                    'Tomato_Tomato_mosaic_virus', 'Tomato_healthy'
                ]
                
                prediction = class_name[result_index]
                st.success("Model is predicting it's a {}".format(prediction))

                # Save record to database
                insert_record(selected_image.name, prediction)

                # Ask chatbot about disease management
                with st.spinner("Getting management advice..."):
                    management_info = chat_with_me(f"What are the management practices for {prediction}?")
                    st.info(f"Management Information: {management_info}")
        else:
            st.warning("Please capture an image or upload an image from your dataset before attempting to predict.")

# Chat Support Page
elif app_mode == "Chat Support":
    st.header("Agri LifeLine")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    def display_chat():
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.write(f"You: {msg['content']}")
            else:
                st.write(f"Bot: {msg['content']}")

    display_chat()

    def send_message():
        user_message = st.session_state.chat_input
        if user_message:
            st.session_state.messages.append({"role": "user", "content": user_message})
            response = chat_with_me(user_message)
            st.session_state.messages.append({"role": "bot", "content": response})
            st.session_state.chat_input = ""
            st.markdown("<script>window.scrollTo(0, document.body.scrollHeight);</script>", unsafe_allow_html=True)

    user_input = st.text_input("Type your message here:", key="chat_input")
    if st.button("Send"):
        send_message()

# History Page
elif app_mode == "History":
    st.header("Prediction History")
    records = fetch_records()
    if records:
        for record in records:
            st.write(f"ID: {record[0]}")
            st.write(f"Image Path: {record[1]}")
            st.write(f"Prediction: {record[2]}")
            st.write(f"Timestamp: {record[3]}")
            st.write("---")
    else:
        st.write("No records found.")
