import os
import subprocess
from logger import Logger

from pytubefix import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip

# For getting high-quality video
# https://github.com/JuanBindez/pytubefix/issues/128


class Download:
    
    def __init__(self):
        # default download location
        self.path = "./output"
        
        
    def url(self, _url, high_quality = True):
        """
        Download YouTube video from given link(s) at specified location
        
        :param _url: URL of YouTube video. Type str or list of str
        :param high_quality: indicate whether higher quality video and audio is required
        :return: None
        """
        
        # create download destination directory
        if not os.path.exists(self.path):
            os.mkdir(self.path)
            print(f"[DEBUG] Directory Created : {self.path}")
        
        try:
            if isinstance(_url, str):
                # get the video stream
                video = YouTube(_url.strip())
                
                if not high_quality:
                    resolution = video.streams.get_highest_resolution().resolution
                    print(f"[DEBUG] Downloading Video ({resolution}) : {video.title}")
                    
                    # download the video
                    video.streams.get_highest_resolution().download(self.path)
                    
                    print(f"[DEBUG] Download Complete : {video.title}")
                    print(f"[DEBUG] Download Destination : {self.path}")
                    
                    return
                
                # get the highest possible quality for video and audio
                print("[DEBUG] Getting highest possible quality for video and audio")
                video_stream = video.streams.order_by("resolution")[-1]  # ascending order
                audio_stream = video.streams.order_by("abr")[-1]  # ascending order
                
                # getting the extension
                video_stream_extension = video_stream.mime_type.split("/")[1]
                audio_stream_extension = audio_stream.mime_type.split("/")[1]
                
                # download video and audio separately
                temp_video_filename = f"video.{video_stream_extension}"
                temp_audio_filename = f"audio.{audio_stream_extension}"
                
                print(f"[DEBUG] Downloading video ({video_stream.resolution})")
                temp_video_path = video_stream.download(filename = temp_video_filename)
                print(f"[DEBUG] Downloading audio ({audio_stream.abr})")
                temp_audio_path = audio_stream.download(filename = temp_audio_filename)
                
                # combine the video and audio and download
                print("[DEBUG] Combining video and audio")
                video_clip = VideoFileClip(temp_video_filename)
                audio_clip = AudioFileClip(temp_audio_filename)
                
                video_clip.set_audio(audio_clip).write_videofile(
                        self.path + f"/{video.title}.mp4",
                        codec = "libx264",
                        logger = Logger()
                )
                
                print(f"[DEBUG] \033[1;32mDownload Complete : {video.title}\033[0;0m ")
                print(f"[DEBUG] Download Destination : {self.path}")
                
                # close the video and audio clip
                print("[DEBUG] Cleanup . . .")
                video_clip.close()
                audio_clip.close()
                
                # cleanup
                os.remove(temp_video_path)
                os.remove(temp_audio_path)
                print("[DEBUG] \033[1;32mDone !\033[0;0m ")
                
            elif isinstance(_url, list):
                
                for i in _url:
                    self.url(i)
                
        except Exception as e:
            print(f"[ERROR] {e}")
            print("[DEBUG] Tips : Setting \"high_quality = False\" may help")
        
    
    def view(self):
        """
        Launch file explorer and view specified folder
        
        :return: None
        """
        path = self.path.replace("/", "\\")
        subprocess.Popen(rf'explorer "{path}"', shell = False)
    

# RED     =   "\033[1;31m"
# YELLOW  =   "\033[1;33m"
# GREEN   =   "\033[1;32m"
# BLUE    =   "\033[1;34m"
# CYAN    =   "\033[1;36m"
# END     =   "\033[0;0m "
# print(RED + "TEXT" + END)

# Download().url(["https://youtu.be/0yOezV2qS6E ", "https://youtu.be/u2qPKcqRlS4 ", "https://youtu.be/RbR6LUKScyw", "https://youtu.be/zjd0vJk8qj8 ", " https://youtu.be/W87M6tRgA3g"])
# Download().url("https://youtube.com/shorts/c8FLGOLSK5s?si=z1ln0w2F34tfgxJd")
