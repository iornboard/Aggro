import pandas as pd
import youtubeRequest as Yre
import datetime

#---------------------------------------------------------
today = datetime.datetime.today().date()
rootSearchNum = 70 # 최대로 받을 수 있는 데이터 수 -> 아마 40예상함  (40*10= 400) -> 1번당 20정도의 비용 [30-> 3500P,]
mainKeyword = "코로나"
mainCatagory = "20"
saveFileName = "data %s_%s_%s.csv" % (mainKeyword, str(rootSearchNum*10), str(today))
savePath = "../data/"
#encondingForm = 'utf-16be'
#---------------------------------------------------------

rootStream = Yre.youtube_search_keyword_to_id(mainKeyword,rootSearchNum,mainCatagory)

allStream = []

for rootId in rootStream:
    allStream.append( Yre.youtube_search_id_to_related(rootId,9,mainCatagory))

data = []

for i, videoIdList in enumerate(allStream, start=1):
    print("working....  %s / %s " % (i ,len(allStream) ))
    for videoId in videoIdList:
        data.append( Yre.youtube_get_video_info(videoId))


df = pd.DataFrame(data)

df.to_csv(savePath+saveFileName, index=False)
print(df)

