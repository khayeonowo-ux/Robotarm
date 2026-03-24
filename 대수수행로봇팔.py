import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🤖 로봇팔 시뮬레이터")

theta1 = st.slider("θ1", 0, 360, 45)
theta2 = st.slider("θ2", 0, 360, 30)
theta3 = st.slider("θ3", 0, 360, 20)

t1 = np.radians(theta1)
t2 = np.radians(theta2)
t3 = np.radians(theta3)

l1, l2, l3 = 2, 1.5, 1

x1, y1 = l1*np.cos(t1), l1*np.sin(t1)
x2, y2 = x1 + l2*np.cos(t1 + t2), y1 + l2*np.sin(t1 + t2)
x3, y3 = x2 + l3*np.cos(t1 + t2 + t3), y2 + l3*np.sin(t1 + t2 + t3)

fig, ax = plt.subplots()
ax.plot([0, x1, x2, x3], [0, y1, y2, y3], 'o-', linewidth=3)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')

st.pyplot(fig)
