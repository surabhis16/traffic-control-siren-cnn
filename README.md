# 🚑 **Emergency Vehicle Detection and Traffic Light Control System**

This project aims to seamlessly integrate **audio processing** and **Arduino-based control systems** to **detect ambulance sirens** and dynamically manage **traffic lights**. The objective is to minimize delays at intersections, ultimately saving lives.

---

## 🚀 **Key Features**

- **🎶 Audio Detection:**  
  Detects ambulance sirens from ambient noise using **MFCC** feature extraction followed by a **Convolutional Neural Network (CNN)** classifier for precise recognition.

- **🚦 Traffic Light Control:**  
  Uses an **Arduino microcontroller** to switch traffic light states based on real-time audio classification results.

- **💡 LCD Display Integration:**  
  The system displays the current status (e.g., "Ambulance" or "Not Ambulance") and a countdown timer for the red light.

---

## ⚙️ **Prerequisites**

### Software Requirements:
- **Python 3.8+**  
- **Key Libraries:**
   - `librosa` (for audio feature extraction)
   - `numpy`, `pandas`, `matplotlib` (for data handling and visualization)
   - `tensorflow` (for model training and inference)
   - `scikit-learn` (for machine learning utilities)
   - `pickle`, `IPython` (for saving and loading models)

- **Arduino IDE**  
  - For uploading the traffic light control script to the Arduino.

### Hardware Requirements:
- **Microcontroller:** Arduino Uno or similar.
- **Peripherals:**
   - Red and Green **LEDs** for traffic light simulation
   - **LCD Display (16x2)** with I2C interface for status messages

---

## 🗂️ **Project File Structure**

```plaintext
project/
│
├── python_scripts/
│   ├── feature_extraction.py         # Audio feature extraction script
│   ├── trainingsavingmodel.py        # Script to train CNN model on features
│   ├── saved_model352.h5            # Trained model weights
│   ├── Extracted_Features352.pkl    # Serialized feature set
│
├── arduino_code/
│   ├── trafficlightswithlcd.ino    # Arduino code to control traffic lights
└── README.md                        # Project documentation
```

---

## 🏁 **Getting Started**

### **Step 1: Dataset Preparation**

The dataset contains **12,000 audio files**, primarily sourced from Kaggle. The files are categorized as follows:

```
sounds/
├── ambulance/
├── notambulance/
```

Each category contains various `.wav` files used for training the model. The ambulance sounds represent emergency vehicle sirens, while the notambulance sounds include everyday noises for classification contrast.

1. **Organize `.wav` Files:**  
   Place your `.wav` files under two directories as shown:
   ```plaintext
   sounds/
   ├── ambulance/
   └── notambulance/
   ```

2. Ensure the dataset contains enough samples for both classes to train the model effectively.

---

### **Step 2: Feature Extraction and Model Training**

1. **Feature Extraction:**
   Extract the **MFCC features** from your audio files by running:
   ```bash
   python feature_extraction.py
   ```
   - This script will save the extracted features into `Extracted_Features352.pkl`.

2. **Training the Model:**  
   Use the extracted features to train a **CNN model**:
   ```bash
   python train_model.py
   ```
   - The model will be saved as `saved_model352.h5`, which you can later load for inference.

---

### **Step 3: Upload Arduino Code**
1. **Hardware Setup:**  
   - Connect your **Red** and **Green LEDs** to **digital pins 13** and **5**, respectively.
   - Connect the **LCD** to the **SDA** and **SCL** pins (A4 and A5 on Arduino Uno).
   
2. **Upload the Code:**  
   Open the `trafficlightswithlcd.ino` in the **Arduino IDE**, verify, and upload it to your Arduino board.

---

## 🖥️ **Usage**

1. **Start Python Script:**  
   Once the model is trained, run the following script to classify new audio inputs and send the classification result ("ambulance" or "notambulance") via serial communication to the Arduino:
   ```bash
   python trainingsavingmodel.py
   ```
   - The classification result is then passed to Arduino, triggering the appropriate traffic light behavior.

2. **Traffic Light Control (Arduino):**  
   - **Ambulance Detected:** The **green light** will turn on for **5 seconds** to allow the ambulance to pass.
   - **Not Ambulance:** The system will continue its default **red light cycle**.

---

## 🔌 **Circuit Connections**

### LED Connections:
- **Red LED:** Pin 13 (Digital)
- **Green LED:** Pin 5 (Digital)

### LCD Connections (I2C Interface):
- **SDA:** A4
- **SCL:** A5
- **Power:** 5V
- **Ground:** GND

---

## 📱 **Example Outputs**

### LCD Display:
- **"Ambulance"**:  
  The **green light** activates for 5 seconds, allowing the ambulance to pass.
  
- **"Timer: XX secs"**:  
  Displays the remaining time for the **red light**.

---

## 🛠️ **Troubleshooting**

1. **Python Issues:**
   - Ensure all required libraries are installed using `pip install -r requirements.txt`.
   - Double-check file paths for the **audio files**, **feature files**, and **model weights**.

2. **Arduino Issues:**
   - Confirm serial communication between the Python script and Arduino is working.
   - Ensure LEDs and LCD are wired correctly.

3. **LCD Not Displaying:**
   - Verify the **I2C address** (`0x27`) matches the one used by your LCD module.

---

## 🌱 **Future Enhancements**
- **Real-Time Audio Detection:**  
  Integrate a **microphone** for live audio detection and processing, enabling real-time traffic control.

- **GPS Integration:**  
  Add **GPS modules** to track ambulance locations and optimize traffic light control across multiple intersections.

- **Computer Vision:**  
  Integrate **computer vision** for vehicle detection and classification, adding an additional layer of accuracy in distinguishing emergency vehicles.

- **Multi-Intersection Control:**  
  Extend the system to control **multiple traffic lights** in real time across a city.

---

## 📝 **License**

This project is licensed under the **MIT License**.
