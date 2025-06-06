
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

# Define form fields
fields = [
    {'name': 'Age', 'label': 'Age', 'type': 'number'},
    {'name': 'Income', 'label': 'Monthly Income', 'type': 'number'},
    {'name': 'LoanAmount', 'label': 'Loan Amount', 'type': 'number'},
    {'name': 'CreditScore', 'label': 'Credit Score', 'type': 'number'},
    {'name': 'MonthsEmployed', 'label': 'Months Employed', 'type': 'number'},
    {'name': 'NumCreditLines', 'label': 'Number of Credit Lines', 'type': 'number'},
    {'name': 'InterestRate', 'label': 'Interest Rate (%)', 'type': 'number'},
    {'name': 'LoanTerm', 'label': 'Loan Term (months)', 'type': 'number'},
    {'name': 'DTIRatio', 'label': 'Debt-to-Income Ratio', 'type': 'number'},
    {'name': 'Education', 'label': 'Education', 'type': 'select', 'options': ['High School', 'Bachelor', 'Master', 'PhD']},
    {'name': 'EmploymentType', 'label': 'Employment Type', 'type': 'select', 'options': ['Employed', 'Self-employed', 'Unemployed', 'Student']},
    {'name': 'MaritalStatus', 'label': 'Marital Status', 'type': 'select', 'options': ['Single', 'Married', 'Divorced']},
    {'name': 'HasMortgage', 'label': 'Has Mortgage', 'type': 'select', 'options': ['Yes', 'No']},
    {'name': 'HasDependents', 'label': 'Has Dependents', 'type': 'select', 'options': ['Yes', 'No']},
    {'name': 'LoanPurpose', 'label': 'Loan Purpose', 'type': 'select', 'options': ['Home', 'Car', 'Education', 'Business', 'Other']},
    {'name': 'HasCoSigner', 'label': 'Has Co-Signer', 'type': 'select', 'options': ['Yes', 'No']},
]

# Map string values to numbers (you must match what your model expects)
def preprocess(form):
    mapping = {
        'Yes': 1, 'No': 0,
        'Single': 0, 'Married': 1, 'Divorced': 2,
        'High School': 0, 'Bachelor': 1, 'Master': 2, 'PhD': 3,
        'Employed': 0, 'Self-employed': 1, 'Unemployed': 2, 'Student': 3,
        'Home': 0, 'Car': 1, 'Education': 2, 'Business': 3, 'Other': 4
    }
    input_data = []
    for field in fields:
        val = form[field['name']]
        if field['type'] == 'select':
            val = mapping[val]
        else:
            val = float(val)
        input_data.append(val)
    return [input_data]

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', fields=fields, prediction=None)



# For the Prediction to display the result:
@app.route('/predict', methods=['POST'])
def predict():
    form = request.form
    input_data = preprocess(form)
    prediction = model.predict(input_data)[0]
    return render_template('result.html', fields=fields, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

















# NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
# import gradio as gr
# import joblib

# model = joblib.load("model.pkl")

# def loan_default(Age,	Income,	LoanAmount,	CreditScore,	MonthsEmployed,	NumCreditLines,	InterestRate,	LoanTerm,	DTIRatio,	Education,	EmploymentType,	MaritalStatus,	HasMortgage,	HasDependents,	LoanPurpose,	HasCoSigner):
#     return model.predict([[Age,	Income,	LoanAmount,	CreditScore,	MonthsEmployed,	NumCreditLines,	InterestRate,	LoanTerm,	DTIRatio,	Education,	EmploymentType,	MaritalStatus,	HasMortgage,	HasDependents,	LoanPurpose,	HasCoSigner  ]])[0]

# demo = gr.Interface(fn=loan_default,
#                     inputs=["number", "number", 'number', 'number', 'number','number','number','number','number', 'number', 'number', 'number', 'number', 'number','number', 'number'],
#                     outputs="number")

# demo.launch()


#To be edited

# #importing libraries
# import numpy as np
# import flask
# import pickle
# from flask import Flask, render_template, request

# #creating instance of the class
# app=Flask(__name__)

# #to tell flask what url shoud trigger the function index()
# @app.route('/')
# @app.route('/index')
# def index():
#     return flask.render_template('index.html')
#     #return "Hello World"

# #prediction function
# def ValuePredictor(to_predict_list):
#     to_predict = np.array(to_predict_list).reshape(1,12)
#     loaded_model = pickle.load(open(r"model.pkl","rb"))
#     result = loaded_model.predict(to_predict)
#     return result[0]


# @app.route('/result',methods = ['POST'])
# def result():
#     if request.method == 'POST':
#         to_predict_list = request.form.to_dict()
#         to_predict_list=list(to_predict_list.values())
#         to_predict_list = list(map(int, to_predict_list))
#         result = ValuePredictor(to_predict_list)
        
#         if int(result)==1:
#             prediction='Income more than 50K'
#         else:
#             prediction='Income less that 50K'
            
#         return render_template("result.html",prediction=prediction)

# if __name__ == "__main__":
# 	app.run(debug=True)