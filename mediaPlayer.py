import vlc
import keyboard  
import time
import subprocess
import pyautogui
import tkinter as tk

"""
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
"""
media_player = vlc.MediaPlayer()
mrl = "1.mp4"
  
# setting mrl to the media player
media_player.set_mrl(mrl)

  # creating vlc media player object


media_player.set_fullscreen(True)
  
# media object
media = vlc.Media("1.avi")
  
# setting media to the media player
media_player.set_media(media)

pencere=tk.Tk()

# start playing video
media_player.play()
quit = False
while True:

    if keyboard.read_key() == "h" :
        media_player.video_take_snapshot(0, "C:/Users/Divit/Desktop/vlcDeneme/imageCropper", 2400, 2300)

    elif keyboard.read_key() == "p" :
        media_player.pause()
        
        
        print("Video Durduruldu")   

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
 
   



