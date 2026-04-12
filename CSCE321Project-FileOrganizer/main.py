import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from config import SOURCE_DIRECTORY, DESTINATION_DIRECTORY
from organizer import FileOrganizer

# Opens a folder picker
def browse_folder(entry_widget, default_path):
    path = filedialog.askdirectory(initialdir=default_path, title="Select folder")
    if path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, path)

# Organizes files from source dir into destination dir
def organize_files(source_dir, destination_dir):
    organizer = FileOrganizer(source_dir, destination_dir)
    organizer.organize()
    messagebox.showinfo("Organizer", f"Done, successfully moved files from:\n{source_dir}\nto\n{destination_dir}")

# Builds the main gui window
def build_gui():
    root = tk.Tk()
    root.title("File Organizer")
    root.resizable(False, False)

    tk.Label(root, text="Source directory:").grid(row=0, column=0, sticky="w", padx=10, pady=(10, 2))
    source_entry = tk.Entry(root, width=70)
    source_entry.grid(row=1, column=0, columnspan=2, padx=10)
    source_entry.insert(0, SOURCE_DIRECTORY)
    tk.Button(root, text="Browse...", command=lambda: browse_folder(source_entry, SOURCE_DIRECTORY)).grid(row=1, column=2, padx=10)

    tk.Label(root, text="Destination directory:").grid(row=2, column=0, sticky="w", padx=10, pady=(10, 2))
    destination_entry = tk.Entry(root, width=70)
    destination_entry.grid(row=3, column=0, columnspan=2, padx=10)
    destination_entry.insert(0, DESTINATION_DIRECTORY)
    tk.Button(root, text="Browse...", command=lambda: browse_folder(destination_entry, DESTINATION_DIRECTORY)).grid(row=3, column=2, padx=10)

    # Validates the source/destination paths
    def on_start():
        source_dir = source_entry.get().strip() or SOURCE_DIRECTORY
        destination_dir = destination_entry.get().strip() or DESTINATION_DIRECTORY

        if not Path(source_dir).is_dir():
            messagebox.showerror("Error", f"Source directory does not exist:\n{source_dir}")
            return
        
        # Asks to create a folder if the destination doesn't exists
        if not Path(destination_dir).exists():
            create = messagebox.askyesno("Create folder?", f"Destination does not exist:\n{destination_dir}\nCreate it?")
            if create:
                Path(destination_dir).mkdir(parents=True, exist_ok=True)
            else:
                return

        organize_files(source_dir, destination_dir)

    start_button = tk.Button(root, text="Start Organizing", width=20, command=on_start)
    start_button.grid(row=4, column=0, columnspan=3, pady=15)

    root.update_idletasks()
    x = (root.winfo_screenwidth() - root.winfo_width()) // 2
    y = (root.winfo_screenheight() - root.winfo_height()) // 2
    root.geometry(f"+{x}+{y}")

    root.mainloop()


def main():
    build_gui()


if __name__ == "__main__":
    main()
