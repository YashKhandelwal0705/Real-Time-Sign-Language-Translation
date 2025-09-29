# Sign Language Translation System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A real-time Sign Language Translation system that converts hand gestures into text using computer vision and deep learning.

## 🚀 Features

- 📱 Real-time hand gesture detection using MediaPipe
- 🤝 Support for 4 gestures: A, F, L, Y
- 🌐 Web-based interface with Flask
- 📺 Real-time video streaming
- 🛡️ Robust error handling and frame boundary detection
- 📱 Mobile-friendly interface

## 🛠️ Tech Stack

- **Backend**: Python 3.12+
- **Computer Vision**: OpenCV, MediaPipe
- **Deep Learning**: YOLOv8
- **Web Framework**: Flask
- **Model**: PyTorch

## 📥 Installation

1. Clone the repository:
```bash
git clone https://github.com/YashKhandelwal0705/Real-Time-Sign-Language-Translation.git
cd Real-Time-Sign-Language-Translation
```

2. Create and activate virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
# or
source venv/bin/activate   # Unix/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Train the model (required):
```bash
python "Python Files/train.py"
```
This will create the necessary model file at `runs/detect/train/weights/best.pt`

## 🚀 Usage

1. Run the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:5000/
```

3. Point your webcam at your hand and make gestures (A, F, L, Y)

## 📁 Project Structure

```
Real-Time-Sign-Language-Translation/
├── app.py               # Main Flask application
├── templates/           # HTML templates
│   └── index.html      # Web interface
├── Python Files/       # Core Python scripts
│   ├── Yolo.py         # YOLO model implementation
│   ├── Feature Extraction.py  # Data preprocessing
│   ├── train.py        # Model training script
│   ├── Hand Detector.py # Hand detection utilities
│   └── ...             # Other utility scripts
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── setup.py           # Package setup
└── LICENSE            # License file

Note: Dataset/ and runs/ folders are not included in the repository due to size constraints.
```

## 🎯 How it Works

1. The system uses MediaPipe's hand tracking module to detect hands in real-time
2. Hand regions are extracted and normalized
3. The YOLOv8 model classifies the gestures into one of the supported categories
4. Results are displayed in real-time via a Flask web interface

## 📱 Supported Gestures
- A: Closed fist with thumb up
- F: Five fingers spread
- L: L-shaped hand
- Y: Y-shaped hand (V sign)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🤝 Acknowledgments

- Thanks to the MediaPipe team for their excellent hand tracking module
- Thanks to the YOLOv8 team for their efficient object detection framework
- Thanks to Flask for providing a simple web framework

## 📞 Contact

Yash Khandelwal - [GitHub](https://github.com/YashKhandelwal0705)

Project Link: [https://github.com/YashKhandelwal0705/Sign-Language-Translation-System](https://github.com/YashKhandelwal0705/Sign-Language-Translation-System)
