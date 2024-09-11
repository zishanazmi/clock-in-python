import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("Simple GUI Clock")

# Set the window size and background color
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg="#1A1A1A")

# Create a label for displaying the time
clock_label = tk.Label(root, font=("Helvetica", 48, "bold"), bg="#1A1A1A", fg="#00FF00")
clock_label.pack(pady=20)

# Create a label for displaying the date
date_label = tk.Label(root, font=("Helvetica", 24, "bold"), bg="#1A1A1A", fg="#FFFFFF")
date_label.pack(pady=10)

# Function to update the time and date on the labels
def update_time():
    # Current time
    current_time = time.strftime("%H:%M:%S %p")  # 12-hour format with AM/PM
    clock_label.config(text=current_time)

    # Current date
    current_date = time.strftime("%A, %B %d, %Y")  # Full weekday, month name, day, year
    date_label.config(text=current_date)

    # Refresh every second
    clock_label.after(1000, update_time)

# Start the clock
update_time()

# Run the tkinter event loop
root.mainloop()
