# 5207
# 이진 탐색 (binary search)

# 문제를 덜 읽어서 틀림 !!!
# 양쪽구간을 번갈아 선택하게 되는 숫자의 개수를 알아보려고 한다.
# 즉 왼쪽 오른쪽 번갈아가면서 체크하고있는지 확인해야 함!

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    sorted_num_lst = list(map(int, input().split()))
    search_num_lst = list(map(int, input().split()))
    ans = 0
    sorted_num_lst.sort() # 정렬된 리스트여야 쓸 수 있음. 이진 탐색의 조건. 무조건 정렬부터하자!
    for search_num in search_num_lst:
        left = 0
        right = N - 1 # index는 0 ~ N-1 임
        left_or_right = 'mid'
        if search_num >= sorted_num_lst[left] and search_num <= sorted_num_lst[right]:         
            while right >= left:
                mid = (left+right)//2
                # print(f'{search_num}, {sorted_num_lst[mid]}')
                if sorted_num_lst[mid] == search_num:
                    ans += 1
                    break
                elif sorted_num_lst[mid] < search_num:
                    left = mid + 1
                    # 이전에 left였는데 또 left 면 조건 만족X
                    if left_or_right == 'left':
                        break
                    left_or_right = 'left'
                else:
                    right = mid - 1
                    if left_or_right == 'right':
                        break
                    left_or_right = 'right'
                # 연속 두 번 체크하는 것을 +1 +2 로 했더니
                # +1 -1 -1 인 경우를 chk 하지 못함.
                
    print("#{} {}".format(tc, ans))