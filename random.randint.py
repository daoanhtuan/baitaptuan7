import numpy as np
#sử dụng hàm np.random.randint để giải quyết bài toán, hàm nhận vào 2 tham số (số nguyên) chính là phạm vi trả về số ngẫu nhiên

# Ngẫu nhiên số nguyên trong khoảng [0, 2)
np.random.randint(0, 2)

#Giờ ta sẽ giả sử tung 1000 đồng xu bằng cách truyền vào tham số size:
coins = np.random.randint(2, size=1000)
print(coins.shape)

#Nếu ta tính % số lần tung được mặt ngửa và úp, ta sẽ thấy nó đều xấp xỉ 50%:
print("% số lần tung được mặt ngửa: ", (coins == 0).mean() * 100)
print("% số lần tung được mặt úp: ", (coins == 1).mean() * 100)
