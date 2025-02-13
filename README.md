# Real-time Hand Scanner

**About**:  
I used OpenCV and MediaPipe to create a real-time hand tracker that creates an outline of your hand, connecting your finger joints and fingertips while a hand is detected in the camera.

**Goal**:  
I hope to have a finalized version to interpret hand signs using a machine-learning classifier. I need to train this model and make it return what it recognizes.

This is something I'm pretty excited to learn about. At the moment, I have only implemented the hand tracker.

## Download Instructions

Real-time hand tracking and inference using the MediaPipe library and OpenCV.

### Requirements

- Python 3.7 or later(not all python releases are compatible with pip, I use 3.11.0)
- OpenCV
- MediaPipe

### Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/Twqy/hand-scanner
    cd hand-scanner
    ```

2. **Create a Virtual Environment**:
    ```sh
    python -m venv .venv
    ```

3. **Activate the Virtual Environment**:
    - For Command Prompt:
        ```sh
        .venv\Scripts\activate.bat
        ```
    - For PowerShell:
        ```sh
        .venv\Scripts\Activate.ps1
        ```
    - For Git Bash or WSL:
        ```sh
        source .venv/Scripts/activate
        ```

4. **Upgrade `pip`**:
    ```sh
    python -m pip install --upgrade pip
    ```

5. **Install Required Packages**:
    ```sh
    pip install opencv-python mediapipe
    ```

### Usage

Run the following command to start the hand tracker(exit by pressing the ESC key):

```sh
python main.py

https://github.com/user-attachments/assets/dff0fefd-c044-4dff-ab69-696c2bde01ff

