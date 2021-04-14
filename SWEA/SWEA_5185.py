# 16 진수는 1자리 2진수 4자리로 표시된다.
# N자리 16 진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오

# 2진수의 앞자리도 0을 반드시 출력할 것!
# 예를 들어 47FE = 0100011111111110

def base_binary(hexa_num):
    temp_binary = []
    # 2진법으로 변환 하는 법 --> 2로 계속 나누면서 나머지값 을 끝에서부터 넣기
    while hexa_num > 1:
        temp_binary.append(hexa_num%2)
        hexa_num //= 2
    temp_binary.append(hexa_num)
    while len(temp_binary) != 4:
        temp_binary.append(0)
    # 처음 나머지 부터 넣었지만 2진법은 뒤에서 부터 넣어야하므로 뒤집어주기
    for i in range(3, -1, -1):
        ans.append(temp_binary[i])


for tc in range(1, int(input())+1):
    hexadecimal_dic = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15 
    }
    ans = []
    num_length, num_hexadecimal = input().split()
    num_length = int(num_length)
    for i in range(num_length):
        # 16 진법의 수를 한자리씩 넣기
        base_binary(hexadecimal_dic[num_hexadecimal[i]])
    print("#{} {}".format(tc, "".join(map(str,ans))))
    # join method는 string list 에만 가능하므로 map 을 이용하여 str로 바꿔준 뒤 사용해야함.