import os
import subprocess
import shutil
import sys
import argparse

# --- Configuration ---
MANIM_SCENE_FILE = "svgs/animate_scene.py"
MANIM_SCENE_NAME = "AnimateSVG"

def get_manim_output_path(quality_flag, scene_script_path, class_name):
    """Helper function to predict where Manim saves the rendered video."""
    res_folder = "480p15"  # default for -ql
    if quality_flag == "-qh":
        res_folder = "1080p60"
    elif quality_flag == "-qk":
        res_folder = "2160p60"
    
    # Get the script name without the 'svgs/' prefix and extension
    script_name_no_ext = os.path.splitext(os.path.basename(scene_script_path))[0]
    
    return os.path.join("media", "videos", script_name_no_ext, res_folder, f"{class_name}.mp4")

def main():
    parser = argparse.ArgumentParser(description="Batch render SVGs with Manim.")
    parser.add_argument("input_folder", help="Path to the folder containing SVG files.")
    parser.add_argument("output_folder", help="Path to the folder where rendered videos will be saved.")
    parser.add_argument("--svg_files", nargs='*', help="Specific SVG files to render. If not provided, all SVGs in the input folder will be rendered.")
    parser.add_argument("-q", "--quality", default="high", choices=["low", "high", "ultra"], help="Render quality (low, high, or ultra).")
    parser.add_argument("-f", "--force_rerender", action="store_true", help="Force re-render of existing videos.")
    args = parser.parse_args()

    INPUT_FOLDER = args.input_folder
    OUTPUT_FOLDER = args.output_folder
    rerender_all = args.force_rerender
    
    quality_map = {
        "low": "-ql",
        "high": "-qh",
        "ultra": "-qk"
    }
    QUALITY_FLAG = quality_map[args.quality]

    if rerender_all:
        print("Force re-render flag detected. All existing videos will be overwritten.")

    os.makedirs(INPUT_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    if not os.path.exists(MANIM_SCENE_FILE):
        print(f"Error: The Manim script '{MANIM_SCENE_FILE}' was not found.")
        return

    svg_files_to_render = args.svg_files
    if not svg_files_to_render:
        svg_files_to_render = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith('.svg')]

    if not svg_files_to_render:
        print(f"No SVG files found in the '{INPUT_FOLDER}' folder.")
        return

    print(f"Found {len(svg_files_to_render)} SVG(s). Checking which ones to render...")
    
    for svg_file in svg_files_to_render:
        output_filename = os.path.splitext(svg_file)[0] + ".mp4"
        final_video_path = os.path.join(OUTPUT_FOLDER, output_filename)

        if os.path.exists(final_video_path) and not rerender_all:
            print(f"✅ Skipping '{svg_file}': Video already exists. (Use --force_rerender to overwrite)")
            continue

        print(f"\n--- Rendering: {svg_file} ---")
        svg_path = os.path.join(INPUT_FOLDER, svg_file)
        
        command = ['manim', 'render', MANIM_SCENE_FILE, MANIM_SCENE_NAME, QUALITY_FLAG, svg_path]
        
        try:
            process = subprocess.run(command, check=True, capture_output=True, text=True)
            
            manim_output_file = get_manim_output_path(QUALITY_FLAG, MANIM_SCENE_FILE, MANIM_SCENE_NAME)

            if os.path.exists(manim_output_file):
                if os.path.exists(final_video_path):
                    os.remove(final_video_path)
                shutil.move(manim_output_file, final_video_path)
                print(f"👍 Success! Video saved to: {final_video_path}")
            else:
                print(f"❌ Error: Manim ran, but the output file was not found at {manim_output_file}")
                print("--- Manim Output ---")
                print(process.stdout)
                print(process.stderr)


        except subprocess.CalledProcessError as e:
            print(f"❌ Error: Manim failed to render {svg_file}.")
            print("--- Manim Error Log ---\n" + e.stderr + "\n-----------------------")
        except FileNotFoundError:
            print("❌ Error: 'manim' command not found. Is Manim installed correctly?")
            break
            
    media_dir = os.path.join("media", "videos", os.path.splitext(MANIM_SCENE_FILE)[0])
    if os.path.exists(media_dir):
        shutil.rmtree(media_dir)

    print("\nBatch rendering process finished.")

if __name__ == "__main__":
    main()
