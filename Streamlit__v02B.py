#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:14:48 2024

@author: parallels
"""

import numpy as np
import streamlit as st
import time


# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(page_title='La page du lapin MAUVE et son dashboard inutile')

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

CTN = 0
while(1):
    CTN+= 1
    chart.title(str(CTN))
    time.sleep(10)

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
