import numpy as np
#Phân phối này là một phân phối xác suất tóm tắt khả năng để một giá trị lấy một trong hai giá trị độc lập trong một tập hợp các tham số hoặc giả định nhất định

#Trong trường hợp đồng xu, “n” sẽ là số lần lật và “p” sẽ là xác suất thành công ( = 0.5)
np.random.binomial(20, 0.5) #Số mặt ngửa nhận được khi tung đồng xu 10 lần
np.random.binomial(20, 0.5, 10) #Số mặt ngửa nhận được khi tung đồng xu 20 lần trong 10 lần lặp

print("Trung bình số mặt ngửa nhận được khi tung đồng xu 20 lần trong vòng 10 lần lặp: ", np.random.binomial(20, 0.5, 10).mean())

n = 10  # tung 10 đồng xu trong 1 lần
p = 0.2  # bias cho mặt ngửa (xác suất cho mặt ngửa là 0.2)
l = 1000  # số lần lặp

b = np.random.binomial(n, p, l)
print("Trung bình số mặt ngửa nhận được: ", b.mean())
