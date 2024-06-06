import numpy as np


def calculate(list):

    npliste = np.array(list)

    matrix = npliste.reshape(3,3)

    mean = np.mean(matrix.flatten())
    mean_row = np.mean(matrix, axis = 0)
    mean_col = np.mean(matrix, axis = 1)

    var_flat= np.var(matrix.flatten())
    var_col = np.var(matrix, axis = 0)
    var_row = np.var(matrix, axis =1)

    std_dev = np.std(matrix,axis=0)
    std_dev_col = np.std(matrix,axis=1)
    std_dev_flat = np.std(matrix.flatten())


    calculations = {
        "mean" :  [mean_row.tolist(),mean_col.tolist(),mean],
        "variance": [var_row.tolist(),var_col.tolist(),var_flat],
        "standard deviation": [std_dev.tolist(),std_dev_col.tolist(),std_dev_flat],
        "max": [np.max(matrix,axis=0).tolist(),np.max(matrix,axis=1).tolist(),np.max(matrix.flatten())],
        "min": [np.min(matrix,axis=0).tolist(),np.min(matrix,axis=1).tolist(),np.min(matrix.flatten())]
    }

    return calculations
    
