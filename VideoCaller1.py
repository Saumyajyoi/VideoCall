#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from vidstream import*
import tkinter as tk
import socket
import threading
import requests
from tkinter import*

local_ip_address = socket.gethostbyname(socket.gethostname())
server = StreamingServer(local_ip_address, 9999)
receiver = AudioReceiver(local_ip_address, 8888)

def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()
   

def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0,'end-1c'),7777)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()
   
def start_screen_sharing():
    screen_client = ScreenShareClient(text_target_ip.get(1.0,'end-1c'),7777)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()

def start_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0,'end-1c'),6666)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()  

def ip():
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)
    myText.set(IPAddr)
    myText1.set(hostname)
    
    
#GUI

window = tk.Tk()
window.title("Video Caller")
window.geometry('300x300')
window.configure(bg="Light Green")

myText=StringVar()
myText1=StringVar()

btn_ip = tk.Button(window, text="Show ip", width=50, command=ip, bg="Light Blue")
btn_ip.pack(anchor=tk.CENTER, expand=True)

result1=Label(window, textvariable=myText1, bg="light green")
result1.pack()

result=Label(window, textvariable=myText , bg="Light Green")
result.pack()

label_target_ip = tk.Label(window, text="Target IP:", bg="Orange")
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

btn_listen = tk.Button(window, text="Start Listening", width=50, command=start_listening, bg="Green")
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_Camera  = tk.Button(window, text="Start Camera Stream", width=50, command=start_camera_stream, bg="Yellow")
btn_Camera.pack(anchor=tk.CENTER, expand=True)

btn_Screen = tk.Button(window, text="Start Screen Sharing", width=50, command=start_screen_sharing, bg="Pink")
btn_Screen.pack(anchor=tk.CENTER, expand=True)

btn_Audio = tk.Button(window, text="Start Audio Stream", width=50, command=start_audio_stream, bg ="Violet")
btn_Audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()


# In[ ]:




