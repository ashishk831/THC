import streamlit as st

st.header("Model Monitoring")

st.sidebar.header("Choose Report")

selected_report = st.sidebar.selectbox("Select a report", ["Feature Drift", "Label Drift"])


report_file_name = selected_report.replace(" ", "") + ".html"
HtmlFile = open(report_file_name, 'r', encoding='utf-8')
source_code = HtmlFile.read() 

st.components.v1.html(source_code, width=1200, height=1500, scrolling=True)