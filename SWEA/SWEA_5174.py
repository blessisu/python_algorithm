# subtree
# 주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수

# 입력
# 테스트케이스 T
# 간선의 개수 E 노드 번호 N
# E 개의 : 부모 - 노드 번호쌍
# 노드 번호 1 ~ E

# 출력
# N을 루트 노드로 하는 트리의 총 노드 개수

def counting_tree(node):
    global cnt
    cnt += 1
    if child_1[node] != 0:
        counting_tree(child_1[node])
    if child_2[node] != 0:
        counting_tree(child_2[node])
        
    return cnt 


for tc in range(1, int(input()) + 1):
    E, N = map(int, input().split())
    # 0 번 노드는 비어있으니 1 개추가하고, E+1 개있으니 총 E+2 개 주의
    child_1 = [0] * (E+2)
    child_2 = [0] * (E+2)
    arr = list(map(int, input().split()))
    for i in range(0, 2*E, 2):
        if child_1[arr[i]] == 0:
            child_1[arr[i]] = arr[i+1]
        else:
            child_2[arr[i]] = arr[i+1]
    
    cnt = 0
    print("#{} {}".format(tc, counting_tree(N)))      