import datetime
from tkinter import *
from tkinter import filedialog
from tkVideoPlayer import TkinterVideo


def update_duration(event):
    end_time["text"] = str(datetime.timedelta(seconds=vid_player.duration()))
    progress_slider["to"] = vid_player.duration()

def update_scale(event):
    progress_slider.set(vid_player.current_duration())

def load_video():
    file_path = filedialog.askopenfilename()

    if file_path:
        vid_player.load(file_path)
        play_pause_btn['state'] = ACTIVE
        play_pause_btn['bg'] = 'green'
        play_pause_btn['fg'] = 'white'
        progress_slider.config(to=0, from_=0)
        progress_slider.set(0)
        play_pause_btn["text"] = "Play"


def seek(value):
    vid_player.seek(int(value))


def skip(value: int):
    """ skip seconds """
    vid_player.skip_sec(value)
    progress_slider.set(progress_slider.get() + value)


def play_pause():
    if vid_player.is_paused():
        vid_player.play()
        play_pause_btn["text"] = "Pause"
        play_pause_btn["bg"] = "gray"
        
    else:
        vid_player.pause()
        play_pause_btn["text"] = "Play"
        play_pause_btn["bg"] = "green"

def video_ended(event):
    progress_slider.set(progress_slider["to"])
    play_pause_btn["text"] = "Play"
    
def StopVideo():
    # play_pause_btn['state'] = DISABLED
    play_pause_btn['bg'] = 'white'
    vid_player.stop()    
    
def exitWindow():
    root.destroy()    
    root.quit()    
    
root = Tk()
root.title("Tkinter media")
root.title("Video Player")
root.geometry("800x550")
root.minsize(1000,500)
root.configure(bg="#116562")

vid_player = TkinterVideo(scaled=True, pre_load=False, master=root)
vid_player.pack(expand=True, fill="both")

load_btn = Button(root, text='Select Video',font="none 10",bg='#4A7A8C',fg='white',activebackground='white',activeforeground='#4A7A8C',width=16, command=load_video)
load_btn.pack(side="left",padx=10, pady=5,anchor="w")


play_pause_btn = Button(root, text='PLAY',bg='green',fg='white',font="none 10 ",activebackground='white',activeforeground='green',width=16, command=play_pause)
play_pause_btn.pack(side="left",padx=10, pady=5,anchor="w")

b4 = Button(root, text='STOP',bg='black',fg='white',font="none 10",activebackground='white',activeforeground='black',width=16, command= StopVideo)
b4.pack(side=LEFT,padx=10, pady=5,anchor="w")

skip_plus_5sec = Button(root, text="-5s",bg='#4a7abc',fg='white', command=lambda: skip(-5))
skip_plus_5sec.pack(side="left",padx=10, pady=5,anchor="w")

progress_slider = Scale(root, from_=0, to=0, orient="horizontal",background='#116562', fg='white', troughcolor='#73B5FA', activebackground='#1065BF', command=seek)
progress_slider.pack(side="left", fill="x", expand=True)

end_time = Label(root, text=str(datetime.timedelta(seconds=0)),bg="#116562",fg='white')
end_time.pack(side="left")

vid_player.bind("<<Duration>>", update_duration)
vid_player.bind("<<SecondChanged>>", update_scale)
vid_player.bind("<<Ended>>", video_ended )

skip_plus_5sec = Button(root, text="+5s",bg='#4a7abc',fg='white', command=lambda: skip(5))
skip_plus_5sec.pack(side="left",padx=10, pady=5,anchor="w")

b5 = Button(root, text='EXIT',bg='red',fg='white',font="none 10 bold",activebackground='white',activeforeground='red',width=16,command=exitWindow)
b5.pack(padx=10, pady=5,anchor="w")

root.mainloop()
