import os
import numpy as np
import matplotlib.pyplot as plt
x = ['Max Pelvis Rotation Velocity','Max Torso Rotation Velocity','Max Elbow Extension Velocity','Max Shoulder Internal Rotation Velocity']
y = [41.67,47.22,66.67,87.78]
fig, ax = plt.subplots()
width = 0.75
ind = np.arange(len(y))
ax.barh (ind, y, width, color = "green")
ax.set_yticks(ind+width/2)
ax.set_yticklabels (x, minor = False)
ax.set_xlim(0,100)
plt.title ('Timing (˚/s) as % of Pitch Cycle (%)')
plt.xlabel('FC-MIR %')
plt.ylabel('Timing Event')
for i, v in enumerate(y):
    ax.text(v, i," " +str(v), color='blue', va = 'center', fontweight='bold')
