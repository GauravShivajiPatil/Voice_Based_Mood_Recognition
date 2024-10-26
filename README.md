# Voice-Based Mood Recognition

This project aims to recognize emotions from speech, including both recorded and live audio inputs. The system detects emotions such as happy, sad, angry, and neutral, while also converting audio to text and offering language translation. This README includes the project setup, code usage, and information on the employed models.

## Table of Contents
- [Introduction](#introduction)
- [Motivation and Objective](#motivation-and-objective)
- [Project Scope](#project-scope)
- [Technical Overview](#technical-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Speech Emotion Recognition (SER) involves detecting emotions from voice inputs. This project classifies emotions from audio data by extracting key features using Mel-Frequency Cepstral Coefficients (MFCC), Chroma, and Mel spectrograms.

## Motivation and Objective
The project aims to support applications in medical fields, customer service, and educational tools by understanding the emotional state from speech data. Potential applications include automated call centers and personalized educational tools.

## Project Scope
- **Emotion Detection**: Recognizes moods like happy, sad, angry, and neutral.
- **Speech-to-Text Conversion**: Converts speech into English text.
- **Language Translation**: Provides English translations of other languages.
- **Web Application**: Accessible online, designed for ease of use.

## Technical Overview
The project leverages neural networks, specifically:
1. **Sequential Neural Networks (SNN)**: For emotion classification.
2. **MLP Classifier**: A multi-layer perceptron model for additional mood classification.

### System Architecture
- **Input**: User-provided recorded or live audio.
- **Feature Extraction**: MFCC, Chroma, and Mel spectrograms.
- **Classification Model**: SNN and MLP Classifier.
- **Output**: Identified mood, emotion emoji, and text transcription.

## Installation

### Prerequisites
- Python 3.x
- Required packages: NumPy, Pandas, Librosa, Scikit-Learn, Flask, Spyder (or another IDE with Python support).

### Steps
1. Clone this repository:
    ```bash
    git clone https://github.com/username/voice-mood-recognition.git
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Flask app:
    ```bash
    python app.py
    ```

## Usage
1. Launch the application in your browser.
2. Upload an audio file or use the live audio input feature.
3. View the detected mood, speech transcription, and emoji display.
4.  Upload an Audio File or Use Live Recording to analyze mood.
5. View detected emotion indicators and text transcription.
6. For language translation, select desired options (if available).

## Technologies Used
- **Programming Language**: Python
- **Framework**: Flask
- **Libraries**: NumPy, Pandas, Librosa, Scikit-Learn, Seaborn

## Usage
1. Upload an Audio File or Use Live Recording to analyze mood.
2. View detected emotion indicators and text transcription.
3. For language translation, select desired options (if available).

## Testing
- Functional, integration, and performance tests were performed to ensure reliable emotion detection, accurate transcription, and a user-friendly interface. See Testing Documentation for detailed test cases and results.

## Project Scope and Limitations
This project is web-focused and may encounter limitations when integrating with hardware like robotics or IoT devices.

## Future Enhancements
Improved Model Accuracy: Further training with more diverse datasets.
Expanded Language Support: Include additional languages for text conversion and translation.
Hardware Integration: Future support for integration with voice-activated devices and IoT applications.

## Contributing
Contributions are welcome! Please fork this repository, create a new branch, and submit a pull request.

## License
This project is licensed under the MIT License.

## VIEW OF PROJECT 
![HOME_PAGE](https://github.com/user-attachments/assets/744dc0ce-d3b5-4410-8fc6-b985187a578b)
)

