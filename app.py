from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__, template_folder='templates')
    
try:
    with open('ml.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    print("Error: 'ml.pkl' file not found. Make sure the file exists in the same directory as your script.")
    model = None
except Exception as e:
    print(f"An error occurred while loading the model: {str(e)}")
    model = None

if model is None:
    print("Model is not loaded successfully. Check the model file and loading code.")


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['post'])
def predict():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g']
    data8 = request.form['h']
    data9 = request.form['i']
    data10 = request.form['j']
    data11 = request.form['k']
    data12 = request.form['l']
    data13 = request.form['m']

    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    
    
