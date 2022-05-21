#print(0b000)
#print(bin(0b000 | 1 << 1))


#값 추가 
now = 0
now += 1 << 2
print(now)
now += 1 << 2
print(now)
now -= 1 << 2 
print(now)


now +=  1 << 4


print(bin(now))

#toggle
now ^= 1 << 5
print(bin(now))

#값 존재 여부
print(now & (1 << 3)) # 없음
print(now & (1 << 2)) # 있음 

print()