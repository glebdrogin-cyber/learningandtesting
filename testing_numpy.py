import numpy as np

def test_array_creation():
    arr = np.array([1, 2, 3])
    assert arr.shape == (3,)
    assert arr.dtype == np.int64


