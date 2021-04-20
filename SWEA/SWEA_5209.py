# 5209
# 최소 생산 비용

def min_price(n, k):
    # 벌써 minV[1]에 저장된 것보다 비용이 많이 들면 더이상 볼 필요없음 

    # 동일해도 점점 + 로 커지기만하니까 stop!
    if minV[0] >= minV[1]:
        return
    if n == k:
        minV[1] = minV[0]
    for product in range(n):
        # 이미 생산한 제품이면 pass
        if vis_pd[product] == 1:
            continue
        # 일단 넣고 아니면 다른 거 넣어보기 --> 백트래킹!
        minV[0] += manip_lst[product][k]
        vis_pd[product] = 1
        min_price(n, k+1)
        vis_pd[product] = 0 # 아니면 다른 거 넣을거니까 ctrl z 되돌리기
        minV[0] -= manip_lst[product][k]
    

for tc in range(1, int(input())+1):
    N = int(input())
    manip_lst = [list(map(int, input().split())) for _ in range(N)]
    minV = [0, 9999999] # 임시 min과 최종 min 갱신
    vis_pd = [0]*N
    min_price(N, 0)    

    print("#{} {}".format(tc, minV[1]))