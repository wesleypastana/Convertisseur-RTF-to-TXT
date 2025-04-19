import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from striprtf.striprtf import rtf_to_text
import os
import re
import math

# Application principale
class RTFConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Convertisseur RTF vers TXT")
        self.geometry("750x550")
        self.resizable(False, False)

        # Variables
        self.files_to_convert = []
        self.output_folder = ""
        self.auto_split = tk.BooleanVar(value=True)
        self.split_limit = tk.IntVar(value=100000)

        # Style
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TButton", font=("Segoe UI", 10), padding=8)
        style.configure("TLabel", font=("Segoe UI", 10))
        style.configure("Header.TLabel", font=("Segoe UI", 14, "bold"))

        # UI
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Convertisseur RTF → TXT", style="Header.TLabel").pack(pady=10)

        frame_buttons = ttk.Frame(self)
        frame_buttons.pack(pady=5)

        ttk.Button(frame_buttons, text="➕ Ajouter fichiers", command=self.add_files).grid(row=0, column=0, padx=5)
        ttk.Button(frame_buttons, text="📂 Choisir dossier de destination", command=self.choose_output_folder).grid(row=0, column=1, padx=5)
        ttk.Button(frame_buttons, text="🗑️ Effacer liste", command=self.clear_list).grid(row=0, column=2, padx=5)

        self.output_label = ttk.Label(self, text="Dossier : (non sélectionné)")
        self.output_label.pack(pady=5)

        self.file_listbox = tk.Listbox(self, height=12, width=90)
        self.file_listbox.pack(pady=10)

        options_frame = ttk.Frame(self)
        options_frame.pack(pady=10)

        ttk.Checkbutton(options_frame, text="Activer split automatique", variable=self.auto_split).grid(row=0, column=0, padx=5)
        ttk.Label(options_frame, text="Caractères max avant split :").grid(row=0, column=1, padx=5)
        ttk.Entry(options_frame, textvariable=self.split_limit, width=10).grid(row=0, column=2, padx=5)

        self.convert_button = ttk.Button(self, text="🚀 Démarrer Conversion", command=self.start_conversion)
        self.convert_button.pack(pady=10)

        self.progress = ttk.Progressbar(self, length=650, mode='determinate')
        self.progress.pack(pady=5)

        self.status_label = ttk.Label(self, text="En attente...")
        self.status_label.pack(pady=5)

    def add_files(self):
        filenames = filedialog.askopenfilenames(filetypes=[("Fichiers RTF", "*.rtf")])
        for file in filenames:
            if file not in self.files_to_convert:
                self.files_to_convert.append(file)
                self.file_listbox.insert(tk.END, os.path.basename(file))

    def choose_output_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.output_folder = folder_selected
            self.output_label.config(text=f"Dossier : {self.output_folder}")

    def clear_list(self):
        self.files_to_convert.clear()
        self.file_listbox.delete(0, tk.END)
        self.progress['value'] = 0
        self.status_label.config(text="Liste vidée.")

    def split_large_file(self, filepath, text):
        filename = os.path.basename(filepath).replace('.rtf', '')
        num_parts = math.ceil(len(text) / self.split_limit.get())
        part_size = len(text) // num_parts

        for i in range(num_parts):
            start = i * part_size
            end = start + part_size if i < num_parts - 1 else len(text)
            part_text = text[start:end]

            output_path = os.path.join(self.output_folder, f"{filename}_Part{i+1}.txt")
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(part_text)

    def start_conversion(self):
        if not self.files_to_convert:
            messagebox.showwarning("Erreur", "Aucun fichier sélectionné.")
            return

        if not self.output_folder:
            messagebox.showwarning("Erreur", "Choisis d'abord le dossier de destination.")
            return

        total_files = len(self.files_to_convert)
        self.progress['maximum'] = total_files
        self.progress['value'] = 0

        for idx, filepath in enumerate(self.files_to_convert, 1):
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                rtf_content = file.read()

            text = rtf_to_text(rtf_content)
            text = re.sub(r'(\w)([A-ZÀ-Ü])', r'\1 \2', text)

            if self.auto_split.get() and len(text) > self.split_limit.get():
                self.split_large_file(filepath, text)
            else:
                output_path = os.path.join(self.output_folder, os.path.basename(filepath).replace('.rtf', '.txt'))
                with open(output_path, 'w', encoding='utf-8') as file:
                    file.write(text)

            self.progress['value'] = idx
            self.status_label.config(text=f"{idx}/{total_files} convertis : {os.path.basename(filepath)}")
            self.update()

        messagebox.showinfo("Terminé", f"{total_files} fichiers convertis avec succès !")
        self.status_label.config(text="✅ Conversion terminée.")


# Démarrage de l'application
if __name__ == "__main__":
    app = RTFConverterApp()
    app.mainloop()
