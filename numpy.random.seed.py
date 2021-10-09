import numpy as np
#là một hàm tạo các bộ sinh số ngẫu nhiên (random generator) và tham số thường là một số nguyên không âm, các giá trị của biến số khác nhau thì sẽ cho ra các số ngẫu nhiên khác nhau,và ngược lại, giống nhau thì sẽ ra số giống nhau
g = np.random
g.seed(10)
print("g rand: ", g.rand())

e = np.random
e.seed(10)
print("e rand: ", e.rand())