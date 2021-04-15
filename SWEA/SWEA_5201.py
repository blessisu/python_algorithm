# 5201
# 컨테이너 운반

# N개의 컨테이너를 M대의 트럭으로 A->B 도시로 옮기기
# 트럭 용량을 초과하는 컨테이너는 옮길 수 없음
# 트럭은 편도로만 운행함
# 화물의 총 중량이 최대가 되도록 컨테이너 옮기기
# 옮겨진 화물의 전체 무게는 얼마?

# 아이디어 : 리스트를 둘다 무게가 큰 순으로 sort
# 화물차가 옮길 수 있는 가장 무거운 컨테이너 옮기기


for tc in range(1, int(input())+1):
    N, M = map(int, input().split()) # N은 컨테이너수 M은 트럭수
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    
    container.sort()
    truck.sort()

    truck_idx = M-1
    container_idx = N-1
    total = 0
    while True:
        # 트럭을 다 사용했거나, 더이상 옮길 컨테이너가 없으면 stop!
        if truck_idx < 0 or container_idx < 0:
            break
        # 현재 사용안한 트럭 중, 적재 용량이 가장 큰 트럭이
        # 옮길 수 있는 무게 중 가장 큰 값의 컨테이너 찾아서 옮기기 (옮기면 total에 누적)
        if truck[truck_idx] >= container[container_idx]:
            total += container[container_idx]
            truck.pop()
            truck_idx -= 1
        container_idx -= 1
    print("#{} {}".format(tc, total))
    


