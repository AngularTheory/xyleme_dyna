import streamlit as st
import numpy as np
from xyleme_core import ΔxylemeCore

st.set_page_config(page_title="∆xylème — Cognitive Interface", layout="centered")
st.title("∆xylème — Cognitive Interface")

user_input = st.text_area("Stimulate the ∆xylème core with a symbolic or emotional perception", "")
if st.button("Stimulate ∆xylème") and user_input.strip():
    vector = np.array([ord(c) % 256 / 255 for c in user_input.strip()][:16])
    core = ΔxylemeCore()
    state = core.perceive(vector)

    st.write("**Decision:**", state["decision"])
    st.write("**Δτ (tension):**", state["Δτ"])
    st.write("**Attractor node:**", state["attractor"])
    st.write("**Internal epoch:**", state["epoch"])
    st.markdown(f"### Binary response : `{state['response']}`")