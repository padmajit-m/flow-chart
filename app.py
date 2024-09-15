import streamlit as st
import pydot
from PIL import Image
import io

def create_flowchart_loan_origination():
    # Create the flowchart graph using pydot
    graph = pydot.Dot(graph_type="digraph", strict=False)

    # Define nodes and edges
    nodes = [
        'KYC Verification', 'Credit Check', 'Kiscore Check', 'Assign Area', 'Group Creation',
        'KYC Capture', 'KYC Document Verification', 'KYC Updation', 'KYC Data Verification',
        'Assign FO for Field Verification', 'Field Verification', 'Appraisal', 'GRT', 'Authorization',
        'Loan Disbursement', 'Kaleidofins System', 'Kicredit System'
    ]
    
    # Add nodes to the graph
    for node in nodes:
        graph.add_node(pydot.Node(node))
    
    # Add edges to the graph
    edges = [
        ('KYC Verification', 'Credit Check'),
        ('Credit Check', 'Kiscore Check'),
        ('Kiscore Check', 'Assign Area'),
        ('Assign Area', 'Group Creation'),
        ('Group Creation', 'KYC Capture'),
        ('KYC Capture', 'KYC Document Verification'),
        ('KYC Document Verification', 'KYC Updation'),
        ('KYC Updation', 'KYC Data Verification'),
        ('KYC Data Verification', 'Assign FO for Field Verification'),
        ('Assign FO for Field Verification', 'Field Verification'),
        ('Field Verification', 'Appraisal'),
        ('Appraisal', 'GRT'),
        ('GRT', 'Authorization'),
        ('Authorization', 'Loan Disbursement'),
        ('Loan Disbursement', 'Kaleidofins System'),
        ('Kaleidofins System', 'Kicredit System')
    ]
    
    # Add edges to the graph
    for edge in edges:
        graph.add_edge(pydot.Edge(*edge))
    
    return graph

def create_flowchart_bc_onboarding():
    # Create the flowchart graph using pydot
    graph = pydot.Dot(graph_type="digraph", strict=False)

    # Define nodes and edges
    nodes = [
        'Login as APEX User', 'Select Admin Management', 'Select Office Management', 'Manage BC',
        'Create New BC', 'Create Branch Office', 'Create Product Code', 'Area Creation', 'Area Approval',
        'Create Ledger', 'Assign Ledger'
    ]
    
    # Add nodes to the graph
    for node in nodes:
        graph.add_node(pydot.Node(node))
    
    # Add edges to the graph
    edges = [
        ('Login as APEX User', 'Select Admin Management'),
        ('Select Admin Management', 'Select Office Management'),
        ('Select Office Management', 'Manage BC'),
        ('Manage BC', 'Create New BC'),
        ('Create New BC', 'Create Branch Office'),
        ('Create Branch Office', 'Create Product Code'),
        ('Create Product Code', 'Area Creation'),
        ('Area Creation', 'Area Approval'),
        ('Area Approval', 'Create Ledger'),
        ('Create Ledger', 'Assign Ledger')
    ]
    
    # Add edges to the graph
    for edge in edges:
        graph.add_edge(pydot.Edge(*edge))
    
    return graph

def render_graph(graph):
    # Render the graph to a PNG image in-memory
    png_image = graph.create_png()
    return Image.open(io.BytesIO(png_image))

st.title('Flowchart Generator')

st.header('Loan Origination Process')
loan_chart = create_flowchart_loan_origination()
st.image(render_graph(loan_chart), caption='Loan Origination Process')

st.header('BC Partner Onboarding Process')
bc_chart = create_flowchart_bc_onboarding()
st.image(render_graph(bc_chart), caption='BC Partner Onboarding Process')
