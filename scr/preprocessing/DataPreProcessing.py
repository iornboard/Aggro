import pandas as pd

#---------------------------------------------------------
fileName = "data 가이코_300_2021-06-08"
savePath = "../data/"
#encondingForm = 'utf-16be'
#---------------------------------------------------------

csv = pd.read_csv(savePath+fileName+".csv")
print(csv)