
# import pyttsx3 # A text-to-speech library I plan to play around with later on
# import pytesseract # A library which can help us with retrieving in-game screen info
# import pyautogui # Some extra GUI tools we could use
import tkinter as tk
import subprocess
import time


""" Function to check if StarCraft 2 is running"""
def isStarCraftRunning():
    # Check the list of running processes for StarCraft II
    process_list = subprocess.Popen(
        ["tasklist"], stdout=subprocess.PIPE, text=True)
    output = process_list.communicate()[0]
    return any("SC2" in line or "StarCraft" in line for line in output.splitlines())


"""A function for updating the resource display"""
def updateResourceDisplay(window, canvas, resourcesDict):
    if isStarCraftRunning():
        canvas.delete("resource_text")
        # Define initial coordinates for the text
        x = 10
        y = 10
        # Iterate through the resourcesDict dictionary
        for resource, value in resourcesDict.items():
            # Create and add a text element to the canvas for each resource
            canvas.create_text(
                x,
                y,
                text=f"{resource}: {value}",
                fill="white",
                font=("Helvetica", 12),
                anchor="w",
                tags="resource_text"
            )
            # Adjust the y-coordinate for the next resource entry
            y += 20
        window.after(100, updateResourceDisplay, window, canvas, resourcesDict)
    else:
        canvas.delete("resource_text")
        # Add the exit message to the canvas
        canvas.itemconfig("status_message", text="Closing SC2 Overlay...")
        canvas.itemconfig("status_message", state="normal")
        window.after(3000, window.destroy)
        print("StarCraft II has ended.")


"""Main method"""
def main():

    # Print to console that overlay has begun
    print("StarCraft II has started.")

    # Initialize in-game resource count
    acquiredResources = {
        "minerals": 0,
        "workers": 0,  # SCVs, Probes, or Drones
        "supply": 0,  # Supply Depots, Pylons, Overlords
        "vespene gas": 0,
        "units": 0,
        "upgrades": 0
    }

    # Create the main window
    window = tk.Tk()
    window.title("StarCraft 2 Overlay")

    # Create a black canvas
    canvas = tk.Canvas(window, width=400, height=100, bg="black")
    canvas.pack()

    # Add the boot-up message
    canvas.create_text(
        200,
        50,
        text="Starting SC2 Overlay...",
        fill="white",
        font=("Helvetica", 16),
        anchor="center",
        tags="status_message"
    )

    # Center the window on the screen
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Start checking if StarCraft 2 is running
    window.after(3000, lambda: [canvas.itemconfig(
        "status_message", state="hidden"), updateResourceDisplay(window, canvas, acquiredResources)])

    # Run the GUI main loop
    window.mainloop()


# Run the program
if __name__ == "__main__":
    main()
