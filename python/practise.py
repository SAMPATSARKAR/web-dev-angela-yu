def generate_inverted_pyramid(n):
    lst=[]
    for i in range(n+1):
        a = ' '*(i) + '*'* (2*n-2*i) + ' '*(i)  
        lst.append(a)
    return lst 
    
print(generate_inverted_pyramid(3))
print(generate_inverted_pyramid(5))