from typing import *
from youtube_api import YouTubeDataAPI
import config

class MyYoutube:
    def __init__(self, API_KEY: str):
        self.Ayoutube: YouTubeDataAPI  = YouTubeDataAPI(API_KEY)
        self.ChID: str =  "PLoABXt5mipg4vxLw0NsRQLDDVBpOkshzF"
        
    def getDataFrom_yt(self)->List[str]:
        searches: List[str] = self.Ayoutube.get_videos_from_playlist_id(self.ChID)
        return [x['video_id'] for x in searches]

    def getMetaFrom_vd(self, Video_id_list: List[str])->List[str]:
        return [self.Ayoutube.get_video_metadata(x)['video_description'] for x in Video_id_list]

if __name__ == "__main__":
    yt: MyYoutube   = MyYoutube(config.API_KEY)
    
    data: List[str] = yt.getDataFrom_yt()
    meta: List[str] = yt.getMetaFrom_vd(data)
    
    print(meta)
    