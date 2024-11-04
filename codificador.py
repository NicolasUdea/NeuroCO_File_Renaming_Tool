import os
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime

# Task names in order
tasks = ["ST1", "ST2", "DTAN", "DTF", "DTV", "DTS1", "DTS7", "DTCT"]

# Function to get the creation date of a file
def get_creation_date(file_path):
    return os.path.getctime(file_path)

# Function to rename files
def rename_files(video_folder, sensor_folder, group, participant, visit, skipped_tasks):
    # Get list of video files and sort by creation date
    video_files = sorted(os.listdir(video_folder), key=lambda x: get_creation_date(os.path.join(video_folder, x)))
    sensor_files = sorted(os.listdir(sensor_folder), key=lambda x: get_creation_date(os.path.join(sensor_folder, x)))

    # Filter out skipped tasks
    performed_tasks = [task for task in tasks if task not in skipped_tasks]

    # Check if the number of files matches the expected count
    expected_video_count = len(performed_tasks)
    expected_sensor_count = len(performed_tasks) * 2

    if len(video_files) != expected_video_count:
        messagebox.showerror("Error",
                             f"Expected {expected_video_count} video files, but found {len(video_files)}. Please check the folder.")
        return

    if len(sensor_files) != expected_sensor_count:
        messagebox.showerror("Error",
                             f"Expected {expected_sensor_count} sensor files, but found {len(sensor_files)}. Please check the folder.")
        return

    # Rename video files
    for i, task in enumerate(performed_tasks):
        old_name = video_files[i]
        new_name = f"Sub-{group}{participant}_ses_{visit}_task_{task}_video.mp4"
        os.rename(os.path.join(video_folder, old_name), os.path.join(video_folder, new_name))

    # Rename sensor files
    for i, task in enumerate(performed_tasks):
        for sensor in ["F6F2", "03F5"]:
            old_name = sensor_files[i * 2 + (0 if sensor == "F6F2" else 1)]
            new_name = f"Sub-{group}{participant}_ses_{visit}_task_{task}_{sensor}.csv"
            os.rename(os.path.join(sensor_folder, old_name), os.path.join(sensor_folder, new_name))

    messagebox.showinfo("Success", "Files renamed successfully!")

# Function to open folder dialog
def select_folder(entry):
    folder = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, folder)

# Function to start the renaming process
def start_renaming():
    group = group_var.get()
    participant = participant_var.get()
    visit = visit_var.get()
    video_folder = video_folder_entry.get()
    sensor_folder = sensor_folder_entry.get()
    skipped_tasks = [task for task, var in task_vars.items() if not var.get()]

    if not group or not participant or not visit or not video_folder or not sensor_folder:
        messagebox.showerror("Error", "All fields are required.")
        return

    rename_files(video_folder, sensor_folder, group, participant, visit, skipped_tasks)

# Create the main window
root = tk.Tk()
root.title("File Renaming Tool")

# Participant group
tk.Label(root, text="Participant Group:").grid(row=0, column=0, sticky=tk.W)
group_var = tk.StringVar()
group_menu = tk.OptionMenu(root, group_var, "CTR", "SAN", "DCL")
group_menu.grid(row=0, column=1, sticky=tk.W)

# Participant number
tk.Label(root, text="Participant Number:").grid(row=1, column=0, sticky=tk.W)
participant_var = tk.StringVar()
participant_entry = tk.Entry(root, textvariable=participant_var)
participant_entry.grid(row=1, column=1, sticky=tk.W)
tk.Label(root, text="e.g., participant 19 would be 019, participant 2 would be 002").grid(row=2, column=1, sticky=tk.W)

# Visit
tk.Label(root, text="Visit:").grid(row=3, column=0, sticky=tk.W)
visit_var = tk.StringVar()
visit_menu = tk.OptionMenu(root, visit_var, "V0", "V1", "V2")
visit_menu.grid(row=3, column=1, sticky=tk.W)

# Video folder
tk.Label(root, text="Video Folder:").grid(row=4, column=0, sticky=tk.W)
video_folder_entry = tk.Entry(root, width=50)
video_folder_entry.grid(row=4, column=1, sticky=tk.W)
video_folder_button = tk.Button(root, text="Browse", command=lambda: select_folder(video_folder_entry))
video_folder_button.grid(row=4, column=2, sticky=tk.W)

# Sensor folder
tk.Label(root, text="Sensor Folder:").grid(row=5, column=0, sticky=tk.W)
sensor_folder_entry = tk.Entry(root, width=50)
sensor_folder_entry.grid(row=5, column=1, sticky=tk.W)
sensor_folder_button = tk.Button(root, text="Browse", command=lambda: select_folder(sensor_folder_entry))
sensor_folder_button.grid(row=5, column=2, sticky=tk.W)

# Task checkboxes
tk.Label(root, text="Tasks not performed:").grid(row=6, column=0, sticky=tk.W)
task_vars = {}
for i, task in enumerate(tasks):
    var = tk.BooleanVar(value=True)
    task_vars[task] = var
    cb = tk.Checkbutton(root, text=task, variable=var)
    cb.grid(row=7 + i // 4, column=i % 4, sticky=tk.W)

# Start button
start_button = tk.Button(root, text="Start Renaming", command=start_renaming)
start_button.grid(row=11, column=0, columnspan=3)

# Run the main loop
root.mainloop()
