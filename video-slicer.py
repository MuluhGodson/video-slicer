# written by Muluh MG Godson
# godsonmuluh@gmail.com

from moviepy.editor import *
import os
import csv


#Defaults
gif_duration = 5
videopath = "videos"
header = ['VIDEO', 'GIF', 'AUDIO', 'TSTART', 'TEND']

#Get all the videos
vid_tot = os.listdir(videopath)
print("Total Videos: " + str(len(vid_tot)))


#add data to csv file
with open('output/metadata.csv', 'a', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    for index, v in enumerate(vid_tot, start=1):
        #Load the video file
        clip = (VideoFileClip(videopath+"/"+v))

        #Get the Duration of the video file
        duration = clip.duration
        gif_total = int(duration/gif_duration)
        print("Clip Duration: " + str(duration))
        print("Total GIFs: " + str(gif_total))

        t_start = 0
        t_end = gif_duration

        for x in range(gif_total):
            print("Video: " + str(index) + " of " + str(len(vid_tot)))
            print("Video Name: " + str(v))
            print("GIF: " + str(x) + " of " + str(gif_total))
            print("GIF Beginning TimeStamp: " + str(t_start))
            print("GIF Ending TimeStamp: " + str(t_end))
            
            #Get 5 seconds of gif
            gif = clip.subclip(t_start,t_end)
            audioclip = gif.audio
            
            #export the gif  video and audio
            g_name = str(v)+str(x)+".gif"
            a_name = str(v)+str(x)+".wav"
            gif.write_gif("output/gif/"+g_name)
            audioclip.write_audiofile("output/audio/"+a_name, 44100, 2, 2000,"pcm_s32le")

            #Add data to csv file
            data = [str(v),g_name,a_name,t_start,t_end]
            writer.writerow(data)

            t_start = t_start + gif_duration
            t_end = t_end + gif_duration

      
  
