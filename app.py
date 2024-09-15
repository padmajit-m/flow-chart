import streamlit as st
import requests

def generate_flowchart():
    # Define the mermaid.js flowchart syntax for the loan origination process
    flowchart = """
    graph TD
        A[KYC Verification] --> B[Credit Check]
        B --> C[Kiscore Check]
        C --> D[Assign Area]
        D --> E[Group Creation]
        E --> F[KYC Capture]
        F --> G[KYC Document Verification]
        G --> H[KYC Updation]
        H --> I[KYC Data Verification]
        I --> J[Assign FO for Field Verification]
        J --> K[Field Verification]
        K --> L[Appraisal]
        L --> M[GRT]
        M --> N[Authorization]
        N --> O[Loan Disbursement]
        O --> P[Kaleidofins System]
        P --> Q[Kicredit System]
    """

    # QuickChart API URL for rendering mermaid diagrams
    quickchart_url = "https://quickchart.io/graphviz"

    # Send the flowchart to QuickChart API
    response = requests.get(quickchart_url, params={"graph": flowchart})

    if response.status_code == 200:
        return response.content
    else:
        st.error("Error generating flowchart. Please try again.")
        return None

# Streamlit UI
st.title("Flowchart Generator: Loan Origination Process")

# Generate the flowchart
image_data = generate_flowchart()

if image_data:
    # Display the image in Streamlit
    st.image(image_data, caption="Loan Origination Process Flowchart")
