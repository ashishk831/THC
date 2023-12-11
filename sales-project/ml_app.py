import gradio as gr
import pickle
import pandas as pd
import glob
import os


def get_latest_folder(directory):
    folders = [folder for folder in glob.glob(os.path.join(directory, '*')) if os.path.isdir(folder)]
    if not folders:
        return None
    return max(folders, key=os.path.getctime)

def load_pickle_from_latest_folder(directory, pickle_filename):
    latest_folder = get_latest_folder(directory)
    if latest_folder is None:
        print("No folders found in the specified directory.")
        return None

    pickle_path = os.path.join(latest_folder, pickle_filename)

    if not os.path.exists(pickle_path):
        print(f"No pickle file '{pickle_filename}' found in the latest folder.")
        return None

    with open(pickle_path, 'rb') as pickle_file:
        data = pickle.load(pickle_file)
        return data

# Example usage
directory_path = 'path to the 06_models folder'
pickle_filename = 'model.pkl'

model = load_pickle_from_latest_folder(directory_path, pickle_filename)

                        

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

