import streamlit as st
from graphviz import Digraph
from PIL import Image
import io

def create_loan_origination_flowchart():
    dot = Digraph(comment='Loan Origination Process')

    # Define nodes
    dot.node('A', 'KYC Verification')
    dot.node('B', 'Credit Check')
    dot.node('C', 'Kiscore Check')
    dot.node('D', 'Assign Area')
    dot.node('E', 'Group Creation')
    dot.node('F', 'KYC Capture')
    dot.node('G', 'KYC Document Verification')
    dot.node('H', 'KYC Updation')
    dot.node('I', 'KYC Data Verification')
    dot.node('J', 'Assign FO for Field Verification')
    dot.node('K', 'Field Verification')
    dot.node('L', 'Appraisal')
    dot.node('M', 'GRT')
    dot.node('N', 'Authorization')
    dot.node('O', 'Loan Disbursement')
    dot.node('P', 'Kaleidofins System')
    dot.node('Q', 'Kicredit System')

    # Define edges
    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'E')
    dot.edge('E', 'F')
    dot.edge('F', 'G')
    dot.edge('G', 'H')
    dot.edge('H', 'I')
    dot.edge('I', 'J')
    dot.edge('J', 'K')
    dot.edge('K', 'L')
    dot.edge('L', 'M')
    dot.edge('M', 'N')
    dot.edge('N', 'O')
    dot.edge('O', 'P')
    dot.edge('P', 'Q')

    return dot

def create_bc_onboarding_flowchart():
    dot = Digraph(comment='BC Partner Onboarding Process')

    # Define nodes
    dot.node('A', 'Login as APEX User')
    dot.node('B', 'Select Admin Management')
    dot.node('C', 'Select Office Management')
    dot.node('D', 'Manage BC')
    dot.node('E', 'Create New BC')
    dot.node('F', 'Create Branch Office')
    dot.node('G', 'Create Product Code')
    dot.node('H', 'Area Creation')
    dot.node('I', 'Area Approval')
    dot.node('J', 'Create Ledger')
    dot.node('K', 'Assign Ledger')

    # Define edges
    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'E')
    dot.edge('E', 'F')
    dot.edge('F', 'G')
    dot.edge('G', 'H')
    dot.edge('H', 'I')
    dot.edge('I', 'J')
    dot.edge('J', 'K')

    return dot

st.title('Flowchart Generator')

st.header('Loan Origination Process')
loan_chart = create_loan_origination_flowchart()
loan_chart_path = '/tmp/loan_origination_flowchart.png'
loan_chart.render(loan_chart_path, format='png', cleanup=True)

st.image(loan_chart_path, caption='Loan Origination Process')

st.header('BC Partner Onboarding Process')
bc_chart = create_bc_onboarding_flowchart()
bc_chart_path = '/tmp/bc_onboarding_flowchart.png'
bc_chart.render(bc_chart_path, format='png', cleanup=True)

st.image(bc_chart_path, caption='BC Partner Onboarding Process')
