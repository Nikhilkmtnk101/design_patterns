from video import Youtube
from video_processor import VideoProcessor4k

if __name__ == "__main__":
    youtube_4k = Youtube(VideoProcessor4k())
    youtube_4k.play()