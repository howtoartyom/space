"""Визуализация компонента магнитного поля во времени."""

import os
from spacepy import pycdf
import matplotlib.pyplot as plt

def analyze_themis_data(file_path):
    try:
        with pycdf.CDF(file_path) as cdf:
            print("Available variables:", list(cdf.keys()))

            if 'thb_fbk_time' in cdf:
                time_data = cdf['thb_fbk_time'][...]

            if 'thb_fbh' in cdf:
                fbh_data = cdf['thb_fbh'][...]

                plt.figure(figsize=(10, 6))
                plt.plot(time_data, fbh_data)
                plt.title('THEMIS FBK Data (THB_FBH)')
                plt.xlabel('Time')
                plt.ylabel('FBH Value')
                plt.grid(True)
                plt.show()
            else:
                print("FBH data not found in the file.")
    except Exception as e:
        print(f"Error processing file: {e}")

def main():
    data_dir = os.path.join(os.path.expanduser("~"), "space/spacepy/themis_data/tha/fgm")
    example_file = os.path.join(data_dir, "thb_l1_fbk_20241231_v01.cdf")

    if os.path.exists(example_file):
        analyze_themis_data(example_file)
    else:
        print(f"File not found: {example_file}")


if __name__ == "__main__":
    main()
