#print(0b000)
#print(bin(0b000 | 1 << 1))


#값 추가 
now = 1 << 1
now += 1 << 2
now +=  1 << 4

now += ~(1 << 2)

print(bin(now))

#toggle
now ^= 1 << 5
print(bin(now))

#값 존재 여부
print(now & (1 << 3)) # 없음
print(now & (1 << 2)) # 있음 

