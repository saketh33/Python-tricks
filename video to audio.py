mp4=eval(input("give your mp4 path"))
mp3=eval(input("give the path with .mp3 extension"))
import moviepy.editor
video=moviepy.editor.VideoFileClip(mp4)
audio=video.audio
audio.write_audiofile(mp3)
print("converetd successfully")