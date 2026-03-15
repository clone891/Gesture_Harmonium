# AirSwar 🎹
### Gesture-Controlled Harmonium using Computer Vision

AirSwar is a computer-vision powered digital harmonium that simulates real harmonium bellows using hand gestures captured from a webcam. The instrument uses gesture pumping to control airflow and keyboard keys to play musical notes, producing sound from real harmonium recordings.

The project combines computer vision, gesture recognition, and real-time audio synthesis to recreate the playing experience of a traditional harmonium.

---

## Features

- Gesture-controlled bellows simulation
- Index finger pumping motion controls airflow
- Keyboard keys play notes
- Supports multiple simultaneous notes (chords)
- Uses real harmonium sound samples
- Smooth airflow decay and filtering for realistic sound
- Live visual airflow indicator

---

## How It Works

AirSwar mimics how a real harmonium works:

1. A webcam detects your hand using MediaPipe.
2. The index finger's vertical motion is tracked.
3. Downward pumping motion increases air pressure (airflow).
4. Airflow controls the volume of the harmonium sound.
5. Keyboard keys trigger individual harmonium notes.

> **Gesture + Keys = Digital Harmonium 🎶**

---

## Controls

| Action | Function |
|---|---|
| Move index finger up/down | Pump bellows |
| `A` | Sa |
| `S` | Re |
| `D` | Ga |
| `F` | Ma |
| `G` | Pa |
| `H` | Dha |
| `J` | Ni |
| `ESC` | Exit program |

> Multiple keys can be pressed simultaneously to play chords.

---

## Project Structure

```
harmonium/
│
├── main.py
├── requirements.txt
├── hand_landmarker.task
│
└── sounds/
    ├── sa.wav
    ├── re.wav
    ├── ga.wav
    ├── ma.wav
    ├── pa.wav
    ├── dha.wav
    └── ni.wav
```

---

## Installation

**Clone the repository:**

```bash
git clone https://github.com/yourusername/airswar.git
cd airswar
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## Running the Project

```bash
python main.py
```

The webcam window will open and the harmonium will be ready to play.

---

## Technologies Used

- **Python**
- **OpenCV**
- **MediaPipe**
- **Pygame**
- Computer Vision
- Real-time gesture tracking

---

## Future Improvements

- Two-hand interaction (one hand for bellows, one for notes)
- Air reservoir simulation like real harmoniums
- Gesture-controlled octave shifting
- Automatic tanpura / raga accompaniment
- MIDI export or DAW integration

---

## Inspiration

This project explores how computer vision can be used to create new musical interfaces, blending traditional instruments with modern technology.

---

## License

This project is open source and available under the [MIT License](LICENSE).
