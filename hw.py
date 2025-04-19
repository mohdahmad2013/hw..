def square (s,e):
    list=[]
    for i in range (s,e):
        list.append(i**2)
    even=[]
    odd=[]
    for i in list:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)

    print("Even squares are ",even)
    print("Odd squares are ",odd)
square(1,10)