# 1954. 달팽이 숫자

# 1부터 N*N까지 시계방향으로 채워진 N*N array
# N을 입력받으면 해당 달팽이 배열 출력
# 1<=N<=10

def snail(idx, start, N):
    if idx > (N-idx):
        return
    if idx == N//2 and N%2 == 1:  # N이 홀수일 경우 가운데가 한 칸 남음
        ans[idx][idx] = start
        return
    if idx == N//2 and N%2 == 0:  # N이 짝수인 경우 가운데가 존재하지 않음
        return

    # 규칙적으로 넣기 위해,
    # 1 2 3
    # 8 9 4 
    # 7 6 5
    # 를 넣을 때 1 2 / 3 4 / 5 6 / 7 8 한 뱡해 같은 개수 숫자씩 넣기
    for i in range(idx, N-idx-1):
        ans[idx][i] = start
        start += 1
    for i in range(idx, N-idx-1):
        ans[i][N-idx-1] = start
        start += 1
    for i in range(N-idx-1, idx, -1):
        ans[N-idx-1][i] = start
        start += 1
    for i in range(N-idx-1, idx, -1):
        ans[i][idx] = start
        start += 1
    snail(idx+1, start, N)


for tc in range(1, int(input()) + 1):
    N = int(input())
    ans = [[0]*N for _ in range(N)]
    snail(0, 1, N)
    print("#{}".format(tc))
    for i in range(N):
        for num in ans[i]:
            print(num, end=" ")
        print()
