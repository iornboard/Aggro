from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
import keys

DEVELOPER_KEY = keys.DEVELOPER_KEY4
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# 유튜브 객체 만들기
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

# id를 통해서 관련된 비디오의 ID를 받아오는 코드
def youtube_search_id_to_related(videoId,dataNums,categoryId): # 비디오 아이디, 데이터 갯수(50이하),

    videos = [videoId]  # 반환 리스트

    search_response = youtube.search().list(
        part="snippet",
        type="video",
        order="date",
        regionCode="KR",
        #q=keywords,
        relatedToVideoId=videoId,
        videoCategoryId=categoryId,
        maxResults=str(dataNums),
    ).execute()

    for search_result in search_response.get("items", []):
        videos.append(search_result["id"]["videoId"])

    return videos
