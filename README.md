# Real-time hand scanner
**About**: <br>
I used OpenCV and MediaPipe to create a real-time hand tracker that creates an outline of your hand making connections between your finger joints and fingertips while a hand is detected in the camera

**Goal**: <br>
I hoped to have a finalized version to interpret hand signs using a machine-learning classifier. I would need to train this model and make it return what it recognizes

This is something I'm pretty excited to learn about
At the moment I have only implemented the hand tracker

# Download instructions

Real-time hand tracking and inference using the MediaPipe library and OpenCV.

## Requirements

- Python 3.7 or later
- OpenCV
- MediaPipe

## Installation

1. **Create a Virtual Environment**:
    ```sh
    python -m venv .venv
    ```

2. **Activate the Virtual Environment**:
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

3. **Upgrade `pip`**:
    ```sh
    python -m pip install --upgrade pip
    ```

4. **Install Required Packages**:
    ```sh
    pip install opencv-python mediapipe
    ```

## Usage

Run the following command to start the hand tracker:

```sh
python main.py
