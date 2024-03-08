from abc import abstractmethod, ABC


class VideoProcessor(ABC):

    @abstractmethod
    def process(self):
        pass


class VideoProcessor4k(VideoProcessor):
    def process(self):
        print("Process given video in 4k")


class VideoProcessor8k(VideoProcessor):
    def process(self):
        print("Process given video in 8k")


class VideoProcessor12k(VideoProcessor):
    def process(self):
        print("Process given video in 12k")


class VideoProcessorHD(VideoProcessor):
    def process(self):
        print("Process given video in HD")
