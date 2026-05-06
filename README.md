# IntenseOS Air Mouse

Control the system pointer with hand gestures using the webcam. This project is built around computer vision (OpenCV, MediaPipe), optional ML (PyTorch), and desktop automation (`pyautogui`, `pynput`).

## Features (intended)

- **Camera input** — capture frames and track hands or pose.
- **Gesture mapping** — interpret gestures as pointer moves, clicks, or scroll.
- **Smoothing / tracking** — filtering (e.g. Kalman-style) for stable cursor motion.

The entry point is `app/main.py` (wire up your pipeline there).

## Requirements

- **Python** 3.10+ recommended (tested in development with 3.13).
- A **webcam**.
- On macOS, you may need to grant **Camera** and **Accessibility** permissions for the terminal or IDE running the app so the camera works and synthetic input is allowed.

## Setup

Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Optional: use a `.env` file for secrets or paths (see `.gitignore`); do not commit it.

## Run

```bash
source venv/bin/activate
python -m app.main
```

## Project layout

| Path | Purpose |
|------|--------|
| `app/main.py` | Application entry — implement capture, tracking, and pointer control here |
| `requirements.txt` | Python dependencies |
| `datasets/raw/` | Raw data (gitignored) |
| `models/trained/` | Trained model artifacts (gitignored) |

## Dependency overview

| Package | Role |
|---------|------|
| `opencv-python` | Webcam and image processing |
| `mediapipe` | Hand / pose landmarks |
| `numpy`, `pandas` | Arrays and data handling |
| `torch`, `torchvision` | Deep learning (if you add custom models) |
| `scikit-learn` | Classical ML / preprocessing |
| `pyautogui`, `pynput` | Move pointer and send clicks from Python |
| `matplotlib` | Debugging plots |
| `jupyter` | Notebooks for experiments |
| `filterpy` | Kalman filtering for smooth tracking |

## License

Add a `LICENSE` file when you choose a license for this project.
