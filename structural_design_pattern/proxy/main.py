from abc import ABC, abstractmethod


class ThirdPartyYoutubeLib(ABC):
    @abstractmethod
    def list_videos(self):
        pass

    @abstractmethod
    def get_video(self, video_id: int):
        pass

    @abstractmethod
    def download_video(self, video_id: int):
        pass


class ThirdPartyYoutubeClass(ThirdPartyYoutubeLib):
    def list_videos(self):
        print("Calling Youtube api to get list of videos")

    def get_video(self, video_id: int):
        print(f"Calling Youtube api to stream the video having id: {video_id}")

    def download_video(self, video_id: int):
        print(f"Calling youtube video to download video having id: {video_id}")


class ThirdPartyYoutubeProxy(ThirdPartyYoutubeLib):
    def __init__(self, service: ThirdPartyYoutubeLib):
        self.service = service
        self.is_cached = False

    def list_videos(self):
        if self.is_cached:
            print("Cache hit, returning list of videos from cache")
        else:
            print("Cache miss, using youtube lib to list down all the videos")
            self.service.list_videos()
            self.is_cached = True

    def get_video(self, video_id: int):
        if self.is_cached:
            print(f"Cache hit, streaming the video from cache having id: {video_id}")
        else:
            print(f"Cache miss, streaming the video from youtube having id: {video_id}")
            self.service.get_video(video_id)
            self.is_cached = True

    def download_video(self, video_id: int):
        if self.is_cached:
            print(f"Cache hit, downloading the video from cache having id: {video_id}")
        else:
            print(f"Cache miss, downloading the video from youtube having id: {video_id}")
            self.service.download_video(video_id)
            self.is_cached = True


if __name__ == "__main__":
    youtube_lib = ThirdPartyYoutubeClass()
    youtube_lib_proxy = ThirdPartyYoutubeProxy(youtube_lib)

    youtube_lib_proxy.get_video(1)
    youtube_lib_proxy.get_video(1)
