from typing import *
from youtube_api import YouTubeDataAPI
import config
import os
import re 

class MyYoutube:
    def __init__(self, API_KEY: str):
        self.Ayoutube: YouTubeDataAPI  = YouTubeDataAPI(API_KEY)
        self.ChID: str =  "PLoABXt5mipg4vxLw0NsRQLDDVBpOkshzF" # paik's youtube

    def getDataFrom_yt(self)->List[str]:
        searches: List[str] = self.Ayoutube.get_videos_from_playlist_id(self.ChID)
        return [x['video_id'] for x in searches]

    def getMetaFrom_vd(self)->List[str]:
        VideoIdList: List[str] = self.getDataFrom_yt()
        video_title: List[str] = [self.Ayoutube.get_video_metadata(x)['video_title'] for x in VideoIdList]
        video_description: List[str] = [self.Ayoutube.get_video_metadata(x)['video_description'] for x in VideoIdList]
        return (video_title, video_description)

if __name__ == "__main__":
    yt: MyYoutube   = MyYoutube(config.API_KEY) # Private API KEY
    (title, meta) = yt.getMetaFrom_vd()
    
    for x in range(len(title)):
        title_name: str = title[x] + ".txt"
        title_name = re.sub('''[-=#/?|:"$'}]''', '', title_name)
        path: str = os.path.join("recipes_raw", title_name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(meta[x])
            
        print("[{}] - {}.txt".format(x, title_name))
    print("[Done..]")