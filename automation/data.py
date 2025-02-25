"""Создание тестовых данных."""

from datetime import datetime, timedelta

import numpy as np
import pandas as pd


def generate_telemetry_data(num_days=7, readings_per_hour=6):
    """
    Генерирует тестовые телеметрические данные.

    :param num_days: Количество дней для генерации данных.
    :param readings_per_hour: Количество показаний в час.
    :return: DataFrame с сгенерированными телеметрическими данными.
    """
    total_readings = num_days * 24 * readings_per_hour

    start_date = datetime(2024, 2, 1)
    timestamps = [
        start_date + timedelta(minutes=(i * (60 / readings_per_hour)))
        for i in range(total_readings)
    ]

    base_temp = 25
    temp_amplitude = 10
    time_values = np.linspace(0, num_days * 2 * np.pi, total_readings)

    temperature = (
        base_temp
        + temp_amplitude * np.sin(time_values)
        + np.random.normal(0, 2, total_readings)
    )

    anomaly_indices = np.random.choice(
        total_readings, size=int(total_readings * 0.02), replace=False
    )
    temperature[anomaly_indices] += np.random.choice(
        [-20, 20], size=len(anomaly_indices)
    )

    initial_voltage = 4.2
    voltage_decay = np.linspace(0, 0.5, total_readings)
    battery_voltage = (
        initial_voltage - voltage_decay + np.random.normal(0, 0.1, total_readings)
    )

    drop_indices = np.random.choice(
        total_readings, size=int(total_readings * 0.01), replace=False
    )
    battery_voltage[drop_indices] -= 0.5

    df = pd.DataFrame(
        {
            "Timestamp": timestamps,
            "Temperature": temperature,
            "BatteryVoltage": battery_voltage,
        }
    )

    df["BatteryVoltage"] = df["BatteryVoltage"].clip(3.0, 4.2)

    return df


telemetry_data = generate_telemetry_data()
telemetry_data.to_csv("telemetry_log.csv", index=False)
print("\nFirst few readings:")
print(telemetry_data.head())
print("\nDataset statistics:")
print(telemetry_data.describe())
