# SVGNim

**SVGNim** is a Python project for batch-rendering beautiful SVG animations using [Manim](https://www.manim.community/). Easily convert your SVG files into high-quality animated videos for presentations, tutorials, or creative projects.

---

## ✨ Features

- **Batch Render**: Automatically process all SVGs in a folder.
- **Custom Scenes**: Easily define your own Manim scenes for SVG animation.
- **High-Quality Output**: Supports multiple resolutions (e.g., 1080p60, 480p15).
- **Smart Skipping**: Skips already-rendered videos unless forced to re-render.
- **Organized Output**: Keeps your input SVGs and output videos neatly separated.

---

## 📦 Project Structure

```
svgnim/
│
├── main.py
├── pyproject.toml
├── README.md
├── .gitignore
├── svgs/
│   ├── animate_scene.py
│   ├── batch_render.py
│   ├── input/         # Place your SVG files here
│   ├── output/        # Rendered videos appear here
│   └── ...
└── ...
```

---

## 🚀 Quick Start

1. **Install Dependencies**

   Make sure you have Python 3.13+ and [Manim](https://docs.manim.community/en/stable/installation.html) installed.

   ```sh
   pip install -r requirements.txt
   # or, if using pyproject.toml:
   pip install .
   ```

2. **Add SVGs**

   Place your SVG files in `svgs/input/`.

3. **Render Animations**

   Run the batch renderer:

   ```sh
   cd svgs
   python batch_render.py
   ```

   - Videos will be saved in `svgs/output`.
   - To force re-render all videos, use:
     ```sh
     python batch_render.py -frr
     ```

---

## 🖥️ Packaging for Windows (GUI)

To create a standalone Windows executable (`.exe`) from the GUI, you can use PyInstaller. This allows you to run the application without needing to install Python or any dependencies on the target machine, with the exception of `ffmpeg`.

**1. Prerequisite: `ffmpeg`**

Manim relies on `ffmpeg` to render videos. PyInstaller does not bundle this. The end-user must:
   - **Download `ffmpeg`:** Get a static build from the [official ffmpeg website](https://ffmpeg.org/download.html).
   - **Make it accessible:** Place `ffmpeg.exe` in the same folder as the final `SVGNimGUI.exe` OR add the `ffmpeg/bin` directory to the system's PATH environment variable.

**2. Install PyInstaller**

In your project's virtual environment, install PyInstaller:
```sh
uv pip install pyinstaller
```

**3. Run the PyInstaller Command**

To create a Windows executable, you must run this command **on a Windows machine**. Open a command prompt, navigate to the project root, and execute:
```bash
pyinstaller --name SVGNimGUI --onedir --windowed --add-data "svgs/animate_scene.py;svgs" gui.py
```
- `--name`: Sets the executable's name.
- `--onedir`: Bundles the app into a single folder.
- `--windowed`: Hides the console window when the GUI runs.
- `--add-data`: Crucially includes the Manim scene script.

**4. Distribute the Application**

After PyInstaller finishes, a `dist/SVGNimGUI` folder will be created. To share the application, **zip and send this entire folder**. The user can run `SVGNimGUI.exe` from inside it.

---

## 🖌️ Customizing Animations

Edit `animate_scene.py` to change how your SVGs are animated. Example:

```python
class AnimateSVG(Scene):
    def construct(self):
        svg = SVGMobject("your_file.svg").scale(3).center()
        self.play(DrawBorderThenFill(svg), run_time=3)
        self.wait(1)
        # Add more animations here!
```

---

## 📁 Output Organization

- **Input SVGs:** `svgs/input`
- **Rendered Videos:** `svgs/output`

Intermediate files and logs are managed automatically.

---

## 🛠️ Requirements

- Python 3.13+
- [Manim](https://www.manim.community/) >= 0.19.0

---

## 📜 License

MIT License. See LICENSE for details.

---

## 🙏 Acknowledgements

- [Manim Community](https://www.manim.community/)
- Inspired by creative coding and open-source animation tools.

---

Happy animating! 🎬✨