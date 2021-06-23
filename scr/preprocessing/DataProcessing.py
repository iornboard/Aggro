import re
from konlpy.tag import Okt
from collections import Counter
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import random
import math

#---------------------------------------------------------
fileName = "2convertTodata 코로나_700_2021-06-23"
fontpath = '..\ect\나눔고딕L.ttf'
SortBy = 'viewCount' # ["viewCount"]["noticeds"]
font = fm.FontProperties (fname=fontpath, size=18)
#encondingForm = 'utf-16be'
#---------------------------------------------------------


titleInfo = pd.read_csv(fileName+".csv")
titleInfo = titleInfo.sort_values(by="subscriberCount",ascending=False) # 구독자 기준으로 정렬
titleInfo = titleInfo[10:-10]

titleInfo["subscriberCount"] = titleInfo["subscriberCount"].astype(int)
titleInfo["viewCount"] = titleInfo["viewCount"].astype(int)
titleInfo["likeCount"] = titleInfo["likeCount"].astype(int)
titleInfo["commentCount"] = titleInfo["commentCount"].astype(int)

subscriberMean = titleInfo["subscriberCount"].mean()
titleInfo = titleInfo[titleInfo["subscriberCount"] < subscriberMean]


okt = Okt()
posList = []
sentencePattons = []

for titleIndex in titleInfo.index :
    posTitle = okt.pos(titleInfo.loc[titleIndex,'title'])

    sentence = []
    for tp in posTitle:
        text = {'text': tp[0], 'pos': tp[1], 'noticeds': titleInfo.loc[titleIndex,'noticeds'], 'viewCount': titleInfo.loc[titleIndex,'viewCount']}
        posList.append(text)
        sentence.append(tp[1])

    sentencePattons.append(" ".join(sentence))

sentencePattons.sort(key=lambda i:len(i))
MostTenSentencePattons = sentencePattons[:20]


noticedPos = pd.DataFrame(posList).sort_values(by=SortBy, ascending=False)
noticedMean = noticedPos["noticeds"].mean()

# noticedPos = noticedPos[noticedPos["noticeds"] < noticedMean]  #--------------------- 변칙성 있음


# ------------------------------표현1 : 단순 비교 -----------------------------------------------------------------

# print(titleInfo.sort_values(by=SortBy,ascending=False)['title'].head(20))


#------------------------------------- 표현2 : 문장 만들기 --------------------------------------------------------#

for sentenceItem in MostTenSentencePattons:
    makedSentence = []
    for item in sentenceItem.split(' '):
        notic = noticedPos[noticedPos['pos'] == item]
        randomIdx = random.randint(0,notic.shape[0])
        try:
            makedSentence.append(notic.iloc[randomIdx]['text'])
        except:
            makedSentence.append(" ")

    print(" ".join(makedSentence))



#------------------------------------------ 표현 3 : 단어 워드 클라우드---------------------------------------------------#

# noticedPos = noticedPos[noticedPos['pos'] == 'Noun']
#
# count = Counter(noticedPos['text'])
# remove_nouns = Counter({ x: count[x] for x in count if len(x)>1 })
#
# rank = remove_nouns.most_common(40)
#
# wordcloud = WordCloud(font_path=fontpath, relative_scaling=0.2, background_color='white').generate_from_frequencies(dict(rank))
#
# plt.figure(figsize=(12,8))
# plt.imshow(wordcloud)
# plt.show()

#---------------------------------------------------------------------------------------------#




