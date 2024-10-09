import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

figura=plt.figure(figsize=(10,7))
ax=figura.add_subplot(111, projection="3d")

figura.patch.set_facecolor("black")
ax.set_facecolor("black")

num_figura=100
n_giro=num_figura*5
radio_inicial=0.1
aumento_radio=0.3
angulo_giro=145

x_vals, y_vals, z_vals= [], [], []

def actualizar(i):
    ax.clear()
    angulo_radio=np.deg2rad(i*angulo_giro)
    radio=radio_inicial+aumento_radio*i

    x=radio*np.cos(angulo_radio)
    y=radio*np.sin(angulo_radio)
    z=i*0.2

    x_vals.append(x)
    y_vals.append(y)
    z_vals.append(z)

    ax.plot(x_vals, y_vals, z_vals, color="white", lw=0.5)

    ax.set_xlim([-num_figura*2,num_figura*2])
    ax.set_ylim([-num_figura*2,num_figura*2])
    ax.set_zlim([0,n_giro*0.1])

    ax.set_title("Tornado 3D", color="white")
    ax.set_xlabel("x", color="white")
    ax.set_ylabel("y", color="white")
    ax.set_zlabel("z", color="white")

    ax.tick_params(axis="x", color="white")
    ax.tick_params(axis="y", color="white")
    ax.tick_params(axis="z", color="white")

main=FuncAnimation(figura, actualizar, frames=n_giro, interval=50)
plt.show()
