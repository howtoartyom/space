"""Вычисление и визуализация индекса NDVI на основе мультиспектральных данных."""

import matplotlib.pyplot as plt

import rasterio

with rasterio.open("1979_St_Helens.tif") as dataset:
    red = dataset.read(1)  # Канал красного цвета
    nir = dataset.read(3)  # Ближний инфракрасный канал


# Рассчитываем Normalized Difference Vegetation Index (NDVI)
def calculate_ndvi(nir, red):
    """
    Рассчитывает индекс NDVI на основе данных ближнего инфракрасного и красного каналов.

    :param nir: Данные ближнего инфракрасного канала.
    :param red: Данные красного канала.
    :return: Индекс NDVI.
    """
    ndvi = (nir.astype(float) - red.astype(float)) / (nir + red)
    return ndvi


ndvi = calculate_ndvi(nir, red)

# Визуализация NDVI
plt.figure(figsize=(10, 10))
plt.title("NDVI")
plt.imshow(ndvi, cmap="RdYlGn")
plt.colorbar()
plt.show()

with rasterio.open(
    "ndvi.tif",
    "w",
    driver="GTiff",
    height=ndvi.shape[0],
    width=ndvi.shape[1],
    count=1,
    dtype=ndvi.dtype,
    crs=dataset.crs,
    transform=dataset.transform,
) as dst:
    dst.write(ndvi, 1)
