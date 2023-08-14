import numpy as np
from scipy import stats as st

data_set = np.array([364, 373, 358, 394, 378, 379, 357, 364, 350, 363, 392, 368, 359, 375, 399, 365, 379, 357, 380])

print("Mean of data set:", data_set.mean())
print("Median of data set:", np.median(data_set))
print("Mode of data set:", st.mode(data_set).mode)
print("Standard deviation of data set:", np.std(data_set))
