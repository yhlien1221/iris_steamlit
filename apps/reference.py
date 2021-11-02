import streamlit as st

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
     st.balloons()
     st.markdown('### **:rainbow:Reference**')
     st.markdown("""<a href="https://streamlit.io/">Streamlit</a>""", unsafe_allow_html=True)
     st.markdown("""<a href="https://en.wikipedia.org/wiki/Main_Page">Wikipedia</a>""", unsafe_allow_html=True)
     st.markdown("""<a href="https://github.com/pandas-profiling/pandas-profiling">Pandas-profiling</a>""", unsafe_allow_html=True)
    