# o = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# g = [[1,2],
#      [4,5]]
# for i in range(1,11):
#      for g in range(1,11):
#           print(i*g)
# for i in range(1,6):
#      for g in range(1,6):
#           print(i*g,end="\t")
#      print()



r = []
def num(*n):
     r.extend(n)
     return sum(r)
print(num(1,1,2,3,3,3,3,3,5,8,8,8,8,8))