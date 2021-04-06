# 5177
# 이진 힙

# 최소힙 : 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가
# 부모노드 < 자식 노드 를 유지. 새로 추가된 노드의 값이 조건에 맞지 않는 경우 만족할 때까지 부모랑 자리 바꾸기
# 부모노드 --> 자식의 N//2
# 조상 노드의 모든 합 구하기!

def min_heap_ancestor_sum(idx):
    global answer
    if idx == 1:
        return
    print(f'idx는 {idx} idx//2는 {idx//2} min_heap[idx//2]은 {min_heap[idx//2]}')
    # 자신의 부모 노드 계속 더하기
    answer += min_heap[idx//2]
    min_heap_ancestor_sum(idx//2)

def min_heap_sort(idx):
    if idx <  2:
        return
    if min_heap[idx//2] > min_heap[idx]:
        min_heap[idx//2], min_heap[idx] = min_heap[idx], min_heap[idx//2]
        min_heap_sort(idx//2)


for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_heap = [0]
    length_arr = len(arr)
    for i in range(length_arr):
        if arr[i] not in min_heap:
            min_heap.append(arr[i])
            min_heap_sort(i+1)
    answer = 0
    min_heap_ancestor_sum(length_arr)
    print("#{} {}".format(tc, answer))