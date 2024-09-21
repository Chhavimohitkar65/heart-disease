# 🫀💻 Heart Disease Prediction Model

This project implements a **Heart Disease Prediction Model** using **Logistic Regression** and provides a simple web interface for users to input medical data and get predictions on the likelihood of heart disease. The model is trained using a dataset containing various patient features like age, cholesterol levels, blood pressure, and more, to predict the presence or absence of heart disease.

## 🔑 Key Features

- **Machine Learning Model**: Logistic Regression model trained on a heart disease dataset.
- **Web Application**: Simple Flask-based web app for user interaction and predictions.
- **Data Input**: Users can input medical data (age, chest pain type, BP, etc.) to receive predictions.
- **Model Persistence**: The trained model is saved and loaded using `pickle` for easy reuse.

## 📂 Project Structure

- **ML.py**: This script handles data preprocessing, model training, and model saving.
- **app.py**: This Flask web app script serves the HTML pages, accepts user input, and returns predictions using the trained model.
- **templates/**: Contains the HTML files (`home.html`, `after.html`) used in the web app.
- **Heart_Disease_Prediction.csv**: The dataset used to train the model, containing patient data.

## 🧠 Model Details

- **Algorithm**: Logistic Regression
- **Dataset**: The heart disease dataset consists of features such as age, blood pressure, cholesterol levels, etc., to predict whether a patient has heart disease.

Example of data:

| Age | Sex | Chest pain type | BP  | Cholesterol | FBS over 120 | EKG results | Max HR | Exercise angina | ST depression | Slope of ST | Number of vessels fluro | Thallium | Heart Disease |
|-----|-----|-----------------|-----|-------------|--------------|-------------|--------|-----------------|---------------|-------------|--------------------------|----------|---------------|
| 70  | 1   | 4               | 130 | 322         | 0            | 2           | 109    | 0               | 2.4           | 2           | 3                        | 3        | Presence       |
| 64  | 1   | 4               | 128 | 263         | 0            | 0           | 105    | 1               | 0.2           | 2           | 1                        | 7        | Absence        |

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/heart-disease-prediction.git
   cd heart-disease-prediction
Prepare the dataset: Ensure that the CSV file (Heart_Disease_Prediction.csv) is in the correct directory as specified in the code.

2. Train the model: Run the ML.py script to train the Logistic Regression model and generate the ml.pkl file:
   ```bash
   python ML.py
3. Run the Flask web application: After the model is saved, start the Flask app:
   ```bash
   python aap.py

4. Access the web application: Open your browser and navigate to:
   ```bash
   http://127.0.0.1:5000/
   
5. Make predictions: Enter the required data in the web form, and the application will predict whether the patient has heart disease.


## 🛠️ Tech Stack

- **Frontend**: HTML (Rendered using Flask's Jinja templates)
- **Backend**: Flask
- **Machine Learning**: Logistic Regression using scikit-learn
- **Data Handling**: pandas, numpy
- **Model Persistence**: pickle
- **Dataset**: CSV file for heart disease prediction

## 🧩 Future Enhancements

- Improve the UI/UX of the web application.
- Integrate more machine learning models (e.g., Random Forest, SVM) to improve prediction accuracy.
- Deploy the web app to a cloud platform like Heroku or AWS.
- Allow for real-time predictions via API integrations.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
