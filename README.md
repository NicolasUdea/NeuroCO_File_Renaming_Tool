# Codificador

This project provides a tool for renaming files in a specific format required by NeuroCO and GRUNECO. The tool includes a graphical user interface (GUI) for selecting folders and specifying parameters, as well as generating test files for different scenarios.

## Features

- Rename video and sensor files based on participant group, number, visit, and task.
- Generate test files for two scenarios:
  1. All tasks completed.
  2. One task skipped (e.g., DTF).

## Requirements

- Python 3.6 or higher
- `tkinter` library (usually included with Python)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/NicolasUdea/NeuroCO_File_Renaming_Tool.git
    cd NeuroCO_File_Renaming_Tool
    ```

2. (Optional) Create a virtual environment:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

3. Install required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the `codificador.py` script to open the file renaming tool:
    ```sh
    python codificador.py
    ```

2. Fill in the required fields:
    - **Participant Group**: Select the group (CTR, SAN, DCL).
    - **Participant Number**: Enter the participant number (e.g., 019 for participant 19).
    - **Visit**: Select the visit (V0, V1, V2).
    - **Video Folder**: Select the folder containing the video files.
    - **Sensor Folder**: Select the folder containing the sensor files.
    - **Tasks not performed**: Check the tasks that were not performed.

3. Click "Start Renaming" to rename the files.

## Generating Test Files

1. Run the `test.py` script to open the test file generator:
    ```sh
    python test.py
    ```

2. Select the scenario to generate test files:
    - **Scenario 1**: All tasks completed.
    - **Scenario 2**: One task skipped (e.g., DTF).

3. Select the folders for video and sensor files. The script will generate the test files in the selected folders.

## Notes

> [!TIP] 
> Ensure that the `tkinter` library is installed and properly configured on your system.

## License

This script is for use by NeuroCO and GRUNECO, created by [NicolasUdea](https://github.com/NicolasUdea).