
def rk4_vec(t, dt, n, s, fun):
    N = 1000
    k1 = [0] * N
    k2 = [0] * N
    k3 = [0] * N
    k4 = [0] * N
    w = [0] * N
    for i in range(n):
        w[i] = s[i]
    fun(t, w, k1)
    for i in range(n):
        w[i] = s[i] + dt / 2 * k1[i]
    fun(t + dt / 2, w, k2)
    for i in range(n):
        w[i] = s[i] + dt / 2 * k2[i]
    fun(t + dt / 2, w, k3)
    for i in range(n):
        w[i] = s[i] + dt * k3[i]
    fun(t + dt, w, k4)
    for i in range(n):
        s[i] = s[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])
