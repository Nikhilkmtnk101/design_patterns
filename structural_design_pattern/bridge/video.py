from abc import ABC, abstractmethod

from video_processor import VideoProcessor


class Video(ABC):
    def __init__(self, video_processor: VideoProcessor):
        self._video_processor = video_processor

    @abstractmethod
    def play(self):
        pass


class Youtube(Video):

    def __init__(self, video_processor: VideoProcessor):
        super().__init__(video_processor)

    def play(self):
        print("Playing Youtube Video")
        self._video_processor.process()


class Netflix(Video):

    def __init__(self, video_processor: VideoProcessor):
        print("Playing Netflix Movie")
        super().__init__(video_processor)

    def play(self):
        self._video_processor.process()


class Prime(Video):

    def __init__(self, video_processor: VideoProcessor):
        super().__init__(video_processor)

    def play(self):
        print("Playing Prime Standup Comedy")
        self._video_processor.process()
