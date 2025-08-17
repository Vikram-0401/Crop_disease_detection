# 🌱 Plant Disease Detection System

Our mission is to help in identifying plant diseases efficiently.
Discover the future of plant disease detection! Upload a plant image, and our state-of-the-art system will rapidly evaluate it for any disease signs. 
Partner with us to enhance crop health and secure a thriving harvest through innovative, precise analysis. Let's work together for healthier, more resilient plants.

## 🚀 Features

- **State-of-the-Art ML Models**: Our system employs advanced machine learning algorithms to achieve high precision in detecting plant diseases.
- **Instant Chat Support**: With Google Generative AI integration, users receive real-time assistance, answering queries and providing support related to plant health.
- **User-Friendly Interface**: Simple and intuitive interface for seamless user experience.
- **Fast and Efficient**: Receive results in seconds, allowing for quick decision-making.
- **Comprehensive Disease Database**: Covers 38 distinct classes of plant diseases and healthy conditions.

## 🏗️ Project Structure

```
Plant-Disease-Detection-system-master/
├── main.py                              # Main Streamlit application
├── requirements.txt                     # Python dependencies
├── trained_plant_disease_model.keras   # Pre-trained TensorFlow model
├── test/                               # Test images for different plant diseases
├── *.db                                # SQLite database files for history and feedback
└── README.md                           # This file
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vikram-0401/Crop_disease_detection.git
   cd Crop_disease_detection
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv plant_disease_env
   ```

3. **Activate the virtual environment**
   ```bash
   # On Linux/Mac
   source plant_disease_env/bin/activate
   
   # On Windows
   plant_disease_env\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   streamlit run main.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:8501`

### Alternative: One-liner setup
```bash
git clone https://github.com/Vikram-0401/Crop_disease_detection.git && \
cd Crop_disease_detection && \
python3 -m venv plant_disease_env && \
source plant_disease_env/bin/activate && \
pip install -r requirements.txt && \
streamlit run main.py
```

## 📱 How It Works

1. **Upload Image**: Go to the Disease Recognition page and upload an image of a plant with suspected diseases.
2. **Analysis**: Our system will process the image using advanced algorithms to identify potential diseases.
3. **Results**: View the results and recommendations for further action.

## 🧠 Technical Details

### Machine Learning Model
- **Framework**: TensorFlow/Keras
- **Architecture**: Convolutional Neural Network (CNN)
- **Input Size**: 128x128 RGB images
- **Output**: 38-class classification

### Supported Plant Diseases
The system can detect diseases in the following crops:
- **Apple**: Apple scab, Black rot, Cedar apple rust, Healthy
- **Blueberry**: Healthy
- **Cherry**: Powdery mildew, Healthy
- **Corn**: Cercospora leaf spot, Common rust, Northern Leaf Blight, Healthy
- **Grape**: Black rot, Esca, Leaf blight, Healthy
- **Orange**: Haunglongbing (Citrus greening)
- **Peach**: Bacterial spot, Healthy
- **Pepper**: Bacterial spot, Healthy
- **Potato**: Early blight, Late blight, Healthy
- **Raspberry**: Healthy
- **Soybean**: Healthy
- **Squash**: Powdery mildew
- **Strawberry**: Leaf scorch, Healthy
- **Tomato**: Bacterial spot, Early blight, Late blight, Leaf Mold, Septoria leaf spot, Spider mites, Target Spot, Yellow Leaf Curl Virus, Mosaic virus, Healthy

### Dataset
- **Total Images**: ~87,000 RGB images
- **Training Set**: 70,295 images
- **Testing Set**: 33 images
- **Validation Set**: 17,572 images
- **Classes**: 38 distinct classes

### Technologies Used
- **Frontend**: Streamlit
- **Backend**: Python
- **ML Framework**: TensorFlow/Keras
- **AI Chat**: Google Generative AI (Gemini)
- **Database**: SQLite
- **Image Processing**: PIL (Pillow), OpenCV

## 🔧 Configuration

### Environment Variables
The application uses the following environment variables:
- `GOOGLE_API_KEY`: Google Generative AI API key (already configured)

### Model Configuration
- Model file: `trained_plant_disease_model.keras`
- Input image size: 128x128 pixels
- Supported formats: JPG, JPEG, PNG

## 🧪 Testing

### Test Images
The `test/` directory contains sample images for testing:
- Various plant diseases
- Healthy plant samples
- Different image qualities and angles

### Running Tests
```bash
# Activate virtual environment
source plant_disease_env/bin/activate

# Run the application
streamlit run main.py

# Test with sample images from the test/ directory
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Contributing Guidelines

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test your changes**
5. **Commit your changes**
   ```bash
   git commit -m "Add: description of your changes"
   ```
6. **Push to your branch**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

### Areas for Contribution
- **Model Improvements**: Enhance the ML model accuracy
- **UI/UX**: Improve the Streamlit interface
- **New Features**: Add support for more plant species
- **Documentation**: Improve code comments and documentation
- **Testing**: Add unit tests and integration tests
- **Performance**: Optimize image processing and prediction speed

### Code Style
- Follow PEP 8 Python style guidelines
- Add docstrings to functions and classes
- Include type hints where possible
- Write clear commit messages

## 🐛 Troubleshooting

### Common Issues

1. **CUDA/GPU Errors**
   - The system will automatically fall back to CPU if GPU is not available
   - This is normal and won't affect functionality

2. **Model Loading Issues**
   - Ensure `trained_plant_disease_model.keras` is in the project root
   - Check file permissions

3. **Dependency Issues**
   - Always use the virtual environment
   - Update pip: `pip install --upgrade pip`
   - Clear pip cache: `pip cache purge`

4. **Port Already in Use**
   - Kill existing processes: `pkill -f streamlit`
   - Use different port: `streamlit run main.py --server.port 8502`

## 📊 Performance

- **Prediction Time**: < 1 second per image
- **Accuracy**: High precision across all disease classes
- **Memory Usage**: Optimized for both CPU and GPU environments

## 🔒 Privacy & Security

- **Local Processing**: Images are processed locally
- **No Data Storage**: Uploaded images are not permanently stored
- **API Security**: Google AI API calls are secured

## 📞 Support

- **GitHub Issues**: Report bugs and feature requests
- **Documentation**: Check this README and code comments
- **Community**: Join discussions in GitHub discussions

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Original dataset contributors
- TensorFlow and Streamlit communities
- Google Generative AI team
- All contributors and users

---

**Get Started**: Navigate to the Disease Recognition page in the sidebar to upload your plant image and witness the capabilities of our cutting-edge Plant Disease Recognition System. This powerful tool will analyze your image in-depth, providing you with accurate insights and disease detection. Explore the technology that's transforming plant health management and optimize your crop care with just a few clicks.

**About Us**: This project harnesses the power of machine learning to revolutionize plant disease detection through image analysis. By employing TensorFlow for precise model predictions and Google Generative AI for interactive chatbot support, our system is crafted to aid farmers and researchers in diagnosing plant health with unparalleled efficiency.

---

⭐ **Star this repository if you find it helpful!**
