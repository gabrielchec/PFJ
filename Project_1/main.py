from math import sin, pi, cos

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
sn = 5
s = [[0.069813, 0], [pi / 4, 0], [pi / 2, 0], [3 * pi / 4, 0], [3.054326, 0]]

data_phi = [[], [], [], [], []]
data_speed = [[], [], [], [], []]
data_T = [[], [], [], [], []]
data_U = [[], [], [], [], []]
data_E = [[], [], [], [], []]


# ---------- functions -----------
def derivative(t, sk, k):
    k[0] = sk[1]
    k[1] = - g / R * sin(sk[0])


k = 0
phi_anal = []
for i in time:
    phi_anal.append(0.069813 * cos(pi * i + 0.069813))
for j in s:
    for i in range(N):
        rk4_vec(t, dt, n, j, derivative)
        t = t + dt
        data_phi[k].append(j[0])
        data_speed[k].append(j[1])
        data_T[k].append(m / 2 * pow(R * data_speed[k][-1], 2))
        data_U[k].append(-m * g * R * cos(data_phi[k][-1]))
        data_E[k].append(data_T[k][-1] + data_U[k][-1])

    k += 1

period = [[], []]
phi_list = []
phi_zero = []
dphi = 0.001

for i in range(31):
    phi_list.append([i * dphi, 0])
    phi_zero.append([i * dphi, 0])
step = 0
for i in phi_list:
    t = 0
    while True:
        rk4_vec(t, dt, n, i, derivative)
        t = t + dt
        if t > 1 and phi_zero[step][0] - dphi <= i[0] <= phi_zero[step][0] + dphi:
            period[1].append(t)
            period[0].append(step * dphi)
            break
    step += 1


def plot_x_y(text, short_x, short_y, save_name, data_x, data_y):
    fig, ax = plt.subplots()
    ax.plot(data_x[0], data_y[0], 'b')
    ax.plot(data_x[1], data_y[1], 'g')
    ax.plot(data_x[2], data_y[2], 'y')
    ax.plot(data_x[3], data_y[3], 'r')
    ax.plot(data_x[4], data_y[4])
    ax.set(xlabel=short_x, ylabel=short_y, title=text)
    phi_0 = mlines.Line2D([], [], label='phi = 4', color='blue')
    phi_1 = mlines.Line2D([], [], label='phi = 45', color='green')
    phi_2 = mlines.Line2D([], [], label='phi = 90', color='yellow')
    phi_3 = mlines.Line2D([], [], label='phi = 135', color='red')
    phi_4 = mlines.Line2D([], [], label='phi = 175', color='black')

    ax.legend(handles=[phi_0, phi_1, phi_2, phi_3, phi_4], loc='upper left',
              fontsize='x-large')

    plt.savefig(save_name + ".png")


def plot_period_phi(text, short_x, short_y, save_name, data_x, data_y):
    fig, ax = plt.subplots()
    ax.plot(data_x, data_y, 'b')
    ax.set(xlabel=short_x, ylabel=short_y, title=text)

    plt.savefig(save_name + ".png")

def plot_phi_anal():
    fig, ax = plt.subplots()
    ax.plot(time, data_phi[0], 'b')
    ax.plot(time, phi_anal, 'g')
    phi_0 = mlines.Line2D([], [], label='numerycznie', color='blue')
    phi_1 = mlines.Line2D([], [], label='analitycznie', color='green')

    ax.legend(handles=[phi_0, phi_1], loc='upper left',
              fontsize='x-large')
    ax.set(xlabel="t", ylabel="phi", title="Wykres zależności kąta od czasu")

    plt.savefig( "phi_t_anal.png")


# plot_x_y("Wykres zależności kąta od czasu", "t", "T", "phi_t", time, data_phi)
# plot_x_y("Wykres zależności Energii kinetycznej od czasu", "t", "T", "T_t", time, data_T)
# plot_x_y("Wykres zależności Energii potencjalnej od czasu", "t", "U", "U_t", time, data_U)
# plot_x_y("Wykres zależności Energii całkowitej od czasu", "t", "E", "E_t", time, data_E)
# plot_x_y("Wykres zależności prędkości od położenia", "phi", "d phi/dt", "v_phi", data_phi, data_speed)

#plot_period_phi("Wykres zależności okresu od maksymalnego wychylenia", "phi", "okres", "period_phi", period[0],
     #           period[1])

plot_phi_anal()