from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
import keys

DEVELOPER_KEY = keys.DEVELOPER_KEY4
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# 유튜브 객체 만들기
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

# 키워드를 통한 1차 영상들의 ID를 추출해서 리스트로 반환하는 코드
def youtube_search_keyword_to_id(keywords,dataNums,categoryId): # 키워드 , 추출할 숫자, 카타고리

    maxNum = dataNums # 남은 추출수 (50개씩 추출함)
    pageToken = "" # 연속해서 추출하기위한 페이지 토큰수
    videos = [] #반환 리스트

    while maxNum > 0:

        if(pageToken == ""):
            search_response = youtube.search().list(
                part="id",
                type="video",
                order="date",
                maxResults=str(maxNum),
                q=keywords,
                videoCategoryId=categoryId,
                regionCode="KR",
            ).execute()

            # 응답에서 ID값만 리스트에 추가
            for search_result in search_response.get("items", []):
                videos.append(search_result["id"]["videoId"])

            maxNum -= 50
            pageToken = search_response.get("nextPageToken")

        else:
            search_response = youtube.search().list(
                part="id",
                type="video",
                order="date",
                maxResults=str(maxNum),
                q=keywords,
                pageToken=pageToken,
                videoCategoryId=categoryId,
                regionCode="KR",
            ).execute()

            for search_result in search_response.get("items", []):
                videos.append(search_result["id"]["videoId"])

            maxNum -= 50
            pageToken = search_response.get("nextPageToken")

    return videos


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

# 비디오 아이디의 대한 파일 정보를 리스트로 받아오는 정보
def youtube_get_video_info(videoId):
    search_response = youtube.videos().list(
        part= ["snippet" , "statistics"],
        id=videoId,
    ).execute()

    try:
        search_result = search_response['items'][0]

        return dict(
            id=videoId,
            title = search_result["snippet"]["title"],
            viewCount = search_result["statistics"]["viewCount"],
            likeCount = search_result["statistics"]["likeCount"],
            commentCount = search_result["statistics"]["commentCount"],
            channelId = search_result["snippet"]["channelId"],
            )

    except:
        return dict(
            id=videoId,
            title = "NA",
            viewCount = "NA",
            likeCount = "NA",
            commentCount = "NA",
            channelId = "NA",
            )


# 비디오 아이디를 통해 채널의 구독자 수를 받아오는 함수
def youtube_get_chennel_info(channelId):
    search_response = youtube.channels().list(
        part= ["statistics"],
        id=channelId,
    ).execute()

    try:
        search_result = search_response['items'][0]
        return search_result["statistics"]["subscriberCount"]

    except:
        return "NA"
