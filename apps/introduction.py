import streamlit as st
import pandas as pd
import emoji as em

def app():
# change the width of sidebar
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
     st.markdown('### **:book:Background of Iris flower dataset**')
     st.write('-------------------')
     st.markdown('<p style="font-size:11px">From Wikipedia, the free encyclopedia</p>', unsafe_allow_html=True)
     st.write('The **Iris flower data set** is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. It is sometimes called **Anderson\'s Iris data set** because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.[2] Two of the three species were collected in the Gaspé Peninsula \"all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus\".')
     st.write(' ')
     st.write(' ')
     st.markdown('### **:heavy_check_mark:About Iris dataset**')
     st.write(" The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.")
     from PIL import Image
     image = Image.open('image/03_iris.png')
     col3, col4, col5 = st.columns([1,6,1])

     with col3:
         st.write('')
     with col4:
          st.image(image, caption='https://www.datacamp.com/community/tutorials/machine-learning-in-r', width=None)
     with col5:
         st.write('')

     st.write('')
     st.write('')
     st.write('### **Dataset preview**')
     df = pd.read_csv ('iris.csv')
     st.write(df)







#https://en.wikipedia.org/wiki/Iris_flower_data_set
#navigation bar (introduction, summary statistics, data visualization, reference)