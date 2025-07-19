import pandas as pd
import os 
data = {"name":["alice","bob","charlie"],"age":[25,60,40],"city":['newyork','la','california']}
g1 = {"name":"riya","age":27,"city":"delhi"}
g2 = {"name":"cccc","age":28,"city":"mumbai"}


df = pd.DataFrame(data)
df.loc[len(df)] = g1
df.loc[len(df)] = g2
data_dir = "data"
os.makedirs(data_dir,exist_ok = True)
ss_path = os.path.join(data_dir,"sample.csv")
df.to_csv(ss_path,index = False)
