"""Анализ и визуализация телеметрических данных."""

import pandas as pd
import matplotlib.pyplot as plt

NORMAL_TEMPERATURE_RANGE = (-30, 50)
NORMAL_BATTERY_VOLTAGE_RANGE = (3.5, 5.0)


def load_telemetry_data(file_path):
    data = pd.read_csv(file_path, sep=',', encoding='utf-8')
    print("Данные успешно загружены.")
    return data

def find_outliers(data, column, normal_range, column_name):
    outliers = data[~data[column].between(*normal_range)]
    if not outliers.empty:
        print(f"Обнаружены аномальные значения {column_name}: {len(outliers)} записей.")
    return outliers

def analyze_telemetry(data):
    temp_outliers = find_outliers(data, 'Temperature', NORMAL_TEMPERATURE_RANGE, 'температуры')
    voltage_outliers = find_outliers(data, 'BatteryVoltage', NORMAL_BATTERY_VOLTAGE_RANGE, 'напряжения батареи')
    return {'temperature_outliers': temp_outliers, 'battery_voltage_outliers': voltage_outliers}

def plot_telemetry(data):
    plt.figure(figsize=(12, 6))
    def create_subplot(ax_num, data_col, title, ylabel, normal_range, color):
        plt.subplot(2, 1, ax_num)
        plt.plot(data_col, label=title, color=color)
        plt.axhline(normal_range[0], color='red', linestyle='--', label='Нижний предел')
        plt.axhline(normal_range[1], color='green', linestyle='--', label='Верхний предел')
        plt.title(title)
        plt.xlabel('Время')
        plt.ylabel(ylabel)
        plt.legend()

    create_subplot(1, data['Temperature'], 'Изменение температуры', 'Температура, °C', NORMAL_TEMPERATURE_RANGE, 'blue')
    create_subplot(2, data['BatteryVoltage'], 'Изменение напряжения батареи', 'Напряжение, В', NORMAL_BATTERY_VOLTAGE_RANGE, 'orange')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_path = 'telemetry_log.csv'
    data = load_telemetry_data(file_path)
    if data is not None:
        analysis_results = analyze_telemetry(data)
        plot_telemetry(data)
