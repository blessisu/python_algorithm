# 5202
# 화물 도크

# 24시간 동안 최대한 많은 화물차가 화물 싣고 내리기
# 최소 몇 대의 화물차 이용?

# 가능한 조합 전부 해보면서
# 최대한 많은 화물 적재하는 것중
# 화물차도 최소인 것 고르기


# greedy algorithm -> 활동 선택 문제 -> 
# 종료시간을 기준으로 정렬한 뒤, 종료시간이 가장 빠른 것을 택하기

def go_truck(truck_num, end_time):
    global ans, N
    if truck_num == N:
        return
    # 선택 가능성 : 시작 시간이 이전의 종료시간과 같거나 후일 것
    if truck[truck_num][0] >= end_time:
        ans += 1
        go_truck(truck_num+1, truck[truck_num][1])
    else:
        go_truck(truck_num+1, end_time)

for tc in range(1, int(input())+1):
    N = int(input()) # 신청서 N
    truck = [list(map(int, input().split())) for _ in range(N)]
    # truck 이라는 list를 index가 1인 column 기준으로 오름차순 정렬
    truck.sort(key=lambda x: x[1])
    ans = 1
    go_truck(1, truck[0][1])
    print("#{} {}".format(tc, ans))
