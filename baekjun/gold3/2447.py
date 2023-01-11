
def solution():
    # round = int(int(input()) ** (1/3))
    # print(round)

    now_pattern = "*"

    for _ in range(3):
        now_pattern = make_pattern(now_pattern)
        print("now_pattern ----------")
        print(now_pattern)


#문자열이여서 그림처럼 딱 잘라지는 형태가 아니다
    

# pattern  = "***\n* *\n***"
def make_pattern(b:str) -> str:
    return b + b + b + "\n" + b + " " + b + "\n" + b + b + b

print(make_pattern("*"))


solution()
