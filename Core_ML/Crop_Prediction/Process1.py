import pandas as pa
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt

datset=pa.read_csv("Dataset1.csv")
#removing duplicates  of district name and crop if they are present. 
datset_district=datset.drop_duplicates('District_Name')['District_Name']
datset_crop=datset.drop_duplicates('Crop')['Crop']


regressor = LinearRegression()

ppp = []

for i in datset_district:
    value_district = datset.loc[(datset['District_Name'] == i)].drop_duplicates('Crop')
    for j in value_district['Crop']:
        www = datset.loc[(datset['Crop'] == j) & (datset['District_Name'] == i)]
        try:
            x = www.iloc[:, 5:6].values
          #  print('x value is Area',x)
            y = www.iloc[:, 7:8].values
          #  print('y value is prod area',y)   #Production/Area
            xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.25, random_state=0)
            regressor.fit(xtrain, ytrain)

            predy = regressor.predict(xtest)
            #        accuracies=cross_val_score(estimator=regressor,X=xtrain,y=ytrain,cv=6)
            #        q=accuracies.mean()0
            print(type(predy))

            pred_min = predy.mean() - 0.2
           # print('pred_min value',pred_min)
            pred_max = predy.mean() + 0.2
            #print('pred_max value', pred_max)
            pred_mean = (pred_max + pred_min) / 2
            state = list(www.loc[(www['District_Name'] == i)].drop_duplicates('State_Name')['State_Name'])
            l = [state[0], i, j, www['prod_area'].mean(), pred_mean]
            ppp.append(l)
            print(l)
        except ValueError as w:
            print('w')
            #



            # %%
# ####################################
# ddd={1stcolum:'state':ppp[0],         2nd column'district':ppp[1],          3rd column'crop':ppp[2],            4th column'originalg_ MEAN VALUE(IN TONS)value':ppp[3],             5th cloumn'predicted_value(IN TONS)':ppp[4]}
##########################

p = pa.DataFrame(data=ppp)
p.to_csv('Output1.csv')





