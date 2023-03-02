import time
from datetime import datetime
import streamlit as st

t = st.empty()

while True:
    t.markdown("%s" % str(datetime.now()))
    time.sleep(1)
