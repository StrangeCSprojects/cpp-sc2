
# import pyttsx3 # A text-to-speech library I plan to play around with later on
# import pytesseract # A library which can help us with retrieving in-game screen info
# import pyautogui # Some extra GUI tools we could use
import tkinter as tk
from tkinter import ttk
import subprocess
import psutil
import threading
import time
import os
import csv


class BuildOrderOverlay(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.title("SC2 Build Order Overlay")

        # Set the window to be always on top
        self.attributes("-topmost", True)
       
        # Set window transparency (0.0: fully transparent, 1.0: fully opaque)
        self.attributes('-alpha', 0.9)

        # Create the table headers
        columns = ("Time", "Unit/Building")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")

        # Define the column headings and widths
        self.tree.heading("Time", text="Time")
        self.tree.heading("Unit/Building", text="Unit/Building")

        self.tree.column("Time", width=60)
        self.tree.column("Unit/Building", width=150)

        # Insert data
        build_order = [
            ("0:17", "Supply Depot"),
            ("0:39", "Barracks"),
            ("0:43", "Refinery"),
            ("1:27", "Marine"),
            ("1:42", "Command Center"),
            ("1:57", "Supply Depot"),
            ("2:20", "Barracks"),
            ("2:20", "Factory"),
            
            # ... add more as needed
        ]

        for item in build_order:
            self.tree.insert("", "end", values=item)

        self.tree.pack(pady=20)

class LiveBuildOrderOverlay(tk.Tk):
    def __init__(self):

        super().__init__()

        # Set the window title
        self.title("SC2 Build Order Overlay")

        # Set the window to be always on top
        self.attributes("-topmost", True)
       
        # Set window transparency (0.0: fully transparent, 1.0: fully opaque)
        self.attributes('-alpha', 0.9)

        # Create the table headers
        columns = ("Time", "Unit/Building")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")

        # Define the column headings and widths
        self.tree.heading("Time", text="Time")
        self.tree.heading("Unit/Building", text="Unit/Building")

        self.tree.column("Time", width=60)
        self.tree.column("Unit/Building", width=150)

        # Insert data
        build_order = [
            # ... add more as needed
        ]

        for item in build_order:
            self.tree.insert("", "end", values=item)

        self.tree.pack(pady=20)

        self.csv_filepath = "build/bin/output.csv"
        self.last_check_time = os.path.getmtime(self.csv_filepath)
        self.poll_csv()

    def has_file_changed(self, filepath, last_check_time):
        """
        Check if the file at 'filepath' has been modified since 'last_check_time'.
        Returns (has_changed, new_check_time).
        """
        current_time = os.path.getmtime(filepath)
        return current_time > last_check_time, current_time
    
    def update_table_from_csv(self, csv_filepath):
        with open(csv_filepath, "r") as file:
            rows = list(csv.reader(file))

        # Assuming first row is headers
        headers = rows[0]
        for col, header in enumerate(headers):
            self.tree.heading(col, text=header)

        # Remove old items and add new items
        for row in self.tree.get_children():
            self.tree.delete(row)

        for row_data in rows[1:]:
            self.tree.insert("", "end", values=row_data)
    def poll_csv(self):
        changed, new_time = self.has_file_changed(self.csv_filepath, self.last_check_time)
        if changed:
            self.update_table_from_csv(self.csv_filepath)
            self.last_check_time = new_time

        # Poll every 5 seconds (5000 milliseconds)
        self.after(5000, self.poll_csv)
    
def check_for_sc2():
    while True:
        
        process_names = [proc.name().lower() for proc in psutil.process_iter(attrs=['name'])]

        print("Checking for sc2 process...")

        if "sc2_x64.exe" in process_names:
            print("Process found!")
            app = BuildOrderOverlay()
            app2 = LiveBuildOrderOverlay()
            app.mainloop()
            app2.mainloop()
            break  # End this function once overlay is launched

        time.sleep(1)  # Wait every 5 seconds before checking again
if __name__ == "__main__":
    check_for_sc2()