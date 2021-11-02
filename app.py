
import streamlit as st
from multiapp import MultiApp
from apps import introduction, summary, visualization, reference # import your app modules here


app = MultiApp()


#st.sidebar.title("Navigation yourself!")
#page_names = ['Introduction','Summary statistics','Data visualization','Reference']
#page = st.sidebar.radio(' ', page_names)

#st.sidebar.write("**The variable 'page' returns:**",page)

#navigation bar (introduction, summary statistics, data visualization, reference)
#cd '/home/jovyan/work/iris'

#st.markdown("""
# Multi-Page App
#This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
#""")

# Add all your application here
app.add_app("Introduction", introduction.app)
app.add_app("Data profiling", summary.app)
app.add_app("Data visualization", visualization.app)
app.add_app("Reference", reference.app)
# The main app
app.run()