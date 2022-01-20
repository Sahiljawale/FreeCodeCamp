import numpy as np

def calculate(list):
    arr=np.array(list)
    try:
        arr_3d = arr.reshape((3, 3))
    except ValueError:
        raise ValueError("List must contain nine numbers.")
    else:
    
        arr_3d=np.reshape(arr,(3,3))
        mean=[np.mean(arr_3d,axis=0).tolist(),np.mean(arr_3d,axis=1).tolist(),np.mean(arr_3d)]
        var=[np.var(arr_3d,axis=0).tolist(),np.var(arr_3d,axis=1).tolist(),np.var(arr_3d)]
        std=[np.std(arr_3d,axis=0).tolist(),np.std(arr_3d,axis=1).tolist(),np.std(arr_3d)]
        max=[np.max(arr_3d,axis=0).tolist(),np.max(arr_3d,axis=1).tolist(),np.max(arr_3d)]
        min=[np.min(arr_3d,axis=0).tolist(),np.min(arr_3d,axis=1).tolist(),np.min(arr_3d)]
        sum=[np.sum(arr_3d,axis=0).tolist(),np.sum(arr_3d,axis=1).tolist(),np.sum(arr_3d)]
  
  
    calculations = {
            "mean": mean,
            "variance": var,
            "standard deviation": std,
            "max": max,
            "min": min,
            "sum": sum
        }
    return calculations

print(calculate([0,1,2,3,4,5,6,7,8]))
