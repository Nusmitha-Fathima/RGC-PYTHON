def isPrime(n):  #m3
    if n == 1 or n == 0:   #1,
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return  True

N = int(input("enter a positive integer:" ))
for i in range(1, N + 1): # 1,2,3,4,5,6,7
    if isPrime(i):
        print(i, end=" ")







# def my_func(a,b,c):
#     return ( a+b-c)

# print(my_func(8,3,4))


# name="nusmitha\nfathima"
# print(name)
# import re
# print(re.findall(r'\s',name))


# txt="""As the hype around AI has accelerated, vendors have been scrambling to promote how their
#  products and services use it. Often, what they refer to as AI is simply 
#  a component of the technology, such as machine learning. AI requires
#    a foundation of specialized hardware and software for writing
#      and training machine learning algorithms. No single programming 
#      language is synonymous with AI, but Python, R, Java, C++ and Julia have features
#        popular with AI developers."""
# print(re.findall(r'\bp\w+\b',txt))

