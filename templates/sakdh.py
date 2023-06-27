import numpy as np
import matplotlib.pyplot as plt

# Tu arreglo original con valores ficticios en lugar de ...
arr = np.array([[[[239, 238, 236],
                  [243, 242, 240],
                  [241, 241, 239]],
                 
                 [[238, 236, 234],
                  [220, 218, 216],
                  [221, 219, 218]],
                 
                 [[225, 222, 220],
                  [143, 140, 139],
                  [161, 159, 157]]],

                [[[32, 32, 32],
                  [15, 15, 15],
                  [16, 16, 16]],
                 
                 [[49, 49, 49],
                  [76, 76, 76],
                  [94, 94, 94]],
                 
                 [[63, 63, 63],
                  [76, 76, 76],
                  [103, 103, 103]]],

                [[[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]],
                 
                 [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]],
                 
                 [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]]])

# Multiplicar cada elemento del arreglo por el factor
factor = 2
arr = arr * factor

# Asegurarse de que los valores estén dentro del rango adecuado (0-255)
arr = np.clip(arr, 0, 255)

# Convertir la matriz a tipo entero
arr = arr.astype(np.uint8)

# Mostrar la imagen
plt.imshow(arr)
plt.show()
