"""Расчет расстояния между объектами в космосе."""

import datetime

import spiceypy as spice


def get_spice_date(date):
    """
    Преобразует дату в формат ET (Ephemeris Time).

    :param date: Дата в формате datetime.
    :return: Время в формате ET.
    """
    return spice.utc2et(date.strftime("%Y-%m-%dT%H:%M:%S"))


# Инициализация SPICE
def load_spice_kernels():
    """
    Загружает необходимые SPICE ядра для расчета.

    Загружает ядра для траектории кометы и високосных секунд.
    """
    spice.furnsh("siding_spring_s46.bsp")  # Траектория кометы
    spice.furnsh("naif0012.tls")  # Високосные секунды


def calculate_distance_between_comet_and_mars(date):
    """
    Рассчитывает расстояние между кометой и Марсом на заданную дату.

    :param date: Дата в формате datetime для расчета расстояния.
    :return: Расстояние между кометой и Марсом в километрах.
    """
    et = get_spice_date(date)

    comet_state, _ = spice.spkgeo(targ=399, et=et, ref="ECLIPJ2000", obs=10)
    mars_state, _ = spice.spkgeo(targ=499, et=et, ref="ECLIPJ2000", obs=10)
    distance_vector = [mars_state[i] - comet_state[i] for i in range(3)]

    distance_km = spice.vnorm(distance_vector)

    return distance_km


if __name__ == "__main__":
    load_spice_kernels()
    date = datetime.datetime(2015, 1, 15)
    distance = calculate_distance_between_comet_and_mars(date)

    print(
        f"Расстояние между кометой C/2013 A1 и Марсом {date.strftime('%Y-%m-%d')} "
        f"составляет: {distance} км"
    )
