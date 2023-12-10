import gradio as gr
import pickle
import pandas as pd

# Load the trained model
model_path = ''
with open(model_path, 'rb') as file:
    model = pickle.load(file)
                        

def predict(ad_id, age, gender, interest, Impressions, Clicks, Spent, Total_Conversion, CTR, CPC):
    # Convert relevant columns to appropriate types
    ad_id = int(ad_id)
    age = int(age)
    gender = int(gender)
    interest = int(interest)
    Impressions = int(Impressions)
    Clicks = int(Clicks)
    Spent = float(Spent)
    Total_Conversion = int(Total_Conversion)
    CTR = float(CTR)
    CPC = float(CPC)

    # Create a dictionary with input values
    input_data = {
        'ad_id': [ad_id],
        'age': [age],
        'gender': [gender],
        'interest': [interest],
        'Impressions': [Impressions],
        'Clicks': [Clicks],
        'Spent': [Spent],
        'Total_Conversion': [Total_Conversion],
        'CTR': [CTR],
        'CPC': [CPC]
    }

    # Create a DataFrame from the input data
    input_df = pd.DataFrame(input_data)

    # Make prediction
    prediction = model.predict(input_df)

    # Return the predicted value for Approved_Conversion
    return prediction[0]

# Define the input components for Gradio
inputs = [
    gr.Number(label='ad_id'),
    gr.Number(label='age'),
    gr.Number(label='gender'),
    gr.Number(label='interest'),
    gr.Number(label='Impressions'),
    gr.Number(label='Clicks'),
    gr.Number(label='Spent'),
    gr.Number(label='Total_Conversion'),
    gr.Number(label='CTR'),
    gr.Number(label='CPC')
]

# Create Gradio interface
iface = gr.Interface(
    fn=predict,
    inputs=inputs,
    outputs=gr.Textbox(type='text', label='Predicted Approved_Conversion')
)

# Launch the interface
iface.launch()

