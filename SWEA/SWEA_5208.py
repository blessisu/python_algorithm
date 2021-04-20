# 5208
# 전기버스2

# 뒤에서부터 확인하면서, 방전되기전이지만 최대한 왼쪽 것을 선택
# 배터리 누적아니고 교체임!

def back_search(end_pt):
    global total
    cnt = 1 # 맨 마지막 정거장은 충전기 없으니까 무조건 한 칸 소모
    max_idx = 1
    if end_pt <= 1: # 첫 정류장에 도착하면 stop
        return
    for idx in range(end_pt, 0, -1): # 첫정류장까지 검사 (index 0은 그냥 arr의 크기임을 주의)
        if cnt <= elec_lst[idx]:
            max_idx = idx
        cnt += 1
    # print(f'최종 max_idx는 {max_idx} 그 값은 {elec_lst[max_idx]}')
    if max_idx != 1: # 첫 정류장은 교체횟수에 포함X
        total += 1
    back_search(max_idx-1)
        



for tc in range(1, int(input())+1):
    elec_lst = list(map(int, input().split()))
    total = 0
    back_search(elec_lst[0]-1)
    print("#{} {}".format(tc, total))
        