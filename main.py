import tkinter
import customtkinter
from pytubefix import YouTube
from PIL import Image

def startdownload():
    try:
        yt_link = link.get()
        ytobject = YouTube(yt_link, on_progress_callback=on_progress)
        video = ytobject.streams.get_highest_resolution()
        video.download(output_path="C:/Users/ameen/Downloads")

        title.configure(text = ytobject.title, text_color = "green")
        finishLabel.configure(text = "")

        video.download()
        finishLabel.configure(text = "Downloaded! :)", text_color = "green")
    except:
        finishLabel.configure(text = "Download Error :(", text_color = "red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    progress_percentage.configure(text=per + '%')
    progress_percentage.update()

    #update progress bar
    progress_bar.set(float(percentage_of_completion/100))

#system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#Our app frames
app = customtkinter.CTk()
app.geometry("480x360")
app.title("Youtube video downloader")

#Adding UI elements
title = customtkinter.CTkLabel(app, text = "Paste a Youtube video URL")
title.pack(padx = 10, pady = 10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width = 350, height = 40, textvariable=url_var)
link.pack()

#finished Downloading
finishLabel = customtkinter.CTkLabel(app, text = "")
finishLabel.pack()

#progress percentage
progress_percentage = customtkinter.CTkLabel(app, text = "0%")
progress_percentage.pack()

progress_bar = customtkinter.CTkProgressBar(app, width = 400,progress_color="#CB0010")
progress_bar.set(0)
progress_bar.pack(padx = 10, pady = 10)

#Download button
img = Image.open("C:/Users/ameen/Downloads/image.png")
download = customtkinter.CTkButton(app, text= "Download",corner_radius=32,fg_color="transparent",hover_color="#CB0010",border_width=1,command=startdownload)
download.pack(padx = 10, pady = 10)

#Run applcation
app.mainloop()



