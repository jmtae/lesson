i = 0
j =0
for i in range(2, 10):  # 2단부터 9단까지
    print(f"{i}단:")
    for j in range(1, 10):  # 각 단의 1부터 9까지
        print(f"{i} x {j} = {i * j}")
    print()  # 각 단 사이에 빈 줄 추가
