
# Emergency Vehicle Detection and Traffic Light Control System

This project uses audio processing and Arduino-based hardware control to detect ambulance sirens and dynamically manage traffic lights. The goal is to create a "green corridor" for emergency vehicles to ensure minimal delays at intersections.

---

## Features
- **Audio Detection:**  
  Detects ambulance sirens using MFCC feature extraction and a CNN-based classifier.
- **Traffic Light Control:**  
  Arduino switches between red and green lights based on detected audio.
- **LCD Display:**  
  Displays the timer and the current state (e.g., "Ambulance" or "Not Ambulance").

---

## Prerequisites

### Software:
1. **Python 3.8+**
2. **Libraries:**
   - `librosa`
   - `numpy`
   - `pandas`
   - `matplotlib`
   - `tensorflow`
   - `scikit-learn`
   - `pickle`
   - `IPython`
3. **Arduino IDE** for uploading the traffic light control code.

### Hardware:
- Arduino Uno or similar microcontroller.
- Red and Green LEDs.
- LCD Display (16x2) with I2C interface.

---

## File Structure

```
project/
│
├── python_scripts/
│   ├── feature_extraction.py       # Extracts MFCC features from audio files.
│   ├── train_model.py              # Trains the CNN classifier.
│   ├── saved_model352.h5           # Pretrained CNN model for classification.
│   ├── Extracted_Features352.pkl   # Extracted features for training/testing.
│
├── arduino_code/
│   ├── traffic_light_control.ino   # Arduino code for traffic light management.
│
└── README.md                       # Documentation file.
```

---

## Getting Started

### Step 1: Dataset Preparation
1. Organize `.wav` files in a directory structure:
   ```
   sounds/
   ├── ambulance/
   ├── notambulance/
   ```
2. Place `.wav` files under the respective folders.

---

### Step 2: Feature Extraction and Model Training
1. Run the `feature_extraction.py` script:
   ```bash
   python feature_extraction.py
   ```
   - Extracts MFCC features and saves them in `Extracted_Features352.pkl`.

2. Train the CNN model using `train_model.py`:
   ```bash
   python train_model.py
   ```
   - Saves the trained model as `saved_model352.h5`.

---

### Step 3: Upload Arduino Code
1. Connect the LEDs and LCD to the Arduino.
2. Open `traffic_light_control.ino` in the Arduino IDE.
3. Verify and upload the code to the Arduino board.

---

## Usage

1. **Start Python Script:**  
   Use the trained model to classify real-time audio or pre-recorded `.wav` files.

   ```bash
   python classify_audio.py
   ```

   - Sends "ambulance" or "notambulance" messages to the Arduino via serial.

2. **Arduino Traffic Light Control:**  
   Based on the classification:
   - If "ambulance" is detected: Green light turns on for 5 seconds.
   - If "notambulance" is detected: Default red light timer continues.

---

## Circuit Connections

1. **LEDs:**
   - Red LED: Digital Pin 13
   - Green LED: Digital Pin 5

2. **LCD Display:**
   - SDA: A4
   - SCL: A5
   - Power: 5V
   - Ground: GND

---

## Example Outputs

### LCD Messages:
1. `Ambulance`  
   - Green light turns on for 5 seconds.

2. `Timer: XX secs`  
   - Displays the remaining time for the red light.

---

## Troubleshooting

1. **Python Errors:**
   - Ensure all required libraries are installed.
   - Verify paths for audio files, feature files, and model files.

2. **Hardware Issues:**
   - Check Arduino serial communication setup.
   - Verify connections to LEDs and LCD.

3. **LCD Not Displaying:**
   - Ensure the I2C address (`0x27`) matches your LCD module.

---

## Future Enhancements
- Integrate real-time audio input for continuous detection.
- Add location tracking for ambulances using GPS modules.
- Expand the system to control multiple intersections.

---

## License
This project is licensed under the MIT License.

---

## Author
**[Your Name]**  
For any questions or contributions, feel free to reach out!

--- 

This `README.md` file can be placed in your project folder to provide clear documentation.
