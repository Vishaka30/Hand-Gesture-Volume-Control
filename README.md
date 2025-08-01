# 🖐️ Hand Gesture Volume Control

Control your system's volume using just your hand gestures via webcam!

This Python-based project uses **OpenCV** and **MediaPipe** to track your hand in real time. By measuring the distance between your thumb and index finger, it adjusts the volume dynamically — all without touching your keyboard or mouse.

## 🔧 Features

- 🖥️ Real-time gesture recognition using webcam  
- 📈 Dynamic volume control:  
  - ✋ Fingers apart → Volume Up  
  - 🤏 Fingers close → Volume Down  
- ⚙️ Supports both **Windows** and **macOS**  
- 🧠 Uses **pycaw** for Windows audio control and **AppleScript** for macOS  

## 🛠️ Tech Stack

- **Python 3**
- OpenCV
- MediaPipe
- pycaw (Windows only)

## 📦 Installation

### 1. Clone the repository
```bash

git clone https://github.com/vishaka30/Hand-Gesture-Volume-Control.git
cd hand-gesture-volume-control
```

### 2. Install dependencies
Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install required packages:
```bash
pip install -r requirements.txt
```

If you're on Windows, also install:
```bash
pip install pycaw comtypes
```

## ▶️ Usage

Run the script:

```bash
python gesture_volume.py
```

- Make sure your webcam is connected.
- Move your thumb and index finger to control volume.
- Press ESC to exit.

## ⚠️ Supported Platforms

| OS      | Status    |
|---------|-----------|
| ✅ Windows | Full support via `pycaw` |
| ✅ macOS   | Volume control via AppleScript |
| ❌ Linux   | Not supported |

## 📁 File Structure

```
hand-gesture-volume-control/
├── gesture_volume.py       # Main script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🧠 How It Works

1. Captures video input using OpenCV.  
2. Detects hand landmarks with MediaPipe.  
3. Measures distance between thumb and index finger tips.  
4. Increases or decreases volume based on the distance.

## 🙌 Contribution

Contributions are welcome!  
Feel free to open an issue or submit a pull request.

## 📄 License

Licensed under the [MIT License](LICENSE).

## 💡 Tip

If you like this project, give it a ⭐ and share it with others!
