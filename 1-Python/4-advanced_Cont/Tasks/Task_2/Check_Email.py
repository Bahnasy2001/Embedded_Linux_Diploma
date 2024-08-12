import pyautogui
import time
import webbrowser
# Adjust sleep times if needed to match the time required for your system to load the email application or website.
time.sleep(5)  # Time to switch to your email application or web browser
gmail_url = "https://mail.google.com/mail/u/0/#inbox"
webbrowser.get("C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s").open(gmail_url)
# Example coordinates - these need to be customized for your setup
# email_app_icon = (100, 200)  # Coordinates for the email app icon
first_unread_email = (482, 381)  # Coordinates for the first unread email
mark_as_read_button = (605, 256)  # Coordinates for the "Mark as Read" button

# Open the email application (if not already open)
# pyautogui.click(email_app_icon)
# time.sleep(5)  # Wait for the email application to open

# Click on the first unread email
pyautogui.click(first_unread_email)
time.sleep(2)  # Wait for the email to open

# Click on the button to mark the email as read (adjust this part based on your email application's UI)
pyautogui.click(mark_as_read_button)

print("Marked the email as read.")
