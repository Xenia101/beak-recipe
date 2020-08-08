from typing import *
from youtube_api import YouTubeDataAPI

class MyYoutube:
    def __init__(self, API_KEY: str):
        self.Ayoutube  = YouTubeDataAPI(API_KEY)
        self.ChID: str =  "PLoABXt5mipg4vxLw0NsRQLDDVBpOkshzF"
        
    def getDataFrom_yt(self)->list:
        searches = self.Ayoutube.get_videos_from_playlist_id(self.ChID)
        return [x['video_id'] for x in searches]

    def getMetaFrom_vd(self, Video_id_list: list)->list:
        return [self.Ayoutube.get_video_metadata(x)['video_description'] for x in Video_id_list]

if __name__ == "__main__":
    API_KEY: str = ""

    yt = MyYoutube(API_KEY)
    
    data: list = yt.getDataFrom_yt()
    meta: list = yt.getMetaFrom_vd(data)