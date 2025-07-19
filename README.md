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

## 🚀 Getting Started

### For Linux (Recommended)

This project includes a setup script to automate the installation process.

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/asup20cs/svgnim.git
    cd svgnim
    ```

2.  **Run the setup script:**
    This will create a virtual environment and install all necessary dependencies.
    ```sh
    chmod +x setup.sh
    ./setup.sh
    ```

3.  **Activate the environment and run the GUI:**
    ```sh
    source .venv/bin/activate
    python gui.py
    ```

### For Windows & Manual Setup

1.  **Prerequisites:**
    Ensure you have Python 3.13+ and [Manim](https://docs.manim.community/en/stable/installation.html) installed on your system.

2.  **Install Dependencies:**
    Clone the repository and install the required packages.
    ```sh
    git clone https://github.com/asup20cs/svgnim.git
    cd svgnim
    pip install .
    ```

3.  **Run the GUI:**
    ```sh
    python gui.py
    ```

---

## 🖥️ Building a Standalone Windows Executable

This project uses GitHub Actions to automatically build a standalone `.exe` file for Windows. This allows users to run the GUI without installing Python or any dependencies.

1.  **Trigger the Build:**
    - Go to the [Actions tab](https://github.com/asup20cs/svgnim/actions) in the GitHub repository.
    - In the left sidebar, click on **"Build Windows Executable"**.
    - Click the **"Run workflow"** button to start the build process.

2.  **Download the Application:**
    - Once the workflow is complete, an "Artifact" named **"SVGNim-Windows-Executable"** will be available for download on the workflow summary page.
    - Download the artifact, unzip it, and run `SVGNimGUI.exe`.

---

## 🖌️ Customizing Animations

Edit `svgs/animate_scene.py` to change how your SVGs are animated. Example:

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