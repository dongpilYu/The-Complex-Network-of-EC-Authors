import pickle
import csv

sum4_a = 0
sum4_b = 0
idx4 = 0

sum5_a = 0
sum5_b = 0
idx5 = 0

sum1_a = 0
sum1_b = 0
idx1 = 0

sum2_a = 0
sum2_b = 0
idx2 = 0

sum3_a = 0
sum3_b = 0
idx3 = 0

with open('actor/actor70.pickle','rb') as f:
    actor_dict = pickle.load(f)

with open('./csv/only-CS-actor70.csv', 'w', encoding='utf-8', newline='') as csvFile:
    wr = csv.writer(csvFile, delimiter=',')
    for k in actor_dict.keys():
        idx5 = idx5 + 1
        coauthors = list(actor_dict[k][0])
        if len(coauthors) == 0:
            pass
        else:
            for coauthor in coauthors:
                sum5_a = sum5_a + 1
                edge = [k, coauthor]
                wr.writerow(edge)

        sum5_b = sum5_b + len(list(actor_dict[k][1]))

with open('actor/actor80.pickle','rb') as f:
    actor_dict = pickle.load(f)

with open('./csv/only-CS-actor80.csv', 'w', encoding='utf-8', newline='') as csvFile:
    wr = csv.writer(csvFile, delimiter=',')
    for k in actor_dict.keys():
        idx4 = idx4 + 1
        coauthors = list(actor_dict[k][0])
        if len(coauthors) == 0:
            pass
        else:
            for coauthor in coauthors:
                sum4_a = sum4_a + 1
                edge = [k, coauthor]
                wr.writerow(edge)
        sum4_b = sum4_b + len(list(actor_dict[k][1]))

with open('actor-recursive-2/actor10.pickle','rb') as f:
    actor_dict = pickle.load(f)

with open('./csv/only-CS-actor10.csv', 'w', encoding='utf-8', newline='') as csvFile:
    wr = csv.writer(csvFile, delimiter=',')
    for k in actor_dict.keys():
        idx1 = idx1 + 1
        coauthors = list(actor_dict[k][0])
        if len(coauthors) == 0:
            pass
        else:
            for coauthor in coauthors:
                sum1_a= sum1_a + 1
                edge = [k, coauthor]
                wr.writerow(edge)
        sum1_b = sum1_b + len(list(actor_dict[k][1]))

with open('actor-recursive-3/actor00.pickle','rb') as f:
    actor_dict = pickle.load(f)

with open('./csv/only-CS-actor00.csv', 'w', encoding='utf-8', newline='') as csvFile:
    wr = csv.writer(csvFile, delimiter=',')
    for k in actor_dict.keys():
        idx2 = idx2 + 1
        coauthors = list(actor_dict[k][0])
        if len(coauthors) == 0:
            pass
        else:
            for coauthor in coauthors:
                sum2_a = sum2_a + 1
                edge = [k, coauthor]
                wr.writerow(edge)
        sum2_b = sum2_b + len(list(actor_dict[k][1]))

with open('actor-recursive-3/actor90.pickle','rb') as f:
    actor_dict = pickle.load(f)

with open('./csv/only-CS-actor90.csv', 'w', encoding='utf-8', newline='') as csvFile:
    wr = csv.writer(csvFile, delimiter=',')
    for k in actor_dict.keys():
        idx3 = idx3 + 1
        coauthors = list(actor_dict[k][0])
        if len(coauthors) == 0:
            pass
        else:
            for coauthor in coauthors:
                sum3_a = sum3_a + 1
                edge = [k, coauthor]
                wr.writerow(edge)
        sum3_b = sum3_b + len(list(actor_dict[k][1]))


print("---")
print(sum5_b/idx5) # 저자 당 논문 수
print(sum5_a/idx5) # 저자 당 공저자 수
print(idx5) # 저자 수

print(sum4_b/idx4)
print(sum4_a/idx4)
print(idx4)

print(sum1_b/idx1)
print(sum1_a/idx1)
print(idx1)

print(sum2_b/idx2)
print(sum2_a/idx2)
print(idx2)

print(sum3_b/idx3)
print(sum3_a/idx3)
print(idx3)
print("---")

print((sum1_a+sum2_a+sum3_a+sum4_a+sum5_a)/(idx1+idx2+idx3+idx4+idx5))
print((sum1_b+sum2_b+sum3_b+sum4_b+sum5_b)/(idx1+idx2+idx3+idx4+idx5))

print((sum1_a+sum2_a+sum3_a)/(idx1+idx2+idx3))
print((sum1_b+sum2_b+sum3_b)/(idx1+idx2+idx3))
