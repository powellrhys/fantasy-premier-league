import streamlit as st
import numpy as np

def position_checkbox(key):
    filter_list = np.array(['Goalkeeper', 'Defender', 'Midfielder', 'Forward'])

    goal_check = st.sidebar.checkbox('Goalkeeper', value=True, key=key+'goal')
    def_check = st.sidebar.checkbox('Defender', value=True, key=key+'def')
    mid_check = st.sidebar.checkbox('Midfielder', value=True, key=key+'mid')
    fow_check = st.sidebar.checkbox('Forward', value=True, key=key+'fow')
    
    filter_index= np.array([goal_check, def_check, mid_check, fow_check])
    position_filter = filter_list[filter_index]

    return position_filter