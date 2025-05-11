import streamlit as st
import numpy as np
from xyleme_core import ΔxylemeCore

st.set_page_config(page_title="∆xylème", layout="centered")
st.title("∆xylème — Interface Cognitive")

user_input = st.text_area("Stimulez le noyau ∆xylème avec une perception (symbolique ou émotionnelle)", "")
if st.button("Stimuler ∆xylème") and user_input.strip():
    vector = np.array([ord(c) % 256 / 255 for c in user_input.strip()][:16])
    core = ΔxylemeCore()
    state = core.perceive(vector)
    
    st.write("**Décision :**", state["decision"])
    st.write("**Δτ :**", state["Δτ"])
    st.write("**Attracteur :**", state["attractor"])
    st.write("**Epoch interne :**", state["epoch"])
