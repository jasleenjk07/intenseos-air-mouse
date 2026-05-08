from core.vision.camera import CameraStream

def main():
    camera = CameraStream()
    camera.start_stream()

if __name__ == "__main__":
    main()