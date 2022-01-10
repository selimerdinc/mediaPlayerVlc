import vlc
import keyboard  
import time
import subprocess
import pyautogui
import tkinter as tk

from tkinter import *
 
from tkinter import messagebox
 


def video(source):
    vlc_instance = vlc.Instance()
     
    # creating a media player
    player = vlc_instance.media_player_new()
     
    # creating a media
    media = vlc_instance.media_new(source)
     
    # setting media to the player
    player.set_media(media)
                              #video kaç ms onu bulan fonksiyon
    # wait time
    time.sleep(0.5)
     
    # getting the duration of the video
    duration = player.get_length()
     
    # printing the duration of the video
    print("Duration : " + str(duration))
     
# call the video method
video("1.mp4")
  # creating vlc media player object
media_player = vlc.MediaPlayer()
  
# media object
media = vlc.Media("1.avi")
  
# setting media to the media player
media_player.set_media(media)




"""
pencere = Tk()
 
pencere.title("SELİMPLAYER")
pencere.geometry("200x300")
 
uygulama = Frame(pencere)
uygulama.grid()


buttonPause = Button(uygulama, text = " Durdur " , width=20, command=media_player.pause())
buttonPause.grid(padx=11, pady=7)

buttonSnap = Button(uygulama, text = " Ekran Görüntüsü Al " , width=20, command=  media_player.video_take_snapshot(0, "C:/Users/Divit/Desktop/vlcDeneme/imageCropper", 2400, 2200))
buttonSnap.grid(padx=11, pady=7)

buttonRate2 = Button(uygulama, text = "2x Hızlandır " , width=20, command=media_player.set_rate(2))
buttonRate2.grid(padx=11, pady=7)

buttonRatenormal = Button(uygulama, text = "Normal haline getir" , width=20, command=media_player.set_rate(1))
buttonRatenormal.grid(padx=11, pady=7)

buttonRateslow = Button(uygulama, text = "0.5x Yavaşlat" , width=20, command=media_player.set_rate(0.5))
buttonRateslow.grid(padx=11, pady=7)
pencere.mainloop()
"""
media_player.play()




quit = False
while True:
    
    if keyboard.read_key() == "h" :
        media_player.video_take_snapshot(0, "C:/Users/Divit/Desktop/vlcDeneme/imageCropper", 2400, 2200)
        
    elif keyboard.read_key() == "p" :
        media_player.pause()
        
        
 

    elif keyboard.read_key() == "z" :
        media_player.set_rate(0.5)
       
        
    elif keyboard.read_key() == "x" :
        media_player.set_rate(2)
        
           

    elif keyboard.read_key() == "c" :
        media_player.set_rate(1)
       
        
    elif keyboard.read_key()=="q":
         media_player.stop()
         
         print("Video Kapatıldı.")
         quit = True

         break

# getting media

value = media_player.get_media()
# printing media 
print("Media : ", value)
time.sleep(0)
 
   



