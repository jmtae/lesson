# # 구구단 출력 코드

# for i in range(2, 10):  # 2단부터 9단까지
#     print(f"{i}단:")
#     for j in range(1, 10):  # 각 단의 1부터 9까지
#         print(f"{i} x {j} = {i * j}")
#     print()  # 각 단 사이에 빈 줄 추가

# print ('구구단 출력 완료했습니다!')


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 마지막 i개의 요소는 이미 정렬되었으므로, 그 부분은 제외하고 반복합니다.
        for j in range(0, n-i-1):
            # 인접한 두 요소를 비교하여 순서가 잘못되었으면 교환합니다.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 테스트 리스트
test_list = [64, 34, 25, 12, 22, 11, 90]

# 정렬 전 리스트 출력
print("정렬 전 리스트:", test_list)

# 버블 정렬 실행
sorted_list = bubble_sort(test_list)

# 정렬 후 리스트 출력
print("정렬 후 리스트:", sorted_list)
