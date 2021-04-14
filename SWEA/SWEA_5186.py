# 0보다 크고 1보다는 작은 십진수 N을 이진수로 변환
# 0.625 = 0.101

# 이진수로 표현할 수 있으면 0. 을 제외한 나머지 부분 출력
# 13자리 이상 필요한 경우 "overflow" 출력
def float_to_binary(num, bin_num):
    if len(ans) > 13 or num == 0.0 :
        return
    # 여기서 num이 0.5여도 bin_num 0.5를 빼줄 수 있도록 equal 넣기!
    if num >= bin_num:
        num -= bin_num
        ans.append(1)
    else:
        ans.append(0)
    
    float_to_binary(num, bin_num*0.5)
    # 이진법은 0.5 (2^-1 씩 증가)

for tc in range(1, int(input())+1):
    float_num = float(input())
    ans = []
    float_to_binary(float_num, 0.5)
    # 0.111111 에서 소수 첫 자리는 0.5 둘째 자리는 0.5*0.5 ... 
    # 2^-1 = 1/2 2^-2 = 1/2 * 1/2 ... 이기 때문에
    if len(ans) <= 12:
        print("#{} {}".format(tc, "".join(map(str, ans))))
    else:
        print("#{} overflow".format(tc))