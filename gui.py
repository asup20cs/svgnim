import tkinter as tk
from tkinter import filedialog, scrolledtext, font
import os
import subprocess
import threading

class ManimGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SVGNim GUI")
        self.geometry("800x600")

        # --- Define Fonts ---
        self.ui_font = font.Font(family="Segoe UI", size=10)
        self.button_font = font.Font(family="Segoe UI", size=10, weight="bold")
        self.console_font = font.Font(family="Consolas", size=11)

        self.input_folder = tk.StringVar()
        self.output_folder = tk.StringVar()
        self.quality_var = tk.StringVar(value="high")
        self.force_rerender = tk.BooleanVar()

        self.create_widgets()

    def create_widgets(self):
        # --- Folder Selection ---
        folder_frame = tk.Frame(self, padx=10, pady=10)
        folder_frame.pack(fill=tk.X)

        tk.Button(folder_frame, text="Select Input Folder", command=self.select_input_folder, font=self.ui_font).pack(side=tk.LEFT)
        tk.Label(folder_frame, textvariable=self.input_folder, font=self.ui_font).pack(side=tk.LEFT, padx=10)
        
        tk.Button(folder_frame, text="Select Output Folder", command=self.select_output_folder, font=self.ui_font).pack(side=tk.LEFT, padx=10)
        tk.Label(folder_frame, textvariable=self.output_folder, font=self.ui_font).pack(side=tk.LEFT, padx=10)

        # --- SVG List ---
        self.svg_listbox = tk.Listbox(self, selectmode=tk.MULTIPLE, font=self.ui_font)
        self.svg_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # --- Render Options ---
        options_frame = tk.Frame(self, padx=10, pady=10)
        options_frame.pack(fill=tk.X)

        tk.Label(options_frame, text="Quality:", font=self.ui_font).pack(side=tk.LEFT)
        quality_menu = tk.OptionMenu(options_frame, self.quality_var, "low", "high", "ultra")
        quality_menu.config(font=self.ui_font)
        quality_menu.pack(side=tk.LEFT)
        
        tk.Checkbutton(options_frame, text="Force Re-render", variable=self.force_rerender, font=self.ui_font).pack(side=tk.LEFT, padx=10)

        # --- Render Button ---
        tk.Button(self, text="Render Selected", command=self.start_render, font=self.button_font, bg="#4CAF50", fg="white").pack(pady=10, ipadx=10, ipady=5)

        # --- Output Console ---
        self.output_console = scrolledtext.ScrolledText(self, height=15, bg="black", fg="#FFFFFF", font=self.console_font, insertbackground="white")
        self.output_console.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def select_input_folder(self):
        folder_path = filedialog.askdirectory(title="Select the 'input' folder for your SVGs")
        if folder_path:
            self.input_folder.set(folder_path)
            self.populate_svg_list()

    def select_output_folder(self):
        folder_path = filedialog.askdirectory(title="Select the 'output' folder for your videos")
        if folder_path:
            self.output_folder.set(folder_path)

    def populate_svg_list(self):
        self.svg_listbox.delete(0, tk.END)
        folder_path = self.input_folder.get()
        if folder_path:
            try:
                svg_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.svg')]
                for svg_file in svg_files:
                    self.svg_listbox.insert(tk.END, svg_file)
            except Exception as e:
                self.output_console.insert(tk.END, f"Error reading folder: {e}\n")

    def start_render(self):
        if not self.input_folder.get():
            self.output_console.insert(tk.END, "Please select an input folder.\n")
            return
            
        if not self.output_folder.get():
            self.output_console.insert(tk.END, "Please select an output folder.\n")
            return

        selected_indices = self.svg_listbox.curselection()
        if not selected_indices:
            self.output_console.insert(tk.END, "Please select at least one SVG file to render.\n")
            return

        selected_files = [self.svg_listbox.get(i) for i in selected_indices]
        
        self.output_console.delete(1.0, tk.END)
        self.output_console.insert(tk.END, "--- Starting Render ---\n")
        
        render_thread = threading.Thread(target=self.run_render_script, args=(selected_files,))
        render_thread.daemon = True
        render_thread.start()

    def run_render_script(self, files_to_render):
        command = [
            'python', 
            'batch_render.py',
            self.input_folder.get(),
            self.output_folder.get(),
            '--quality', self.quality_var.get(),
        ]
        if self.force_rerender.get():
            command.append('--force_rerender')
        
        command.append('--svg_files')
        command.extend(files_to_render)

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True)

        for line in iter(process.stdout.readline, ''):
            self.output_console.insert(tk.END, line)
            self.output_console.see(tk.END)
        
        process.stdout.close()
        return_code = process.wait()

        if return_code == 0:
            self.output_console.insert(tk.END, "\n--- Render Finished Successfully ---\n")
        else:
            self.output_console.insert(tk.END, f"\n--- Render Failed (Exit Code: {return_code}) ---\n")


if __name__ == "__main__":
    app = ManimGUI()
    app.mainloop()
