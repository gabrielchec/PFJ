from math import sin
from rk4 import rk4_vec
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
# ----------- constants -----------
g = 9.81
R = 1
m = 1
# ------------ init ------------
n = 2
dt = 0.01
N = 1000
t = 0
time = [i * dt for i in range(N)]
s = []
s.append(4)
s.append(0)
data_phi = []
data_speed = []


# ---------- functions -----------
def derivative(t, s, k):
    k[0] = s[1]
    k[1] = - g / R * sin(s[0])


for i in range(N ):
    rk4_vec(t, dt, n, s, derivative)
    t = t + dt
    data_phi.append(s[0])
    data_speed.append(s[1])


def plot_phi_t():
    ax.plot(time, data_phi, 'b')
    ax.set(xlabel='x', ylabel="y", title="Metoda RK4 dla dt = 15 min")
    plt.savefig("RK4_x_y.png")

    # plt.show()


fig, ax = plt.subplots()
plot_phi_t()
