# def add(b, c):
#     return[b, c]
# var = add(3, 4)
# print(var[0],var[1])
# print(var[0]+var[1])
# def sub(a,b):
#     return(a, b)
# a,b=add(2,5)
# print(a*b)
# ab =add(2,3)
# print(ab)
# var = print("hi")
# var = print("hello")
# var = print("Hi sir")
# n = int(input("enter the range:"))
# for i in range(n):
#     for j in range(i):
#         print("* ", end =' ')
#     print("\r")

# for i in range(n):
#     print("  "*(n-i), " *"*(i))

# for i in range(n):
#     print(" "*(n-i), " *"*i)
# for i in range(n):
#     print(" "*(i), " *"*(n-i))

# for i in range(n):
#     print(" "*(i), " *"*(n-i))    

# for i in range(n):
#     print(" *"*(n-i)," "*(i))

# for i in range(n):
#     print(" *"*(i)," "*(i))


# matrix
# a = [[2,2],[2,2]]
# b = [[3,3],[3,3]]
# res = [[0,0],
#        [0,0]]
# e=[]
# # print(a+b)
# for i in range(len(a)):
#     f=[]
#     for j in range(len(b)):
#         c=0
#         for k in range(len(b)):
#         # print(a[i][j]+b[i][j])
#         # print(a[i][j]-b[i][j],end = ' ')
#         # print("\r")
#             c += a[i][k]*b[k][j]
#         f.append(c)
#     e.append(f)
# print(e)

c = [[1,2,3],
     [4,5,6],
     [7,8,9]]
d = [[5,6,7],
     [8,9,10],
     [11,12,13]]

n=[]
for i in range(len(c)):
    l=[]
    for j in range(len(d)):
        m=0
        for k in range(len(d)):
            m += c[i][k]*d[k][j]
        l.append(m)
    n.append(l)
print(n)
    

