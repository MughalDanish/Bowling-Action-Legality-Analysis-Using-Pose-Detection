# Bowling Action Legality Analysis Using Pose Detection

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Build Status](https://img.shields.io/github/workflow/status/MughalDanish/Bowling-Action-Legality-Analysis-Using-Pose-Detection/CI)
![Contributors](https://img.shields.io/github/contributors/MughalDanish/Bowling-Action-Legality-Analysis-Using-Pose-Detection)
![Stars](https://img.shields.io/github/stars/MughalDanish/Bowling-Action-Legality-Analysis-Using-Pose-Detection)
![Forks](https://img.shields.io/github/forks/MughalDanish/Bowling-Action-Legality-Analysis-Using-Pose-Detection)

## Project Description

Bowling Action Legality Analysis Using Pose Detection is a system designed to analyze and classify the legality of a bowler's action in cricket using advanced pose detection techniques. The system leverages computer vision and machine learning to detect body keypoints, calculate joint angles, and determine whether a bowling action conforms to the legal standards set by cricket authorities.

### Features
- **Pose Detection**: Utilizes state-of-the-art models to detect and track body keypoints in real-time.
- **Angle Calculation**: Computes joint angles to assess the bowling action.
- **Legality Classification**: Classifies the bowling action as legal or illegal based on calculated angles.
- **Real-Time Analysis**: Provides instantaneous feedback on the legality of the bowling action.
- **User-Friendly Interface**: Easy-to-use interface for uploading videos and viewing results.

## Demo & Screenshots

![Demo Video](https://link-to-demo-video.com)
![Screenshot](https://link-to-screenshot.com)

## Features

- 📷 **Pose Detection**: Accurate detection of body keypoints using advanced models.
- 📐 **Angle Calculation**: Precise calculation of joint angles for legality analysis.
- 🏏 **Legality Classification**: Robust classification of bowling actions as legal or illegal.
- ⏱️ **Real-Time Analysis**: Instant feedback on bowling action legality.
- 💻 **User-Friendly Interface**: Simple and intuitive interface for user interaction.

## Installation

Follow these steps to set up the project:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/MughalDanish/Bowling-Action-Legality-Analysis-Using-Pose-Detection.git
    cd Bowling-Action-Legality-Analysis-Using-Pose-Detection
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Download Pre-trained Models**:
    - Download the pose detection model from [Mediapipe Models](https://link-to-mediapipe-models.com) and place it in the `models` directory.

## Usage Guide

To analyze a bowling action video, follow these steps:

1. **Run the System**:
    ```bash
    python main.py --video path/to/your/video.mp4
    ```

2. **View Results**:
    - The results will be displayed in the console and saved in the `output` directory.

## Model & Dataset

- **Pre-trained Models**: The system uses pre-trained models from [Mediapipe](https://mediapipe.dev) for pose detection.
- **Datasets**: Various cricket bowling action videos were used for training and testing the system.

## Technologies Used

- **Programming Languages**: Python
- **Frameworks & Libraries**: 
    - OpenCV
    - Mediapipe
    - TensorFlow
    - PyTorch
    - Flask

## Project Structure

```
Bowling-Action-Legality-Analysis-Using-Pose-Detection/
│
├── models/                 # Pre-trained models
├── datasets/               # Dataset used for training and testing
├── output/                 # Output results
├── scripts/                # Utility scripts
│   ├── pose_detection.py   # Pose detection logic
│   ├── angle_calculation.py # Angle calculation logic
│   └── legality_classification.py # Legality classification logic
├── main.py                 # Main execution script
├── requirements.txt        # Project dependencies
└── README.md               # Project README file
```

## Contributing

We welcome contributions from the community! Here’s how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact & Support

If you have any questions or need support, feel free to reach out:

- **Email**: mughaldanish@example.com
- **GitHub Issues**: [Create an Issue](https://github.com/MughalDanish/Bowling-Action-Legality-Analysis-Using-Pose-Detection/issues)

We appreciate your feedback and contributions!
