import pandas as pd
import json
 
with open("data/movie_data.json") as myFile:
  fileData = json.load(myFile)
  dataFrame = pd.DataFrame(columns=fileData[0].keys())
  for i in range(len(fileData)):
     dataFrame.loc[i] = fileData[i].values()
     print(dataFrame)