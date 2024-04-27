#pip install pytube moviepy

from pytube import YouTube
import os
from moviepy.editor import *

def download_youtube_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(output_path=output_path)
        return os.path.join(output_path, stream.default_filename)
    except Exception as e:
        print("Error:", e)
        return None

def convert_to_mp3(video_file, output_path):
    try:
        audio = AudioFileClip(video_file)
        output_file = os.path.splitext(os.path.basename(video_file))[0] + ".mp3"
        output_path = os.path.join(output_path, output_file)
        audio.write_audiofile(output_path)
        # Eliminar el archivo de video después de la conversión
        os.remove(video_file)
        return True
    except Exception as e:
        print("Error:", e)
        return False

if __name__ == "__main__":
    youtube_url = input("Ingrese la URL de YouTube: ")
    output_directory = "MP3Downloaded"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    video_file = download_youtube_video(youtube_url, output_directory)
    if video_file:
        if convert_to_mp3(video_file, output_directory):
            print("¡Conversión exitosa!")
        else:
            print("La conversión falló.")
