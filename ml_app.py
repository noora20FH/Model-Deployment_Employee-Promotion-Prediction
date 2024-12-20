import streamlit as st
from modelML_app import run_ml_app

import streamlit.components.v1 as stc

html_temp = """
            <div style="background-color:#3872fb;padding:10px;border-radius:10px">
		    <h1 style="color:white;text-align:center;">Employee Promotion Prediction App </h1>
		    <h4 style="color:white;text-align:center;">HR Team </h4>
		    </div>
            """

desc_temp = """
            ### Employee Promotion Prediction App
            This app will be used by the HR team to predict whether the employee get a promotion or not
            #### Data Source
            - https://raw.githubusercontent.com/densaiko/data_science_learning/main/dataset/Human%20Capital.csv
            #### App Content
            - Exploratory Data Analysis
            - Machine Learning Section
            """


def main(): #Homepage
    stc.html(html_temp)

    menu = ['Home', 'Machine Learning']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == "Home":
        st.subheader("Welcome to Home Page")
        st.markdown(desc_temp)
    elif choice == "Machine Learning" :
        # st.subheader("Machine Learning")
        run_ml_app()

if __name__ == '__main__' :
    main()
    