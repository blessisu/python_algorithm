# 테스트 케이스는 10개
# 첫 줄 총 점 N개
# 정점이 수이면, 정점 번호와 양의 정수
# 연산자면 정점번호 - 연산자 - 왼쪽 자식 번호 - 오른쪽 자식 번호
# 루트 정점 번호는 반드시 1
# 사칙연산 + - / * 만 가능

# Left_Right_Root 순으로 방문
def postorder_traverse(node):
    global N
    if node <= N:
        if type(tree[node][1]) == int:
            print(f"리턴 합니당. {node}번의 수는 {tree[node][1]}")
            return tree[node][1]
        if type(tree[node][1]) == str:
            left_child = tree[node][2]
            right_child = tree[node][3]
            postorder_traverse(tree[node][2])
            postorder_traverse(tree[node][3])

            if tree[node][1] == '+':
                tree[node][1] = tree[left_child][1] + tree[right_child][1]
            elif tree[node][1] == '-':
                tree[node][1] = tree[left_child][1] - tree[right_child][1]
            elif tree[node][1] == '*':
                tree[node][1] = tree[left_child][1] * tree[right_child][1]
            elif tree[node][1] == '/':
                tree[node][1] = tree[left_child][1] // tree[right_child][1]
        print(f" 덧셈합니당. {node}번의 수는 {tree[node][1]}")
        return tree[node][1]


for tc in range(1, 11):
    N = int(input())
    tree = [[0]*4 for _ in range(N+1)]
    for i in range(N):
        tree_info = input().split()
        tree_num = int(tree_info[0])
        if len(tree_info) == 2:
            tree[tree_num][1] = int(tree_info[1])
        else:
            tree[tree_num][1] = tree_info[1]
            tree[tree_num][2] = int(tree_info[2])
            tree[tree_num][3] = int(tree_info[3])

    postorder_traverse(1)
    print("#{} {}".format(tc, tree[1][1]))