import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random as rd

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
     df = pd.read_csv ('iris.csv')
     st.set_option('deprecation.showPyplotGlobalUse', False)
     #box plot for each species
     all_types = ['Petal.Length', 'Petal.Width', 'Sepal.Length', 'Sepal.Width']
     st.write('### **Box plot in three species**')
     test0 = st.multiselect("Select a variable or multiple variables:",['Petal.Length', 'Petal.Width', 'Sepal.Length', 'Sepal.Width'])

     def combination(y):
       x = list()
       for i in range(100):
         x.append(tuple(rd.sample(all_types,y)))
       x = set(x)
       x = list(x)
       x1 = list()
       for i in range(len(x)):
         x1.append(list(x[i]))   
       return(x1)

     comb1 = combination(1)
     comb2 = combination(2)
     comb3 = combination(3)
     comb4 = combination(4)
    
     
     for i in range(len(comb1)):
       if len(test0) == 1 and comb1[i] == test0:
         fig, axes = plt.subplots(1,figsize=(6,4))
         ax = sns.boxplot(x="Species", y=comb1[i][0], data=df, orient='v')
         st.pyplot(fig)
     
     
     for i in range(len(comb2)):
       if len(test0) == 2 and comb2[i] == test0:
         fig, axes = plt.subplots(1, 2,figsize=(10,5))
         ax = sns.boxplot(x="Species", y=comb2[i][0], data=df, orient='v', 
         ax=axes[0])
         ax = sns.boxplot(x="Species", y=comb2[i][1], data=df, orient='v', 
         ax=axes[1])
         st.pyplot(fig)

     for i in range(len(comb3)):
       if len(test0) == 3 and comb3[i] == test0:
         fig, axes = plt.subplots(1, 3,figsize=(14,6))
         ax = sns.boxplot(x="Species", y=comb3[i][0], data=df, orient='v', 
         ax=axes[0])
         ax = sns.boxplot(x="Species", y=comb3[i][1], data=df, orient='v', 
         ax=axes[1])
         ax = sns.boxplot(x="Species", y=comb3[i][2], data=df, orient='v', 
         ax=axes[2])
         st.pyplot(fig)

     for i in range(len(comb4)):
       if len(test0) == 4 and comb4[i] == test0:
         fig, axes = plt.subplots(2, 2,figsize=(12,10))
         ax = sns.boxplot(x="Species", y=comb4[i][0], data=df, orient='v', 
         ax=axes[0, 0])
         ax = sns.boxplot(x="Species", y=comb4[i][1], data=df, orient='v', 
         ax=axes[0, 1])
         ax = sns.boxplot(x="Species", y=comb4[i][2], data=df, orient='v', 
         ax=axes[1, 0])
         ax = sns.boxplot(x="Species", y=comb4[i][3], data=df, orient='v', 
         ax=axes[1, 1])
         st.pyplot(fig)
    

     st.write('')
     st.write('')
     st.write('')
     

     st.write('### **Relationship between Length and Width in three flower species**')

     
     all = list()
     for x in range(len(all_types)):
       for y in range(len(all_types)):
         temp = list()
         temp.append([all_types[x],all_types[y]])
         all.append(temp[0])

     num = list()
     for i in range(len(all)):
          num.append(i)



     test = st.multiselect("Select two variables:",['Petal.Length', 'Petal.Width', 'Sepal.Length', 'Sepal.Width'])
     st.write("You selected",len(test),"variables")

     
     for i in num:
       if all[i] == test:
          fig, axes = plt.subplots(1,figsize=(6,4))
          ax = sns.scatterplot(x=all[i][0], y=all[i][1], data=df,hue="Species",style="Species").set_title("Relationship between"+" "+all[i][0]+" "+"and"+" "+all[i][1])
          st.pyplot(fig)
     
     st.write('')
     st.write('')
     st.write('')
    
     st.write('### **Histogram in three flower species**')
     test2 = st.selectbox("Select a variable",['<select>','Petal.Length', 'Petal.Width', 'Sepal.Length', 'Sepal.Width'])
     
     if test2 == '<select>':
       st.write('')
     elif test2 != '<select>':
       fig, axes = plt.subplots(1,figsize=(6,4))
       ax = sns.distplot( df.loc[df.Species=='setosa', test2] , color="dodgerblue", label="Setosa")
       ax = sns.distplot( df.loc[df.Species=='virginica', test2] , color="orange", label="virginica")
       ax = sns.distplot( df.loc[df.Species=='versicolor', test2] , color="deeppink", label="versicolor")
       plt.legend()
       txt="I need the caption to be present a little below X-axis"
       plt.figtext(0.3, -0.05, txt, wrap=True, horizontalalignment='center', fontsize=6)
       st.pyplot(fig)
    


  

