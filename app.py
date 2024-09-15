import streamlit as st
import pygraphviz as pgv
from PIL import Image
import io

def create_flowchart_loan_origination():
    # Create the graph using AGraph from pygraphviz
    graph = pgv.AGraph(strict=False, directed=True)

    # Define nodes and edges
    graph.add_edge('KYC Verification', 'Credit Check')
    graph.add_edge('Credit Check', 'Kiscore Check')
    graph.add_edge('Kiscore Check', 'Assign Area')
    graph.add_edge('Assign Area', 'Group Creation')
    graph.add_edge('Group Creation', 'KYC Capture')
    graph.add_edge('KYC Capture', 'KYC Document Verification')
    graph.add_edge('KYC Document Verification', 'KYC Updation')
    graph.add_edge('KYC Updation', 'KYC Data Verification')
    graph.add_edge('KYC Data Verification', 'Assign FO for Field Verification')
    graph.add_edge('Assign FO for Field Verification', 'Field Verification')
    graph.add_edge('Field Verification', 'Appraisal')
    graph.add_edge('Appraisal', 'GRT')
    graph.add_edge('GRT', 'Authorization')
    graph.add_edge('Authorization', 'Loan Disbursement')
    graph.add_edge('Loan Disbursement', 'Kaleidofins System')
    graph.add_edge('Kaleidofins System', 'Kicredit System')

    return graph

def create_flowchart_bc_onboarding():
    # Create the graph using AGraph from pygraphviz
    graph = pgv.AGraph(strict=False, directed=True)

    # Define nodes and edges
    graph.add_edge('Login as APEX User', 'Select Admin Management')
    graph.add_edge('Select Admin Management', 'Select Office Management')
    graph.add_edge('Select Office Management', 'Manage BC')
    graph.add_edge('Manage BC', 'Create New BC')
    graph.add_edge('Create New BC', 'Create Branch Office')
    graph.add_edge('Create Branch Office', 'Create Product Code')
    graph.add_edge('Create Product Code', 'Area Creation')
    graph.add_edge('Area Creation', 'Area Approval')
    graph.add_edge('Area Approval', 'Create Ledger')
    graph.add_edge('Create Ledger', 'Assign Ledger')

    return graph

def render_graph(graph):
    # Render the graph to an in-memory PNG image
    png_image = graph.draw(format='png', prog='dot')
    return Image.open(io.BytesIO(png_image))

st.title('Flowchart Generator')

st.header('Loan Origination Process')
loan_chart = create_flowchart_loan_origination()
st.image(render_graph(loan_chart), caption='Loan Origination Process')

st.header('BC Partner Onboarding Process')
bc_chart = create_flowchart_bc_onboarding()
st.image(render_graph(bc_chart), caption='BC Partner Onboarding Process')
