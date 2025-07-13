# 👀 Blink Control: Smart Home Automation through Eye Blinks

Unlock a futuristic way to interact with your smart home devices\! **Blink Control** is an innovative Python-based project that transforms your eye blinks into commands for controlling various appliances. By leveraging real-time computer vision and facial landmark detection, this system accurately counts your blinks and triggers predefined actions, offering a hands-free and intuitive automation experience.

Imagine turning off your lights or fan with just a series of deliberate blinks – that's the power of Blink Control\!

-----

## ✨ Features

  * **Real-time Blink Detection**: Utilizes a webcam to continuously monitor eye movements and detect blinks.
  * **Eye Aspect Ratio (EAR) Calculation**: Employs the EAR metric to precisely determine eye closure and openness.
  * **Sequential Blink Recognition**: Counts consecutive blinks to identify specific commands.
  * **Voice Feedback**: Provides audio confirmations for actions performed (e.g., "Turning Light on").
  * **Sound Alerts**: Emits a distinct buzzer sound upon command execution (Windows-specific).
  * **Modular Control System**: Easily extensible `eye_detect.py` class allows you to define and integrate various home automation commands.
  * **On-screen Information**: Displays real-time blink count and EAR values on the video feed.

-----

## 💡 How It Works

1.  **Video Capture**: The system initializes your webcam to capture a live video stream.
2.  **Face & Landmark Detection**: Using `dlib`, it detects your face and pinpoints 68 key facial landmarks, with a focus on your eyes.
3.  **Eye Aspect Ratio (EAR)**: The `eye_aspect_ratio` function calculates a ratio based on the distances between specific eye landmarks. A low EAR indicates a closed eye (a blink).
4.  **Blink Counting**: When the EAR drops below a set threshold for a specified number of consecutive frames, a blink is registered.
5.  **Command Triggering**: A `TOTAL` blink counter accumulates blinks. When `TOTAL` reaches a predefined number (e.g., 8 blinks), it triggers an action defined in `eye_detect.py`. This counter then resets.
6.  **Action Execution**: The `Myclass.Blink()` method in `eye_detect.py` maps the `TOTAL` blink count to specific voice commands and buzzer sounds, simulating control over devices (e.g., "Light on", "Fan off").

-----

## 🛠 Technologies Used

  * **Python**: The core programming language.
  * **OpenCV (`opencv-python`)**: For real-time video capture, image processing, and displaying the feed.
  * **dlib**: For robust face detection and high-accuracy facial landmark prediction.
  * **NumPy**: For efficient numerical operations on image and landmark data.
  * **SciPy (`scipy.spatial.distance`)**: Used for calculating Euclidean distances for the EAR.
  * **imutils**: A collection of OpenCV convenience functions for easier video stream handling and image resizing.
  * **pyttsx3**: For text-to-speech capabilities, providing audible feedback.
  * **winsound**: For playing system sounds/beeps (Windows-specific).
  * **argparse**: For handling command-line arguments (e.g., specifying the path to the facial landmark predictor).
  * **datetime**: For potential timestamping or timing functionalities.

-----

## 🚀 Getting Started

Follow these steps to set up and run the Blink Control system on your local machine.

### Prerequisites

  * **Python 3.x**
  * **`shape_predictor_68_face_landmarks.dat`**: This crucial file for `dlib` enables accurate facial landmark detection. You can download it from [dlib's official website](https://www.google.com/search?q=http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2). Make sure to uncompress it and place it in the same directory as `main.py` or provide its path via the command line argument.

### Installation

1.  **Clone the Repository (if applicable)**:

    ```bash
    git clone https://github.com/0YogeshKumar/Blink_Control_Automation.git # Replace with your actual repo URL
    cd Blink_Control_Automation # Adjust path as necessary
    ```

2.  **Create a Virtual Environment (Recommended)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install Dependencies**:
    While a `requirements.txt` was not explicitly provided for this set of files, based on the imports, you will need:

    ```bash
    pip install opencv-python dlib scipy numpy imutils pyttsx3
    ```

      * **Note for Linux/macOS users**: `winsound` is Windows-specific. For audio alerts, `pyttsx3` might require additional setup for speech engines (e.g., `espeak`, `nsspeechsynthesizer`). Refer to `pyttsx3` documentation for details.

### Running the System

1.  **Place `shape_predictor_68_face_landmarks.dat`**: Ensure this file is in the same directory as `main.py` or ready to be pointed to.

2.  **Execute the main script**:

    ```bash
    python main.py -p shape_predictor_68_face_landmarks.dat
    ```

    (Replace `shape_predictor_68_face_landmarks.dat` with the actual path if it's not in the same directory.)

    Your webcam feed will open, and the system will begin detecting blinks. Try blinking deliberately to trigger the defined actions\!

-----

## ⚙️ Customization

  * **`eye_detect.py`**: Modify the `Myclass.Blink` method to add or change the actions triggered by different blink counts (e.g., 1 blink for "Hello", 2 blinks for "Goodbye").
  * **`main.py`**: Adjust `EYE_AR_THRESH` (eye aspect ratio threshold) and `EYE_AR_CONSEC_FRAMES` (consecutive frames for blink detection) to fine-tune sensitivity. The `TOTAL` blink count and its reset logic can also be modified.

-----

## 🤝 Contributing

Contributions are highly appreciated\! If you have ideas for new features (e.g., integrating with actual smart home APIs, more sophisticated gesture recognition, cross-platform audio), bug fixes, or performance improvements, please:

  * Open an issue
  * Submit a pull request

-----

## 🙏 Acknowledgments

  * Thanks to the `dlib` and `OpenCV` libraries for making computer vision accessible.
  * Inspired by the possibilities of human-computer interaction through natural gestures.

-----
