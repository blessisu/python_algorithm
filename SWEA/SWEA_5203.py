# 5203
# baby gin

# 교대로 카드를 가져가면서, 누구라도 먼저 run(연속 3자리) or triplet(같은 숫자 3개) 

def run_or_tri(arr):
    for i in range(10):
        # 한 숫자 카드가 세 장이 되면 triplet이므로 return true(카드 한 장 얻을 때마다 검사하므로 세 장 초과는 존재하지 않음)
        if arr[i] == 3:
            return True
    for i in range(8):
        # 연속 되는 세 숫자 카드가 존재하면 run이므로 return true
        if arr[i] > 0 and arr[i+1] > 0 and arr[i+2] > 0:
            return True
    # run도, triplet도 안될 경우 false 를 return
    return False


for tc in range(1, int(input())+1):
    card_lst = list(map(int, input().split()))
    # 플레이어가 0~9 카드를 몇 개 가지고 있는지 저장하는 list
    player1 = [0]*10
    player2 = [0]*10
    # 만약 12장 뽑을 때까지 승리자가 나오지않으면 무승부이므로 ans 에 무승부를 저장하고 시작
    ans = 0
    for i in range(12):
        # i가 짝수일 때는 player1 이 가져가는 카드임
        # 카드를 하나 가져갈 때마다, run 이나 triplet이 되는 지 확인해주기
        if i%2==0:
            player1[card_lst[i]] += 1
            # run이나 triplet 을 찾으면 ans에 승리한 플레이어를 저장하고 더이상 카드를 뽑지 않아도 됨
            if run_or_tri(player1):
                ans = 1
                break
        # i가 홀수면 player2의 카드
        else:
            player2[card_lst[i]] += 1
            if run_or_tri(player2):
                ans = 2
                break
    print("#{} {}".format(tc, ans))
        