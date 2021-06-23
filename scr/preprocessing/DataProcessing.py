import pandas as pd

#---------------------------------------------------------
fileName = "convertTodata 코로나_700_2021-06-23"
#encondingForm = 'utf-16be'
#---------------------------------------------------------

titleInfo = pd.read_csv(fileName+".csv")
titleInfo = titleInfo[10:-10]


titleInfo["subscriberCount"] = titleInfo["subscriberCount"].astype(int)
titleInfo["viewCount"] = titleInfo["viewCount"].astype(int)
titleInfo["likeCount"] = titleInfo["likeCount"].astype(int)
titleInfo["commentCount"] = titleInfo["commentCount"].astype(int)

subscriberMean = titleInfo["subscriberCount"].mean()
print(subscriberMean)

titleInfo = titleInfo[titleInfo["subscriberCount"] < subscriberMean]
titleInfo = titleInfo.sort_values(by="subscriberCount",ascending=False)

print(titleInfo["viewCount"])



