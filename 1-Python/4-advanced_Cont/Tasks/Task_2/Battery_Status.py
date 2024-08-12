from plyer import notification
import psutil
battery = psutil.sensors_battery()
percent = battery.percent

# Print the battery percentage
print(f"Battery percentage: {percent}%")

# Send the notification
notification.notify(
    title="Battery Percentage",
    message=f"{percent}% remaining",
    timeout=10  # Duration in seconds
)