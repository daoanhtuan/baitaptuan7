import numpy as np
# là một phân phối xác suất cực kì quan trọng trong nhiều lĩnh vực
numpy.random.normal(loc=0.0, scale=1.0, size=None)
# loc = mean, scale = standard deviation

m, sigma = 0, 0.1
# mean và standard deviation
s = np.random.normal(m, sigma, size=5)
print(s)