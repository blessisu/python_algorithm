# 5176
# 이진탐색

# Testcast T
# 1부터 N까지 자연수를 이진 탐색 트리에 저장, N

# 가장 왼쪽 아래의 노드는
# 완전 이진 트리의 레벨이 i 일 때 2^i 번

def complete_binary_tree(root):
    global value
    global N
    # 왼쪽 먼저, 루트, 오른쪽 순으로 처리해야 하니까 순서대로

    # root > N 일 때 return 해버리면, 왼쪽 노드에서 root가 N보다 커질 때 멈춰 버려서 오른쪽 검사 안할 수도 있음
    # root <= N 인 경우만 재귀함수가 돌게 되면, 일단 root <= N 까지만 tree[root] = value 가 실행됨
    # 그리고 그 뒤로 남은 root 들은 다시 root <= N 에 걸려서 실행되지 않고 
    # 딱 root <= N 까지만 트리가 만들어짐.
    if root <= N:
        complete_binary_tree(root*2)
        tree[root] = value
        value += 1
        complete_binary_tree(root*2 + 1)


for tc in range(1, int(input())+1):
    N = int(input())
    tree = [0] * (N+1)
    
    # 가장 작은 수부터 넣을 건데, 가장 왼쪽 아래부터 넣기
    value = 1  # 작은 수부터 넣을거니까
    complete_binary_tree(1)
    print("#{} {} {}".format(tc, tree[1], tree[N//2]))

      