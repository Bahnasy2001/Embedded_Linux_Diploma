# from pytube import YouTube
# YouTube("https://youtu.be/GxDZR8A3QPM?si=vvh7SjZao8u-KMS8")\
# .streams.filter(progressive=True, file_extension='mp4').first().download()

from pytube import YouTube

# URL of the YouTube video to download
video_url = "https://youtu.be/GxDZR8A3QPM?si=vvh7SjZao8u-KMS8"

# Create a YouTube object using the video URL
yt = YouTube(video_url)

# Filter the streams to get only progressive (video + audio) MP4 files
# and select the first available stream
stream = yt.streams.filter(progressive=True, file_extension='mp4').first()

# Download the selected stream
stream.download()
