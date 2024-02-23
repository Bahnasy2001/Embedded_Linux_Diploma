from pytube import YouTube
YouTube("https://youtu.be/GxDZR8A3QPM?si=vvh7SjZao8u-KMS8")\
.streams.filter(progressive=True, file_extension='mp4').first().download()