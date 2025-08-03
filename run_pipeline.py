import os
import subprocess

MESHROOM_BIN = "/opt/ml/code/meshroom_bin"
INPUT_IMAGES = "/opt/ml/input/data/images"
OUTPUT_FOLDER = "/opt/ml/output"

def run_meshroom():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    command = [
        os.path.join(MESHROOM_BIN, "meshroom_photogrammetry"),
        "--input", INPUT_IMAGES,
        "--output", OUTPUT_FOLDER
    ]
    print("Running:", " ".join(command))
    subprocess.run(command, check=True)

if __name__ == "__main__":
    run_meshroom()
    print("3D reconstruction complete. Output is in:", OUTPUT_FOLDER)
