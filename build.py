import subprocess
import imageio_ffmpeg
import os
import platform

def main():
    """
    Runs the PyInstaller command to build the SVGNim GUI for Windows.
    This script automatically finds and bundles the correct ffmpeg executable.
    """
    if platform.system() != "Windows":
        print("This build script is intended to be run on Windows (e.g., via GitHub Actions).")
        # We can still try to run it for testing purposes on other OSes
        # but the final artifact should be built on Windows.

    print("--- Starting SVGNim Build Process ---")

    # 1. Find the path to the ffmpeg executable
    try:
        ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
        print(f"Found ffmpeg executable at: {ffmpeg_path}")
    except Exception as e:
        print(f"Error: Could not find ffmpeg. Please ensure 'imageio-ffmpeg' is installed correctly. {e}")
        return

    # 2. Define the PyInstaller command
    command = [
        'pyinstaller',
        '--name', 'SVGNimGUI',
        '--onedir',
        '--windowed',
        '--add-data', f'svgs/animate_scene.py{os.pathsep}svgs',
        '--add-binary', f'{ffmpeg_path}{os.pathsep}.',
        'gui.py'
    ]

    print(f"\nRunning command:\n{' '.join(command)}\n")

    # 3. Run the command
    try:
        subprocess.run(command, check=True)
        print("\n--- PyInstaller build completed successfully! ---")
        print("You can find the output in the 'dist' folder.")
    except subprocess.CalledProcessError as e:
        print(f"\n--- Error: PyInstaller build failed. ---")
        print(f"Return code: {e.returncode}")
    except FileNotFoundError:
        print("\n--- Error: 'pyinstaller' command not found. ---")
        print("Please ensure PyInstaller is installed in your environment.")

if __name__ == "__main__":
    main()
