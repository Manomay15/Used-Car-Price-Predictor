import pickle
model = pickle.load(open('linear_regression.pkl', 'rb'))
print(model.predict([[10, 2002, 1, 2, 4, 213, 532, 3,4, 25 ,34, 234, 245, 45, 245, 0, 0, 0, 0, 1, 0]]))