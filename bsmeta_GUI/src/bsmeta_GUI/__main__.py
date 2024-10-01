import tkinter as tk
from tkinter import filedialog, messagebox
import json

def export_to_json():
    data = {section: {entry_labels[section][i]: entry.get() for i, entry in enumerate(entries[section])} for section in entries}
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file)

def load_from_json():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            for section in entries:
                for i, entry in enumerate(entries[section]):
                    entry.delete(0, tk.END)
                    entry.insert(0, data.get(section, {}).get(entry_labels[section][i], ""))

def load_template():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, 'r') as json_file:
            template = json.load(json_file)
            create_fields(template, template)

def create_fields(template, data=None):
    global entries, entry_labels
    for widget in root.winfo_children():
        widget.destroy()
    
    # Recreate the menu
    create_menu()

    entry_labels = {section: list(template[section].keys()) for section in template}
    entries = {section: [] for section in template}
    
    for col, section in enumerate(template):
        section_frame = tk.Frame(root)
        section_frame.grid(row=0, column=col, padx=10, pady=10, sticky='n')

        tk.Label(section_frame, text=f"{section}:", font=('Arial', 12, 'bold')).pack(pady=(0, 10))
        
        for label in entry_labels[section]:
            tk.Label(section_frame, text=f"{label}:").pack(pady=(5, 0), anchor='w')
            entry = tk.Entry(section_frame, width=40)
            entry.pack(pady=(0, 10))
            if data:
                entry.insert(0, data[section].get(label, ""))
            entries[section].append(entry)
    
    button_frame = tk.Frame(root)
    button_frame.grid(row=1, column=0, columnspan=len(template), pady=(10, 20))

    export_button = tk.Button(button_frame, text="Export to JSON", command=export_to_json)
    export_button.pack(side=tk.LEFT, padx=5)
    
    load_button = tk.Button(button_frame, text="Load from JSON", command=load_from_json)
    load_button.pack(side=tk.LEFT, padx=5)

    # Update the window size
    root.update_idletasks()
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    root.geometry(f"{window_width}x{window_height}")

def create_menu():
    menu = tk.Menu(root)
    root.config(menu=menu)

    file_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Load New Template", command=load_template)

# Create the main window
root = tk.Tk()
root.title("Simple GUI")

# Create the menu
create_menu()

# Initialize with default fields
default_template = {
    "Section 1": {
        "Field 1": "",
        "Field 2": ""
    },
    "Section 2": {
        "Field 3": "",
        "Field 4": ""
    }
}
create_fields(default_template)

# Run the application
root.mainloop()