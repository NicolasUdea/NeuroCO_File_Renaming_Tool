import os
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime, timedelta

# Task names in order
tasks = ["ST1", "ST2", "DTAN", "DTF", "DTV", "DTS1", "DTS7", "DTCT"]

# Function to create test files
def create_test_files(folder, include_dtf=True):
    if not os.path.exists(folder):
        os.makedirs(folder)

    base_time = datetime.now()
    for i, task in enumerate(tasks):
        if task == "DTF" and not include_dtf:
            continue
        # Create video file
        video_filename = os.path.join(folder, f"video_{i+1}.mp4")
        with open(video_filename, 'w') as f:
            f.write("This is a test video file.")
        os.utime(video_filename, (base_time.timestamp(), base_time.timestamp()))

        # Create sensor files
        for sensor in ["F6F2", "03F5"]:
            sensor_filename = os.path.join(folder, f"sensor_{i+1}_{sensor}.csv")
            with open(sensor_filename, 'w') as f:
                f.write("This is a test sensor file.")
            os.utime(sensor_filename, (base_time.timestamp(), base_time.timestamp()))

        # Increment base time for next file
        base_time += timedelta(seconds=10)

# Function to generate scenario 1
def generate_scenario_1():
    video_folder = filedialog.askdirectory(title="Select Video Folder for Scenario 1")
    sensor_folder = filedialog.askdirectory(title="Select Sensor Folder for Scenario 1")
    if video_folder and sensor_folder:
        create_test_files(video_folder, include_dtf=True)
        create_test_files(sensor_folder, include_dtf=True)
        messagebox.showinfo("Success", "Scenario 1 files created successfully!")

# Function to generate scenario 2
def generate_scenario_2():
    video_folder = filedialog.askdirectory(title="Select Video Folder for Scenario 2")
    sensor_folder = filedialog.askdirectory(title="Select Sensor Folder for Scenario 2")
    if video_folder and sensor_folder:
        create_test_files(video_folder, include_dtf=False)
        create_test_files(sensor_folder, include_dtf=False)
        messagebox.showinfo("Success", "Scenario 2 files created successfully!")

# Create the main window
root = tk.Tk()
root.title("Test File Generator")

# Scenario 1 button
scenario_1_button = tk.Button(root, text="Generate Scenario 1", command=generate_scenario_1)
scenario_1_button.pack(pady=10)

# Scenario 2 button
scenario_2_button = tk.Button(root, text="Generate Scenario 2", command=generate_scenario_2)
scenario_2_button.pack(pady=10)

# Run the main loop
root.mainloop()
