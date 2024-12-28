import tkinter as tk
from tkinter import messagebox

def calculate_factorial():
    try:
        # Get the number from the entry field
        n = int(number_entry.get())
        
        # Check for negative numbers
        if n < 0:
            messagebox.showerror("Error", "Please enter a non-negative integer!")
            return
            
        # Calculate factorial
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
            
        # Update result label
        result_label.config(text=f"The factorial of {n} is: {factorial}")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer!")

# Create the main window
window = tk.Tk()
window.title("Factorial Calculator")
window.geometry("400x200")

# Create and pack the input label
input_label = tk.Label(window, text="Enter an integer N:", font=("Arial", 12))
input_label.pack(pady=10)

# Create and pack the entry field
number_entry = tk.Entry(window, font=("Arial", 12))
number_entry.pack(pady=5)

# Create and pack the calculate button
calc_button = tk.Button(window, text="Calculate Factorial", command=calculate_factorial, font=("Arial", 12))
calc_button.pack(pady=10)

# Create and pack the result label
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Start the main loop
window.mainloop()