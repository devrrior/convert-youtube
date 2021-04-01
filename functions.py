# Show qualities available
import pytube
import ffmpeg
import os
import shutil

def choose_option(url):
    # Show available options and choose the option
    qualities_of_video = url.streams.filter(adaptive=True,file_extension="mp4",only_video=True)
    print("\n### Qualities available ###")

    counter = 0
    options = {}
    last_resolution = ""
    last_fps = 0

    for quality in qualities_of_video:
        counter += 1

        if last_resolution == quality.resolution:
            if  last_fps == quality.fps:
                pass
            else:
                print(f"Qualities {counter}: Resolution: {quality.resolution}  FPS: {quality.fps}")
                options[counter] = [quality.resolution,quality.fps]
                last_resolution = quality.resolution
                last_fps = quality.fps
        else:
            print(f"Qualities {counter}: Resolution: {quality.resolution}  FPS: {quality.fps}")
            options[counter] = [quality.resolution,quality.fps]
            last_resolution = quality.resolution
            last_fps = quality.fps

    number_option = int(input("What quality do you prefer?: "))

    return options[number_option]

def download_video_audio(url,option):
    # Download videos and audio
    video = url.streams.filter(file_extension="mp4",resolution=option[0],fps=option[1])
    video[0].download(filename="video",output_path=".cache/")

    audio = url.streams.filter(only_audio=True,file_extension="mp4")
    audio[0].download(filename="audio",output_path=".cache/")

def merge_video_and_audio(name):
    # Merge audio and video
    video = ffmpeg.input(f".cache/video.mp4")
    audio = ffmpeg.input(f".cache/audio.mp4")

    out = ffmpeg.output(video, audio, f"/Users/fernando/Downloads/{name}.mp4", vcodec="copy", acodec="aac", strict="experimental")
    out.run()

def delete_cache(name):
    os.remove(f".cache/video.mp4")
    os.remove(f".cache/audio.mp4")
