import tkinter as tk
from tkinter import messagebox
import time

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        self.master.resizable(False, False)
        
        self.time_left = 0
        self.timer_id = None
        
        self.create_widgets()

    def create_widgets(self):
        # Create the labels and buttons
        self.time_label = tk.Label(self.master, text="Time left: 0")
        self.time_label.pack(padx=20, pady=10)

        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack(padx=20, pady=5)

        self.pause_button = tk.Button(self.master, text="Pause", state=tk.DISABLED, command=self.pause_timer)
        self.pause_button.pack(padx=20, pady=5)

        self.reset_button = tk.Button(self.master, text="Reset", state=tk.DISABLED, command=self.reset_timer)
        self.reset_button.pack(padx=20, pady=5)

    def start_timer(self):
        # Create a new window for the user to enter the time
        time_window = tk.Toplevel(self.master)
        time_window.title("Enter time")
        time_window.geometry("200x100")
        time_window.resizable(False, False)

        # Create a label and an entry widget
        time_label = tk.Label(time_window, text="Enter the number of seconds to count down:")
        time_label.pack(padx=20, pady=10)

        time_entry = tk.Entry(time_window)
        time_entry.pack(padx=20, pady=5)

        # Create a button to start the timer
        start_button = tk.Button(time_window, text="Start", command=lambda: self.start_timer_callback(time_entry, time_window))
        start_button.pack(padx=20, pady=5)

    def start_timer_callback(self, time_entry, time_window):
        # Get the time from the entry widget and close the window
        try:
            self.time_left = int(time_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of seconds.")
            return

        time_window.destroy()

        # Disable the start button and enable the pause and reset buttons
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.NORMAL)

        # Start the timer
        self.run_timer()

    def run_timer(self):
        # Update the time label
        self.time_label.config(text=f"Time left: {self.time_left}")

        # Decrement the time left
        self.time_left -= 1

        # Check if the timer is done
        if self.time_left < 0:
            self.time_left = 0
            self.pause_timer()
            messagebox.showinfo("Countdown Timer", "Time is up!")

        # Set a timer to update again in 1 second
        self.timer_id = self.master.after(1000, self.run_timer)

    def pause_timer(self):
        # Stop the timer
        self.master.after_cancel(self.timer_id)
        self.timer_id = None

        # Disable the pause button and enable the start button
        self.pause_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
    
    def reset_timer(self):
        # Stop the timer
        self.master.after_cancel(self.timer_id)
        self.timer_id = None

        # Reset the time left and update the time label
        self.time_left = 0
        self.time_label.config(text="Time left: 0")

        # Disable the pause and reset buttons and enable the start button
        self.pause_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

