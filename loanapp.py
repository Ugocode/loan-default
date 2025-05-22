import gradio as gr
import joblib

model = joblib.load("model.pkl")

def loan_default(Age,	Income,	LoanAmount,	CreditScore,	MonthsEmployed,	NumCreditLines,	InterestRate,	LoanTerm,	DTIRatio,	Education,	EmploymentType,	MaritalStatus,	HasMortgage,	HasDependents,	LoanPurpose,	HasCoSigner):
    return model.predict([[Age,	Income,	LoanAmount,	CreditScore,	MonthsEmployed,	NumCreditLines,	InterestRate,	LoanTerm,	DTIRatio,	Education,	EmploymentType,	MaritalStatus,	HasMortgage,	HasDependents,	LoanPurpose,	HasCoSigner  ]])[0]

demo = gr.Interface(fn=loan_default,
                    inputs=["number", "number", 'number', 'number', 'number','number','number','number','number', 'number', 'number', 'number', 'number', 'number','number', 'number'],
                    outputs="number")

demo.launch()
