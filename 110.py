#for i in range(50):
    #if i % 2 == 0:
        #if i % 3 == 0:
            #if i >= 6:
               #print(i)
from os import remove

# gradse = {
#     "dana":[88,92,100],
#     "eli":[75,78,80],
#     "noa":[90,90,90],
#     "tomer":[95,99,100],
#     "lior":[60,65,70]
#}
#for name, numbers in gradse.items():
    #if sum(numbers) >= 3*90:
        #print(name)

# new_dict = {}
# for name,numbers in gradse.items():
#     average = sum(numbers)/len(numbers)
#     if average >= 90:
#         new_dict[name] = average
# print(new_dict)
#
#
#
#
#
#
#
# gradse1={}
# gradse1["dana"] = sum(gradse["dana"])/len(gradse["dana"])
# gradse1["eli"] = sum(gradse["eli"])/len(gradse["dana"])
# gradse1["noa"] = sum(gradse["noa"])/len(gradse["noa"])
# gradse1["tomer"] = sum(gradse["tomer"])/len(gradse["tomer"])
# gradse1["lior"] = sum(gradse["lior"])/len(gradse["lior"])
#for name,i in gradse1.items():
#     if i >= 90:
#
#         print(name,":",i )
#
#
# p = 10
# while p > 6:
#     print("7")
#     p -= 1
#
# k = []
# v = []
#
# f = {"t":105, "h":102,"j":205}
# for i , r in f.items():
#    k.append(i)
#    v.append(r)
# print(k)
#print(v)
# y = {"a":0,"b":1,"c":2,"d": 1}
# r ={}
# for a ,b in y.items():
#     if b in r:
#         r[b].append(a)
#     else:
#        r[b] = [a]
# print(r)
#
#
#
# arr = ["a","c","d","s"]
#for a in arr:
   # print(a,a, sep = "\n")
# k =list(range(100))
# print(k)
# arr = ["a","c","d",'s']
# for i in range(len(arr)):
#     print(arr[i],arr[i])


# a = ["a","c","d",'s']
# for i in range(len(a)):
#     if a[i] != a[-1]:
#        print(a[i],a[i+1])
#     else:
#         print(a[i])



r =[]
w = [1,4,7,6,9,34]
for i in range (len(w)):
    if w[i] % 2 == 0:
        r.append(w[i]//2)
    else:
        r.append(w[i])
print(r)







e =[]
y = [10,6,7,8,9,35,86,72,]
for i in range(len(y)):
    if y[i] %2 ==0:
        e.append(y[i]//2)
    else:
        e.append(y[i])
print(e)



















