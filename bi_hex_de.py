
# 10 -> n진수 
def dem_to_n(num, n):
    
    rev_base = ''

    while num > 0:
        num , remainder = divmod(num, n)
        rev_base += str(remainder)

    return rev_base[::-1]


#n진수 -> 10 
def n_to_dem(num, n):
    
    demical = 0

    for i, val in enumerate(num[::-1]):
        demical += (n ** i) * int(val)
    
    return demical

    

print(dem_to_n(10, 2))

print(n_to_dem('1010', 2))