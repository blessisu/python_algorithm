# 5188
# 최소합

# N*N 칸에 숫자가 적힌 판 --> 각 칸에서는 오른쪽/아래로만 이동 가능
# 모든 경로에 대한 합 계산 후 최솟값 찾기
# (0,0) 시작 (N-1, N-1) 도착 고정!!

def right_down_search(x, y, cnt):
    global N
    if x <= N-1 and y <= N-1:
        cnt += arr[x][y]
        if x==N-1 and y == N-1: # 오른쪽 아래 도착하면 성공! 합계 min_list에 넣기
            min_list.append(cnt)
            return
        right_down_search(x, y+1, cnt) # 오른쪽으로 이동
        right_down_search(x+1, y, cnt) # 아래로 이동
        

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_list = []
    # 사실 그 때 그 때 저장해서 비교해도 되는데
    # 문제에서 합을 모두 구하고 최솟값을 찾으라고 시켜서 리스트로 만들어줌.
    right_down_search(0, 0, 0)
    print("#{} {}".format(tc, min(min_list)))
