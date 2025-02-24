import os
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_directory():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        directory_var.set(folder_selected)
        list_files()

def list_files():
    file_listbox.delete(0, tk.END)
    directory = directory_var.get()
    if os.path.isdir(directory):
        for filename in os.listdir(directory):
            file_listbox.insert(tk.END, filename)

def rename_files():
    directory = directory_var.get()
    text_to_replace = find_text_var.get()
    replacement_text = replace_text_var.get()
    
    if not os.path.isdir(directory):
        messagebox.showerror("Error", "Invalid directory selected")
        return
    
    if not text_to_replace:
        messagebox.showerror("Error", "Enter text to find")
        return
    
    renamed_files = []
    for filename in os.listdir(directory):
        old_file_path = os.path.join(directory, filename)
        if os.path.isfile(old_file_path) and text_to_replace in filename:
            new_file_name = filename.replace(text_to_replace, replacement_text)
            new_file_path = os.path.join(directory, new_file_name)
            os.rename(old_file_path, new_file_path)
            renamed_files.append(f"{filename} -> {new_file_name}")
    
    list_files()
    messagebox.showinfo("Success", "Files renamed successfully!\n\n" + "\n".join(renamed_files))

# GUI Setup
root = tk.Tk()
root.title("Specific Text Renamer By SOUL HACKER")
root.geometry("600x500")
root.configure(bg="#ecf0f1")
root.minsize(500, 400)
root.maxsize(800, 600)

directory_var = tk.StringVar()
find_text_var = tk.StringVar()
replace_text_var = tk.StringVar()

title_label = tk.Label(root, text="File Renamer", font=("Arial", 16, "bold"), bg="#34495e", fg="white", pady=10)
title_label.pack(fill=tk.X)

tk.Label(root, text="Select Folder:", bg="#ecf0f1", font=("Arial", 12)).pack(pady=5)
browse_frame = tk.Frame(root, bg="#ecf0f1")
browse_frame.pack(pady=5, fill=tk.X, padx=20)

browse_button = tk.Button(browse_frame, text="Browse", command=browse_directory, bg="#3498db", fg="white", font=("Arial", 10))
browse_button.pack(side=tk.RIGHT)

directory_entry = tk.Entry(browse_frame, textvariable=directory_var, width=50, font=("Arial", 10))
directory_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)

tk.Label(root, text="Find Text:", bg="#ecf0f1", font=("Arial", 12)).pack(pady=5)
find_entry = tk.Entry(root, textvariable=find_text_var, width=40, font=("Arial", 10))
find_entry.pack(pady=5)

tk.Label(root, text="Replace With:", bg="#ecf0f1", font=("Arial", 12)).pack(pady=5)
replace_entry = tk.Entry(root, textvariable=replace_text_var, width=40, font=("Arial", 10))
replace_entry.pack(pady=5)

rename_button = tk.Button(root, text="Rename Files", command=rename_files, bg="#2ecc71", fg="white", font=("Arial", 12, "bold"), pady=5)
rename_button.pack(pady=10)

file_list_frame = tk.Frame(root, bg="#ecf0f1")
file_list_frame.pack(pady=5, expand=True, fill=tk.BOTH)

tk.Label(file_list_frame, text="Files in Directory:", bg="#ecf0f1", font=("Arial", 12)).pack(pady=5)
file_listbox = tk.Listbox(file_list_frame, width=60, height=10, font=("Arial", 10))
file_listbox.pack(pady=5, expand=True, fill=tk.BOTH)

root.mainloop()
