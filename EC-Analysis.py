import pickle
import csv

sum = 0
idx = 0

with open('actor/actor80.pickle','rb') as f:
    actor_dict = pickle.load(f)

with open('./csv/only-EC-actor80.csv', 'w', encoding='utf-8', newline='') as csvFile:
    wr = csv.writer(csvFile, delimiter=',')
    for k in actor_dict.keys():
        if actor_dict[k][2] == True:
            idx = idx + 1
            coauthors = list(actor_dict[k][0])
            if len(coauthors) == 0:
                pass
            else:
                for coauthor in coauthors:
                    if actor_dict[coauthor][2] == True:
                        sum = sum + 1
                        edge = [k, coauthor]
                        wr.writerow(edge)

with open('actor/actor70.pickle','rb') as f:
    actor_dict = pickle.load(f)

with open('./csv/only-EC-actor70.csv', 'w', encoding='utf-8', newline='') as csvFile:
    wr = csv.writer(csvFile, delimiter=',')
    for k in actor_dict.keys():
        if actor_dict[k][2] == True:
            idx = idx + 1
            coauthors = list(actor_dict[k][0])
            if len(coauthors) == 0:
                pass
            else:
                for coauthor in coauthors:
                    if actor_dict[coauthor][2] == True:
                        sum = sum + 1
                        edge = [k, coauthor]
                        wr.writerow(edge)

"""
with open('actor-recursive-3/actor00.pickle','rb') as f:
    actor_dict = pickle.load(f)

with open('./csv/only-EC-actor00.csv', 'w', encoding='utf-8', newline='') as csvFile:
    wr = csv.writer(csvFile, delimiter=',')
    for k in actor_dict.keys():
        if actor_dict[k][2] == True:
            idx = idx + 1
            coauthors = list(actor_dict[k][0])
            if len(coauthors) == 0:
                pass
            else:
                for coauthor in coauthors:
                    if actor_dict[coauthor][2] == True:
                        sum = sum + 1
                        edge = [k, coauthor]
                        wr.writerow(edge)

with open('actor-recursive-3/actor90.pickle','rb') as f:
    actor_dict = pickle.load(f)

with open('./csv/only-EC-actor90.csv', 'w', encoding='utf-8', newline='') as csvFile:
    wr = csv.writer(csvFile, delimiter=',')
    for k in actor_dict.keys():
        if actor_dict[k][2] == True:
            idx = idx + 1
            coauthors = list(actor_dict[k][0])
            if len(coauthors) == 0:
                pass
            else:
                for coauthor in coauthors:
                    if actor_dict[coauthor][2] == True:
                        sum = sum + 1
                        edge = [k, coauthor]
                        wr.writerow(edge)
"""