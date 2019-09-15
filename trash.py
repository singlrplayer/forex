import h5py
import numpy as np

arr = np.random.randn(1000)

with h5py.File('random.hdf5', 'w') as f:
    dset = f.create_dataset("default", data=arr)
