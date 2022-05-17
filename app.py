from flask import Flask, render_template, request
import pickle
import sklearn
app = Flask(__name__)
model = pickle.load(open('linear_regression.pkl', 'rb'))


@app.route('/', methods=['GET'])
def Home():
    # return render_template('index.html', cities=cities)
    return render_template('index.html')


# cities = ["Bengaluru", "Chennai", "Faridabad", "Ghaziabad", "Gurgao", "Hyderabad", "Kolkata", "Lucknow", "Mumbai", "New Delhi", "Noida", "Pune"]

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Year = int(request.form.get('Year'))
        Present_Price = float(request.form.get('Present_Price'))
        Kms_Driven = int(request.form.get('Kms_Driven'))
        Owner = int(request.form.get('Owner'))
        Fuel_Type = int(request.form.get('Fuel_Type_Petrol'))
        car_name = int(request.form.get('Brand'))
        Transmission = float(request.form.get('Transmission_Mannual'))
        Body_type = float(request.form.get('Body_type'))
        warranty = int(request.form.get('Warranty'))
        city = request.form.get('City')
        city_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        city_arr[int(city)] = 1
        input = [[car_name, Year, Fuel_Type, Kms_Driven, Body_type, Transmission, Owner, Present_Price, warranty]]
        for i in city_arr:
            input[0].append(i)
        print(input)
        prediction = model.predict(input)
        output = round(prediction[0], 2)
        if output < 0:
            return render_template('index.html', prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html', prediction_text="You can sell the Car at ₹{} Lakhs".format(output))
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)