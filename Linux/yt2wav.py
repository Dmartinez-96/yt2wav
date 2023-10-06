import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube
import os
import subprocess
import sys
import platform

# Determine the null device based on the operating system
if platform.system() == "Windows":
    null_device = "nul"
else:
    null_device = "/dev/null"

if __name__ == "__main__":
    executable_dir = os.path.dirname(sys.executable)
    #ffmpeg_path = os.path.join(executable_dir, "ffmpeg")
    ffmpeg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ffmpeg")
    def download_and_convert():
        url = entry_url.get()
        output_directory = entry_directory.get()
        if not output_directory or not os.path.exists(output_directory):
            output_directory = filedialog.askdirectory()
            entry_directory.delete(0, tk.END)
            entry_directory.insert(0, output_directory)
        if not output_directory:
            return
        yt = YouTube(url)

        stream = yt.streams.get_highest_resolution()
        if not stream:
            messagebox.showerror("Error", "No WAV stream available for this video.")
            return

        stream.download(output_path=output_directory)
        file_name = stream.default_filename
        wav_file_name = file_name.split('.')[0] + '.wav'
        ffmpeg_command = [ffmpeg_path, "-y", "-i", file_name, '-f', 'wav', wav_file_name]
        os.chdir(output_directory)
        try:
            # Redirect the subprocess's stdout and stderr to the null device
            with open(null_device, 'w') as null_out:
                subprocess.run(ffmpeg_command, check=True, stdout=null_out, stderr=subprocess.STDOUT)
            os.remove(file_name)
            messagebox.showinfo("Conversion Complete", "Audio conversion completed successfully!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def browse_directory():
        selected_directory = filedialog.askdirectory()
        entry_directory.delete(0, tk.END)
        entry_directory.insert(0, selected_directory)
    
    def on_entry_click(event):
        """Function to handle behavior when an entry is clicked."""
        if entry_url.get() == 'Enter YouTube URL':
            entry_url.delete(0, tk.END)
            entry_url.insert(0, '')
            entry_url.config(fg='black')

        if entry_directory.get() == 'Enter output directory':
            entry_directory.delete(0, tk.END)
            entry_directory.insert(0, '')
            entry_directory.config(fg='black')


    root = tk.Tk()
    root.title("YouTube Audio Downloader")
    root.configure(bg="black")
    label_url = tk.Label(root, text="YouTube Video URL:", bg="dark gray")
    label_url.pack()
    
    entry_url = tk.Entry(root, bg="dark gray", highlightbackground="gray")
    entry_url.insert(0, 'Enter YouTube URL')
    entry_url.bind('<FocusIn>', on_entry_click)
    entry_url.pack()
    label_directory = tk.Label(root, text="Output Directory:", bg="dark gray")
    label_directory.pack()
    entry_directory = tk.Entry(root, bg="dark gray", highlightbackground="gray")
    entry_directory.insert(0, 'Enter output directory')
    entry_directory.bind('<FocusIn>', on_entry_click)
    entry_directory.pack()
    
    button_browse = tk.Button(root, text="Browse", command=browse_directory, bg="dark gray", fg="black")
    button_browse.pack()
    button_download = tk.Button(root, text="Download and Convert", command=download_and_convert, bg="dark gray", fg="black")
    button_download.pack()
    
    root.mainloop()
