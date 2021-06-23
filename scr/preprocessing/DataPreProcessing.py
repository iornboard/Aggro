import pandas as pd
import youtubeRequest as Yre

#---------------------------------------------------------
fileName = "data 코로나_700_2021-06-23"
savePath = "../data/"
#encondingForm = 'utf-16be'
#---------------------------------------------------------


titleInfo = pd.read_csv(savePath+fileName+".csv")

noticedTileInfo = []

for x in range(0,len(titleInfo),10):
    noticedTileInfo.append(titleInfo.loc[x:x+10].sort_values(by="viewCount",ascending=False)[:3])


df_titles = pd.concat(noticedTileInfo)
higherinfo = df_titles.sort_values(by="viewCount",ascending=False)
higherinfo.drop_duplicates(inplace=True, subset=['id'] )

higherinfo['channelId'] = higherinfo['channelId'].apply(lambda x: Yre.youtube_get_chennel_info(x))

higherinfo.rename(columns = {'channelId':'subscriberCount'},inplace = True)

higherinfo.to_csv("convertTo"+fileName+".csv")



