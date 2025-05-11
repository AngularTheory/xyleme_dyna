import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
from xyleme_core import ΔxylemeCore
import numpy as np

# Must be the first Streamlit command
st.set_page_config(page_title="∆xyleme — Live Memory", layout="wide")

st.title("∆xyleme — Cognitive Memory Visualization")

# Initialize or retrieve the core instance
if 'core' not in st.session_state:
    st.session_state.core = ΔxylemeCore()

# User input
input_text = st.text_input("Stimulate ∆xyleme (symbolic perception)", "hello")
if st.button("Stimulate"):
    vec = np.array([ord(c) % 128 / 128 for c in input_text])
    st.session_state.core.perceive(vec)

# Access the memory graph
graph = st.session_state.core.self_model.mental_map

# Draw the graph
fig, ax = plt.subplots(figsize=(12, 6))
pos = nx.spring_layout(graph, seed=42)
node_labels = {n: n for n in graph.nodes}
nx.draw(graph, pos, with_labels=True, labels=node_labels, node_size=900, node_color="#FF6F61", font_size=8, ax=ax)
st.pyplot(fig)