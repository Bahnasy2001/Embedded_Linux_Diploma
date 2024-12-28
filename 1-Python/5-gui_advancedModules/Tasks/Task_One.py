import tkinter as tk
import time
import math


def update_clock():
    """Update the digital clock every second."""
    current_time = time.strftime('%H:%M:%S')
    time_label.config(text=current_time)
    root.after(1000, update_clock)


def update_gauge(value):
    """Update the gauge needle to point to the current value."""
    canvas.delete("needle")
    angle = (value - min_val) / (max_val - min_val) * 300  # Map value to 300° range
    angle_rad = math.radians(240 - angle)  # Start at 240° (top left) and sweep to -60°
    needle_x = center_x + needle_length * math.cos(angle_rad)
    needle_y = center_y - needle_length * math.sin(angle_rad)
    canvas.create_line(center_x, center_y, needle_x, needle_y, fill="red", width=3, tag="needle")
    value_label.config(text=str(value))


# Initialize the Tkinter application
root = tk.Tk()
root.title("Gauge with Gray Background and Black Design")

# Define gauge parameters
min_val = 0
max_val = 1000
current_value = 609
radius = 120
center_x, center_y = 200, 200
needle_length = radius - 20

# Create a frame for layout
frame = tk.Frame(root, bg="gray")
frame.pack(padx=20, pady=20)

# Create a digital clock on the left
time_label = tk.Label(frame, text="", font=("Arial", 20), bg="gray", fg="black")
time_label.grid(row=0, column=0, padx=20, pady=10, sticky="n")
update_clock()

# Create a canvas for the gauge
canvas = tk.Canvas(frame, width=400, height=400, bg="gray", highlightthickness=0)
canvas.grid(row=0, column=1, padx=10, pady=10)

# Draw the gauge background (circle)
canvas.create_oval(
    center_x - radius, center_y - radius, center_x + radius, center_y + radius,
    fill="black", outline="gray"
)

# Add major and minor tick marks for 300° range
for i in range(0, 101):  # 101 ticks for a range of 0-1000
    angle = math.radians(240 - i * 3)  # Map 300° range: 240° to -60°
    outer_x = center_x + radius * math.cos(angle)
    outer_y = center_y - radius * math.sin(angle)

    if i % 10 == 0:  # Major tick (for values like 0, 100, 200, ...)
        inner_x = center_x + (radius - 15) * math.cos(angle)
        inner_y = center_y - (radius - 15) * math.sin(angle)
        canvas.create_text(
            center_x + (radius - 35) * math.cos(angle),
            center_y - (radius - 35) * math.sin(angle),
            text=str(i * 10), fill="white", font=("Arial", 10)
        )
    else:  # Minor tick
        inner_x = center_x + (radius - 10) * math.cos(angle)
        inner_y = center_y - (radius - 10) * math.sin(angle)

    canvas.create_line(outer_x, outer_y, inner_x, inner_y, fill="white", width=1)

# Add a circular center for the gauge needle pivot
canvas.create_oval(
    center_x - 10, center_y - 10, center_x + 10, center_y + 10,
    fill="white", outline="white"
)

# Add a label for the value being pointed to
value_label = tk.Label(frame, text=str(current_value), font=("Arial", 16), bg="gray", fg="black")
value_label.grid(row=1, column=1, pady=10)

# Add status indicator below the clock
status_label = tk.Label(frame, text="Arduino RS232 okay", font=("Arial", 12), bg="gray", fg="green")
status_label.grid(row=1, column=0)

# Update the gauge pointer
update_gauge(current_value)

# Run the Tkinter event loop
root.mainloop()
