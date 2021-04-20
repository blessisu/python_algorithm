# 1865
# 동철이의 일분배

# 직원 N명 과 해야할 일 N개
# i 직원이 j 번 일을 하면 성공확률 arrij
# 모든 일을 잘 풀리도록
# 주어진 일이 모두 성공할 확률의 최댓값 << 을 구하자

# N이 커질 수록 너무 다양한 것 같아서.. 완전 탐색으로 모든 경우 살펴보고 거기서 max 값 갱신해나가자
# 라고생각했지만, 다 찾는 것이 아니라 계산해가면서 max값의 확률이 없으면 바로 빼버리자.

def func(n, k): # nPk가 nPn이 될 때까지..!
    # 만약에 지금 최대 확률보다 계산을 끝내기도전에 작아지거나 같아진다면
    # 완전 계산 후에는 무조건 같거나 작으므로 볼 필요도 없음. 
    # why? 확률은 무조건 1보다 작으니까 계산할 수록 같거나 작아지기만함.
    if maxV[0] <= maxV[1]:
        return 
    if n == k:
        maxV[1] = maxV[0] # 최댓값 갱신
        return
    for person in range(N):
        if vis[person]:
            continue
        temp_maxV = maxV[0]
        maxV[0] *= (arr[person][k]/100)
        vis[person] = 1
        func(n, k+1)
        vis[person] = 0
        maxV[0] = temp_maxV  # 확률이 0이었을 때는 zero division 오류 뜰까봐 그냥 temp에 저장.


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] # 행이 i번 열이 j번 일. 즉 arrij
    # 모든 순열을 다 찾아보면 시간초과남
    vis = [0]*N # 만약 이 사람이 이미 일을 한 사람이라면
    maxV = [1, 0] 
    # 최소 하나의 확률이 존재할텐데, 그 확률을 살펴보려면 1x확률 이어야하니까 일단 1로 
    # 확률의 최소는 0 최대 찾을 예정. 실제 최대값은 maxV[1]에, temp_maxV는 maxV[0]에
    func(N, 0)
    print("#{} {:0.6f}".format(tc, maxV[1]*100)) # 퍼센트 출력, 6째자리까지 출력
    