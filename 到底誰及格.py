eng={1,2,4,6,8,9}
math={1,3,5,6,8,10}
all={1,2,3,4,5,6,7,8,9,10}
s1=eng-math
print(s1,"英文及格但數學不及格的")

s2=math-eng
print(s2,"數學及格但英文不及格的")

s3=math & eng
print(s3,"都及格的")

s4=all -math-eng
print(s4,"都不及格的")

s5=all-s3-s4
print(s5,"只有及格一科的")
