import streamlit as st
import pandas_profiling as pp
import pandas as pd
import streamlit_pandas_profiling as stpp 

def app():
     st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 200px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 200px;
        margin-left: -200px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
     st.markdown('### **:boat:Data profiling**')
     st.markdown('This iris data are a data frame of 150 records of iris petal and sepal lengths and widths. There are 50 samples in each iris species including “setosa”,”versicolor” and ”virginica”. The iris data profiling was presented by two package called **“pandas_profiling” and “streamlit_pandas_profiling”.** This profiling contains **data type for each column, quantile statistics, descriptive statistics, most frequent values, histogram, correlations and missing values.** It is a very convenient tool that allows us to understand data in details.  ')
     df = pd.read_csv ('iris.csv')
     report = pp.ProfileReport(df)
     stpp.st_profile_report(report)
 
 
