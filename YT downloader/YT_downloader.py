from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download(url, save_path):
    try:
        yt_vid = YouTube(url)
        streams = yt_vid.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully! ")
    except Exception as exp:
        print(exp)

def open_file_dialog():
    save_folder = filedialog.askdirectory()
    if save_folder:
        print(f"Selected folder: {save_folder}")

    return save_folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    #above 'if' loop to ensure that the whole code is executed only when this code is run

    video_url = input("Enter a YouTube url: ")
    save_box = open_file_dialog()

    if save_box:
        print("Downloading, please wait...")
        download(video_url, save_box)
    else:
        print("Invalid save location.")