import pandas as pd
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
dataset = pd.read_excel('Agri_Fertilizers_Used.xls')

dataset = dataset.values

Y = dataset[0:, 3:4]
X = dataset[:, [1,3,4,5]]
print("Y is")
print(Y)

print("X is")
print(X)
X=list(X)


#print(Y.head())


X_trian, X_test, Y_train, Y_test = train_test_split(X, Y,  random_state=42)



model = LinearRegression()
model.fit(X_trian, Y_train)

X_test=list(X_test)
#print(X_test)
df=pd.DataFrame(X_test,columns=["Crop", "N", "P","K"])
df.sort_values('Crop')
#print(df)
final_df = df.sort_values(by=['Crop'], ascending=False)
#print("final df",final_df)

final_df=np.array(final_df)
predict = model.predict(final_df)

def mean(input):
    return sum(input)/len(input)



#print("Final Predict",predict)
predict=list(predict)
Tea=predict[0:4]  #tea 0.9

#print("Tea",Tea)
print("Tea",mean(Tea))          #Mean predicted value of the quantity of fertilizers for tea


Oilseeds=predict[5:7]   #0.8
#print("Oil",Oilseeds)
print("Oil",mean(Oilseeds))

Barley=predict[8:10]
#print("Barley",Barley)
print("Barley",mean(Barley))

sugercane=predict[11:16]   ##0.6
#print("sugercane",sugercane)
print("sugercane",mean(sugercane))


Millets=predict[17:21]      #0.5
#print("millets",Millets)
print("millets",mean(Millets))

Maize=predict[22:24]     #0.4
#print("Maize",Maize)
print("Maize",mean(Maize))

Rice=predict[25:30]
#print("Rice",Rice)
print("Rice",mean(Rice))
#0.3
Groundnut=predict[31:41]
#print("Ground",Groundnut)
print("Ground",mean(Groundnut))#0.2
#print("dddd")
Bajra=predict[42:47]
#print("Bajra",Bajra)
print("Bajra",mean(Bajra))
#0.12
Sorghum=predict[48:54]
#print("Sorghum",Sorghum)
print("Sorghum",mean(Sorghum))
#0.11
Wheat=predict[55:70]
#print("Wheat",Wheat)
print("Wheat",mean(Wheat))
#0.10
