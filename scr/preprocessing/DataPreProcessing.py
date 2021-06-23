import pandas as pd
import youtubeRequest as Yre

#---------------------------------------------------------
fileName = "data 코로나_700_2021-06-23"
savePath = "../data/"
#encondingForm = 'utf-16be'
#---------------------------------------------------------

#1. 10개의 데이터 중에서 조회수 기준 상위 3개의 데이터를 추출 -> 하나의 DF으로 만듬
#2.

titleInfo = pd.read_csv(savePath+fileName+".csv")

noticedTileInfo = []



for x in range(0,len(titleInfo),10):
    videoGroup = titleInfo.loc[x:x + 10]
    viewMeans = videoGroup.mean()
    noticeds = videoGroup["viewCount"].apply(lambda x: x / viewMeans)["viewCount"]

    noticedsSl = pd.Series(noticeds,name="noticeds")
    NewVedioDF = pd.concat([videoGroup,noticedsSl], axis=1)

    highVeiwVedio =NewVedioDF.sort_values(by="noticeds",ascending=False)[:4]
    noticedTileInfo.append(highVeiwVedio)

# for x in range(0,len(titleInfo),10):
#     noticedTileInfo.append(titleInfo.loc[x:x+10].sort_values(by="viewCount",ascending=False)[:4])

df_titles = pd.concat(noticedTileInfo)
higherinfo = df_titles.sort_values(by="viewCount",ascending=False)
higherinfo.drop_duplicates(inplace=True, subset=['id'] )

higherinfo['channelId'] = higherinfo['channelId'].apply(lambda x: Yre.youtube_get_chennel_info(x))

higherinfo.rename(columns = {'channelId':'subscriberCount'},inplace = True)

higherinfo.to_csv("2convertTo"+fileName+".csv")



