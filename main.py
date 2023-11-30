import streamlit as st
import datetime

tab1, tab2, tab3 = st.tabs(["Home", "Peminjaman", "Pengembalian"])
with tab1:
   st.header('pinjam')
with tab2:
   st.header('Peminjaman')
with tab3:
   st.header("Pengembalian")

