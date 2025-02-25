"""Визуализация компонента магнитного поля во времени."""

import os

import matplotlib.pyplot as plt

from spacepy import pycdf


def analyze_themis_data(file_path):
    """
    Анализирует данные THEMIS и визуализирует компонент магнитного поля.

    :param file_path: Путь к файлу CDF с данными THEMIS.
    """
    try:
        with pycdf.CDF(file_path) as cdf:
            print("Доступные переменные:", list(cdf.keys()))

            if "thb_fbk_time" in cdf:
                time_data = cdf["thb_fbk_time"][...]

            if "thb_fbh" in cdf:
                fbh_data = cdf["thb_fbh"][...]

                plt.figure(figsize=(10, 6))
                plt.plot(time_data, fbh_data)
                plt.title("Данные THEMIS FBK (THB_FBH)")
                plt.xlabel("Время")
                plt.ylabel("Значение FBH")
                plt.grid(True)
                plt.show()
            else:
                print("Данные FBH не найдены в файле.")
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")


def main():
    """
    Основная функция для запуска анализа данных THEMIS.
    Загружает данные из указанного каталога и вызывает функцию анализа.
    """
    data_dir = os.path.join(
        os.path.expanduser("~"), "space/spacepy/themis_data/tha/fgm"
    )
    example_file = os.path.join(data_dir, "thb_l1_fbk_20241231_v01.cdf")

    if os.path.exists(example_file):
        analyze_themis_data(example_file)
    else:
        print(f"Файл не найден: {example_file}")


if __name__ == "__main__":
    main()
