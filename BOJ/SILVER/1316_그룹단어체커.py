#그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
#단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

#입력
#첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

#출력
#첫째 줄에 그룹 단어의 개수를 출력한다.

#"jjkkkasd"는 이상 없는 그룹 단어이다. 
#"asdddbbbs"는 그룹 단어가 아니다. s가 따로 떨어졌다.
#각 문자들이 연속이 되거나 한 번만 등장하면 문제가 되지 않는다. 하지만 두 번째 예시처럼 s가 서로 떨어져있다. 이러면 연속되지 않음을 간주한다.

#happy
#new
#year
#3

#aba
#abab
#abcabc
#a
#1

#ab
#aa
#aca
#ba
#bb
#4 

#yzyzy
#zyzyz
#0

#z
#1

import sys
from collections import Counter

N = int(sys.stdin.readline())

grp_word_cnt = 0

for _ in range(0, N):
    
    input_string = sys.stdin.readline().rstrip()
    if max(list(Counter(input_string).values()))>1:
        if len(list(Counter(input_string))) == 1:
            # print("*GROUP WORD*")
            grp_word_cnt += 1
        else:    
            for i in range(0, len(input_string)):
                temp_string = input_string[i:]
                if len(temp_string) == 1:
                    # print("*GROUP WORD*")
                    grp_word_cnt += 1
                elif temp_string[0] == temp_string[1]:
                    if i == len(input_string):
                        # print("*GROUP WORD*")
                        grp_word_cnt += 1
                    continue
                elif temp_string[0] != temp_string[1]:
                    if temp_string[0] in temp_string[1:]:
                        # print(temp_string, temp_string[i])
                        break
    else:
        # print("*GROUP WORD*")
        grp_word_cnt += 1
    # print("GROUPWORD COUNT : ", grp_word_cnt)
print(grp_word_cnt)