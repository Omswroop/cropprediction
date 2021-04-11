a = [
     [12, 18, 6, 3],
     [ 4,  3, 1, 2],
     [15,  8, 9, 6],
[ 4,  3, 1, 2]
]
a.sort(key=lambda x: x[1])
print(a)



# wncoding the dependent variable

# print(list(X[0]))         ##wheat     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,
# print("-->",list(X[17]))  ##groundnut 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
# print("-->",list(X[38]))  ##Rice      0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,
# print("-->",list(X[54]))  ##Maize     0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
# print("-->",list(X[65]))  ##Millets   0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
# print("-->",list(X[85]))  ##Sugercane 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0,
# print("-->",list(X[103])) ##Barley    0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
# print("-->",list(X[138])) ##oilsedds  0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,
# print("-->",list(X[150]))  ##Tea      0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0,
# print("-->",list(X[175]))  ##Bajra    1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
# print("-->",list(X[190]))  ##Sorghum  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,

# avoid dummy variable trap



Tea = predict[0:4]  # tea 0.9
    print("Tea", Tea)  # 4
    Oilseeds = predict[5:7]  # 0.8
    print("Oil", Oilseeds)
    ###8,10
    sugercane = predict[11, 16]  ##0.6
    print("sugercane", sugercane)
    Millets = predict[17, 21]  # 0.5
    print("millets", Millets)
    Maize = predict(22, 24)  # 0.4
    print("Maize", Maize)
    Rice = predict[25, 30]
    print("Rice", Rice)  # 0.3
    Groundnut = predict[31, 41]
    print("Ground", Groundnut)  # 0.2
    print("dddd")
    Bajra = predict(42, 47)
    print("Bajra", Bajra)  # 0.12
    Sorghum = predict(48, 54)
    print("Sorghum", Sorghum)  # 0.11
    Wheat = predict(55, 70)
    print("Wheat", Wheat)  # 0.10

if (input_Crop == "Tea"):
     data = predii[0:4]

if (input_Crop == "Tea"):
     data = predii[0:4]

print("Tea", Tea)  # 4
Oilseeds = predict[5:7]  # 0.8
print("Oil", Oilseeds)
###8,10
sugercane = predict[11, 16]  ##0.6
print("sugercane", sugercane)
Millets = predict[17, 21]  # 0.5
print("millets", Millets)
Maize = predict(22, 24)  # 0.4
print("Maize", Maize)
Rice = predict[25, 30]
print("Rice", Rice)  # 0.3
Groundnut = predict[31, 41]
print("Ground", Groundnut)  # 0.2
print("dddd")
Bajra = predict(42, 47)
print("Bajra", Bajra)  # 0.12
Sorghum = predict(48, 54)
print("Sorghum", Sorghum)  # 0.11
Wheat = predict(55, 70)
print("Wheat", Wheat)  # 0.10

