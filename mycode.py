import pandas as pd
import os 
data = {"name":["alice","bob","charlie"],"age":[25,60,40],"city":['newyork','la','california']}
df = pd.DataFrame(data)
data_dir = "data"
os.makedirs(data_dir,exist_ok = True)
ss_path = os.path.join(data_dir,"sample.csv")
df.to_csv(ss_path,index = False)
