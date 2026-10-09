import streamlit as st
from feature01 import return_even

o_list = [i for i in range(0,10)]

st.write("we connected everything")

st.write(return_even(o_list))

