# 1231
# 중위 순회

# 10 개의 테스트 케이스
def inorder_traverse(node):
    # 중위 순회 : LVR left - root - right 순서대로 읽기
    if node <= N:
        inorder_traverse(node*2)
        answer.append(tree[node])
        inorder_traverse(node*2+1)

for tc in range(1, 11):
    N = int(input()) # 트리가 갖는 정점의 총 수
    child_1 = [0] * (N+1)
    child_2 = [0] * (N+1)
    tree = ['_']*(N+1)
    # 트리 저장 
    for i in range(N):
        # N, root, left_child, right_child 로 받으면 좋지만 자식이 하나이거나 없을 수도 있어서..
        arr  = list(input().split())
        N = int(arr[0])
        tree[N] = arr[1]
        if len(arr) > 2:
            child_1[N] = int(arr[2])
        if len(arr) > 3:
            child_2[N] = int(arr[3])
    answer = []
    inorder_traverse(1)
    print("#{} {}".format(tc, "".join(answer)))

