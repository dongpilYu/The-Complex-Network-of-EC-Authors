import pickle

sum1_a = 0
sum1_b = 0
idx1 = 0

sum2_a = 0
sum2_b = 0
idx2 = 0

sum3_a = 0
sum3_b = 0
idx3 = 0

sum4_a = 0
sum4_b = 0
idx4 = 0

sum5_a = 0
sum5_b = 0
idx5 = 0

with open('actor-recursive-3/actor80.pickle','rb') as f:
    actor_dict = pickle.load(f)

for k in actor_dict.keys():
    if actor_dict[k][2] == True:
        coauthors = list(actor_dict[k][0])
        if len(coauthors) == 0:
            pass
        else:
            for coauthor in coauthors:
                if actor_dict[coauthor][2] == True:
                    sum1_a = sum1_a + 1
        idx1 = idx1 + 1

        sum1_b = sum1_b + len(list(actor_dict[k][1]))

print("80: \n")
print(sum1_a/idx1) # 저자 당 공저자 수
print(sum1_b/idx1) # 저자 당 논문 수

with open('actor-recursive-3/actor90.pickle','rb') as f:
    actor_dict = pickle.load(f)

for k in actor_dict.keys():
    if actor_dict[k][2] == True:
        coauthors = list(actor_dict[k][0])
        if len(coauthors) == 0:
            pass
        else:
            for coauthor in coauthors:
                if actor_dict[coauthor][2] == True:
                    sum2_a = sum2_a + 1
        idx2 = idx2 + 1

        sum2_b = sum2_b + len(list(actor_dict[k][1]))

print("90: \n")
print(sum2_a/idx2)
print(sum2_b/idx2)

with open('actor-recursive-3/actor00.pickle','rb') as f:
    actor_dict = pickle.load(f)

for k in actor_dict.keys():
    if actor_dict[k][2] == True:
        coauthors = list(actor_dict[k][0])
        if len(coauthors) == 0:
            pass
        else:
            for coauthor in coauthors:
                if actor_dict[coauthor][2] == True:
                    sum3_a = sum3_a + 1
        idx3 = idx3 + 1

        sum3_b = sum3_b + len(list(actor_dict[k][1]))

print("00: \n")
print(sum3_a/idx3)
print(sum3_b/idx3)

with open('actor-recursive-2/actor10.pickle','rb') as f:
    actor_dict = pickle.load(f)

for k in actor_dict.keys():
    if actor_dict[k][2] == True:
        coauthors = list(actor_dict[k][0])
        if len(coauthors) == 0:
            pass
        else:
            for coauthor in coauthors:
                if actor_dict[coauthor][2] == True:
                    sum4_a = sum4_a + 1
        idx4 = idx4 + 1

        sum4_b = sum4_b + len(list(actor_dict[k][1]))

print("10: \n")
print(sum4_a/idx4)
print(sum4_b/idx4)

print((sum1_a+sum2_a+sum3_a+sum4_a)/(idx1+idx2+idx3+idx4))
print((sum1_b+sum2_b+sum3_b+sum4_b)/(idx1+idx2+idx3+idx4))

print((sum4_a+sum3_a+sum2_a)/(idx1+idx2+idx3))
print((sum4_b+sum3_b+sum2_b)/(idx1+idx2+idx3))

print("----------")

print(idx1)
print(idx2)
print(idx3)
print(idx4)

print(idx4+idx3+idx2)
print(idx4+idx3+idx2+idx1)