"""Расчет баллистической траектории с учетом сопротивления воздуха."""

import numpy as np
import matplotlib.pyplot as plt

def ballistic_trajectory(v0, angle, cd=0.5, rho=1.225, A=0.01, m=1.0, g=9.81, dt=0.01):
    angle_rad = np.radians(angle)
    vx = v0 * np.cos(angle_rad)
    vy = v0 * np.sin(angle_rad)

    x = 0
    y = 0
    trajectory_x = [x]
    trajectory_y = [y]

    while y >= 0:
        v = np.sqrt(vx**2 + vy**2)
        Fd = 0.5 * cd * rho * A * v**2
        ax = -Fd * vx / (m * v)
        ay = -g - Fd * vy / (m * v)

        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt

        trajectory_x.append(x)
        trajectory_y.append(y)

    return trajectory_x, trajectory_y

initial_velocity = 30       # м/с
launch_angle = 45           # градусы
mass = 0.1                  # кг
cross_section_area = 0.005  # м^2

x, y = ballistic_trajectory(initial_velocity, launch_angle, m=mass, A=cross_section_area)

plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.xlabel("Дальность (м)")
plt.ylabel("Высота (м)")
plt.title("Баллистическая траектория с сопротивлением воздуха")
plt.grid(True)
plt.show()
