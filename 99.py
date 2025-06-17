grades = []
print(len(grades))
grades.append(90)
grades.append(80)
grades.append(65)
grades.append(75)
grades.append(99)
print(grades)
print(len(grades))
print(grades[0])
grades[0] ,grades[4] =grades[4],grades[0]
print(grades)
names = ["a","b","c","d","e"]
grades_and_names = [grades[0] , names[0] ,grades[1] ,names[1] ,grades[2],names[2],grades[3], names[3],grades[4],names[4]]
print(grades_and_names)
print((len(grades_and_names)))
print(grades_and_names[0])
