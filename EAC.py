import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def power_vs_delta(E, V, X):
    delta_values = np.linspace(0, 180, 100)
    P_values = (E * V / X) * np.sin(np.radians(delta_values))

    fig, ax = plt.subplots()
    ax.plot(delta_values, P_values)
    ax.set_xlabel('Delta (degrees)')
    ax.set_ylabel('Power (P)')
    ax.set_title('Power vs. Delta')
    ax.grid(True)

    st.pyplot(fig)


# Streamlit UI
st.title("Power vs. Delta Plotter")
st.sidebar.header("Input Parameters")

# Input fields for E, V, and X
E = st.sidebar.number_input("EMF (E)", value=1.0)
V = st.sidebar.number_input("Voltage (V)", value=1.0)
X = st.sidebar.number_input("Reactance (X)", value=1.0)

# Plot the graph based on user input
power_vs_delta(E, V, X)
