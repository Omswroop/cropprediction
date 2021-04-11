import pandas as pa
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer,LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score



datset=pa.read_csv("Dataset2.csv")
datset_crop=datset.drop_duplicates('crop')['crop']
ll=[]
for k in range(0,5):
    l=[]
    for j in datset_crop:
        value_crop=(datset.loc[(datset['crop'] == j)]).iloc[:,1:]
        for i in range(0,6):
            if i<=2:
                x = value_crop.iloc[:,i+1:].values
                print(x)
            else:
                x = value_crop.iloc[:,1:-(6-i)].values
            y = value_crop.iloc[:, i+1].values

            print('x values are',x)
            print('y valus are',y)
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True, random_state=k * 23)
            regressor = LinearRegression()
            regressor.fit(x_train, y_train)
            y_pred = regressor.predict(x_test)
            l.append(y_pred.mean())
            print('{2}===={0}===={1}\n'.format(y.mean(), y_pred.mean(), j))
            ll.append(l)
final = np.vstack((np.array(ll[0]), np.array(ll[1]), np.array(ll[2]), np.array(ll[3]), np.array(ll[4])))
final_mean = list(np.mean(final, axis=0))
print('np.array(ll[0])', np.array(ll[0]))
print('np.array(ll[1])', np.array(ll[1]))
print('np.array(ll[2])', np.array(ll[2]))
print('np.array(ll[3])', np.array(ll[3]))
headers = list(datset[0:0])
print('headers',len(headers))
datset_crop_list = list(datset_crop)
lll = []
for i in range(0, len(datset_crop_list)):
                l = []
                l.append(datset_crop_list[i])
                for j in range(0 ,6):
                    l.append(final_mean[j])
                    print('j',j)
                    print(final_mean[j])
                    lll.append(l)
                    print("lllcsv",lll)
popo = pa.DataFrame(lll)
popo.to_csv('Output2.csv')


# %%

