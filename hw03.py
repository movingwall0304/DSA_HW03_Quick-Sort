#定義列表
list = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]

#以函數方式結構化快速排序法
def QuickSort(list):
    #取得陣列長度
    n = len(list)
    #如果陣列只有一個元素或沒有元素，直接回傳
    if n <= 1:
        return list
    # 初始化左右兩個子陣列和基準點
    left = []
    right = []
    pivot = list[0]
    # 從第二個元素開始迭代
    for i in range(1, n):
        # 如果當前元素小於基準點，加到左子陣列，否則加到右子陣列
        if list[i] < pivot:
            left.append(list[i])
        else:
            right.append(list[i])
    # 遞迴排序左右子陣列，再將排序後的左子陣列、基準點、右子陣列依序合併
    return QuickSort(left) + [pivot] + QuickSort(right)
# 列印函數測試結果
print(QuickSort(list))