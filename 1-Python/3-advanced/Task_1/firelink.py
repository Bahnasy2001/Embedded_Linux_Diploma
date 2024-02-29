import webbrowser

def firelink(index):
    links = [
        "https://www.facebook.com/profile.php?id=100009364682555",
        "https://www.linkedin.com/in/hassan-bahnasy-7b4952253/",
        "https://twitter.com/bahnasy2001"
    ]
    webbrowser.get("C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s").open(links[index-1])


