# 5178 
# 노드의 합

def tree_sum(node): 
    global N, L
    if node > N:
        return 0

    if tree[node]:
        return tree[node]
    
    tree[node] = tree_sum(node*2) + tree_sum(node*2+1)
    return tree[node]
    # 바로 윗줄 'return tree[node]'으로 리턴 값을 넣어주지 않으면
    # 처음에 tree_sum(4) tree_sum(5) 를 호출 했는데
    # tree_sum(4)도 tree_sum(8)+tree_sum(9)로 계산하는 것 이기때문에 계산만하고
    # 함수자체는 NoneType 을 return 하므로 결국 tree[2] 는 NoneType + NoneType 이 되서
    # Type error 가 발생한다.
    # 아마 C++ 이었으면, return tree[node] = tree_sum(node*2) + tree_sum(node*2+1) 로 작성하여
    # 더해준 값을 바로 return 해주기 때문에
    # 결국 tree[node] = tree_sum(node*2) + tree_sum(node*2+1), return tree[node]를 해준 것인데
    # 이는 내부적으로 C++ 이 해당 코드를 해석해서 해주기 때문이고, 파이썬은 직접 해줘야해서
    # 나눠 작성이 필요한 부분으로 보임.


for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split()) # N은 노드 개수 M은 리프노드 개수 L은 출력할 노드 번호
    tree = [0] * (N + 1)
    for i in range(M):
        node_num, node_value = map(int, input().split())
        tree[node_num] = node_value
    
    # 끝에서부터 구하려니까 너무 어려워서..
    # 원하는 노드부터 내려가되, 재귀를 돌아서 아래서부터 더하게 하자..!
    tree_sum(L)
    print("#{} {}".format(tc, tree[L]))
        
    
    