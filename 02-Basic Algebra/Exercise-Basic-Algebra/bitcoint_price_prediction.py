import matplotlib

matplotlib.use('TkAgg')  # или 'Qt5Agg'
import matplotlib.pyplot as plt
import numpy as np
import datetime
import requests


def bitcoin_price_prediction(points, degree, min_x, max_x, predict_steps):
    x, y = points[:, 0], points[:, 1]

    coeffs = np.polyfit(x, y, deg=degree)
    poly = np.poly1d(coeffs)

    plot_x = np.linspace(min_x, max_x + predict_steps, 1000)
    plot_y = poly(plot_x)

    future_x = np.arange(max_x + 1, max_x + predict_steps + 1)
    future_y = poly(future_x)

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, label="data points", color="red")
    plt.plot(plot_x, plot_y, color='green', label="interpolating polynomial")
    plt.scatter(future_x, future_y, color='orange', label="forecast", marker='x', s=100)

    for fx, fy in zip(future_x, future_y):
        print(f"Прогноза: x = {fx}, y = {fy:.4f}")

        plt.text(future_x[-1], future_y[-1], f"${future_y[-1]:,.0f}", color='orange', fontsize=12, ha='left',
                 va='bottom')

    plt.xlabel("x (time)")
    plt.ylabel("y (price)")
    plt.title("Bitcoin Price Interpolation and Forecast")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


currentPoints = np.array([
    (1, 84240), (2, 87025), (3, 86525),
    (4, 88155), (5, 88415), (6, 83955),
    (7, 84195), (8, 85635), (9, 82230),
    (10, 84610), (11, 84840), (12, 80245),
    (13, 83155), (14, 83395), (15, 79025),
    (16, 87320), (17, 89460), (18, 90935),
    (19, 86570), (20, 90450), (21, 83490),
    (22, 83375)]
)

degree = 3
min_x = np.min(currentPoints[:, 0])
max_x = np.max(currentPoints[:, 0])
predict_steps = 5

bitcoin_price_prediction(currentPoints, degree, min_x, max_x, predict_steps)
