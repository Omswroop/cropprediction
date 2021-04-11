import pandas as pa
import numpy as np
import matplotlib.pyplot as plt
from statistics import *
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
datset = pa.read_csv("Dataset3.csv")
datset_crop = datset.drop_duplicates('crop')['crop']


# %%
def fit(x, y, crop, d):
    ppp = []
    regressor = LinearRegression()
    for i in range(10):
        xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.25, random_state=i * 13)
        regressor.fit(xtrain, ytrain)
        predy = regressor.predict(xtest)
        ppp.append(predy.mean())
    d[crop] = ppp
    return d



production = {}
imports = {}
exports = {}

for i in datset_crop:
    dis_val = datset.loc[(datset['crop'] == i)]

    x1 = dis_val.iloc[:, 7:8].values  # seed
    y1 = dis_val.iloc[:, 2:3].values  # production
    production = fit(x1, y1, i, production)
    print(production)

#####Upto here production Done

    a = dis_val.iloc[:, 3:6]
    b = dis_val.iloc[:, 2:3]
    x2=b+a
    print('x2',x2)
    x2['Production'] = b.iloc[:, 0]
    x2['Export']= a.iloc[:, 0]
    x2['Imports'] = a.iloc[:, 1]
    x2['Stock'] = a.iloc[:, 2]
    print('x2',x2)
    lll = []

    for k in list(a.iloc[0:0]):
        print('kk',k)
        x2[k] = a[k]

    y2 = dis_val.iloc[:, 2:3].values
    print('y2',y2)
    imports = (fit(x2.values, y2, i, imports))
    # model3=======exports
    a = dis_val.iloc[:, 2:4]
    b = dis_val.iloc[:, 7:8]
    print('b',b)

    x3=b+a
    x3['Production']=a.iloc[:, 0]
    x3['Imports'] = a.iloc[:, 1]

    x3['Seed'] = b.iloc[:, 0]
    print('x3',x3)
    for k in list(a.iloc[0:0]):
        x3[k] = a[k]

    y3 = dis_val.iloc[:, 4:5].values
    exports = (fit(x3.values, y3, i, exports))

# %%
#    finding the mean of all the entries required from the produced dictionaries
mean_prod = {}
mean_imp = {}
mean_exp = {}
for i in datset_crop:
    mean_prod[i] = (mean(production[i]))
    print('mean prod', mean_prod[i])
    mean_imp[i] = (mean(imports[i]))
    print('mean imp', mean_imp[i])
    mean_exp[i] = (mean(exports[i]))
    print('mean exp', mean_exp[i])
# %%
#    write these values in proper order in a csv file
print("lll",lll)


for i in datset_crop:
    l = []
    l.append(i)

    l.append(mean_exp[i])
    l.append(mean_imp[i])
    l.append(mean_prod[i])
    print('l',l)
    lll.append(l)

print("Its Working")
popo = pa.DataFrame(lll)
popo.to_csv('Output3.csv')



