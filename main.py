import streamlit as st
import datetime

tab1, tab2, tab3 = st.tabs(["Home", "Peminjaman", "Pengembalian"])
with tab1:
   st.write('pinjam')
with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

