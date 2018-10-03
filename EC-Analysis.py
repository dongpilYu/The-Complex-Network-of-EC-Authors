#-*-coding: utf-8-*-

import pickle
import csv

sum = 0
idx = 0

"""
    이 코드는 한국인 저자만을 위한 네트워크를 만들기 위해
    2018-09-28에 수정되었습니다.

    경로 ./csv/only-EC-actor.csv -> ./csv/only-EC-KR-actor.csv
    파일 이름만 달라졌지, 딕셔너리 파일은 같은 것을 읽습니다.
    
    첫 번째 IF 문에서 유전 알고리즘 관련 저자이면서 한국인이도록 하고
    두 번째 IF 문에서 공저자가 유전 알고리즘 저자이면서 한국이도록 한다.

    actor70, actor80은 합쳐서 유전 알고리즘 분야 한국인 저자가 한 명 뿐이므로 
    코드가 수정된 부분이 없다.
"""

""" 
with open('actor-recursive-3/actor70.pickle','rb') as f:
    actor_dict = pickle.load(f)

with open('./csv/only-EC-KR-actor70.csv', 'w', encoding='utf-8', newline='') as csvFile:
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

with open('actor-recursive-3/actor80.pickle','rb') as f:
    actor_dict = pickle.load(f)

kr_actor80 = []
with open('KR/kr-author80.txt','rb') as kr:
    while True:
        line = kr.readline()
        if not line:
            break
        kr-actor80.append(line)

with open('./csv/only-EC-KR-actor80.csv', 'w', encoding='utf-8', newline='') as csvFile:
    wr = csv.writer(csvFile, delimiter=',')
    for k in actor_dict.keys():
        if actor_dict[k][2] == True and k in kr-actor80: # 유전 알고리즘 관련 저자
            idx = idx + 1
            coauthors = list(actor_dict[k][0])
            if len(coauthors) == 0:
                pass
            else:
                for coauthor in coauthors:
                    if actor_dict[coauthor][2] == True and coauthor in kr-actor80: 
                        # 유전 알고리즘 관련 저자의 공저자 중 유전 알고리즘 관련 저자
                        sum = sum + 1
                        edge = [k, coauthor]
                        wr.writerow(edge)
"""

with open('actor-recursive-3/actor90.pickle','rb') as f:
    actor_dict = pickle.load(f)

kr_actor90 = []
with open('KR/kr-author90.txt','r') as kr:
    while True:
        line = kr.readline()
        if not line:
            break
        line = line.split('\n')[0]
        kr_actor90.append(line)

with open('./csv/only-EC-KR-actor90.csv', 'w', encoding='utf-8', newline='') as csvFile:
    wr = csv.writer(csvFile, delimiter=',')
    for k in actor_dict.keys():
        
        if actor_dict[k][2] == True and any(k in s for s in kr_actor90):
            idx = idx + 1
            coauthors = list(actor_dict[k][0])
            if len(coauthors) == 0:
                pass
            else:
                for coauthor in coauthors:
                    if actor_dict[coauthor][2] == True and any(coauthor in s for s in kr_actor90):
                        sum = sum + 1
                        edge = [k, coauthor]
                        wr.writerow(edge)

"""
with open('actor-recursive-3/actor00.pickle','rb') as f:
    actor_dict = pickle.load(f) # 00~10 년대의 딕셔너리를 가져온다.
 
kr_actor00 = []
with open('KR/kr-author00.txt','r') as kr:
    while True:
        line = kr.readline()
        if not line:

            break
        line = line.split('\n')[0]
        kr_actor00.append(line)


with open('./csv/only-EC-KR-actor00.csv', 'w', encoding='utf-8', newline='') as csvFile:
    wr = csv.writer(csvFile, delimiter=',')
    for k in actor_dict.keys():
        if actor_dict[k][2] == True and any(k in s for s in kr_actor00): # 유전 알고리즘 관련 저자
            idx = idx + 1
            coauthors = list(actor_dict[k][0])
            if len(coauthors) == 0:
                pass
            else:
                for coauthor in coauthors:
                    if actor_dict[coauthor][2] == True and any(coauthor in s for s in kr_actor00):
                        sum = sum + 1
                        edge = [k, coauthor]
                        wr.writerow(edge)

"""
"""
with open('actor-recursive-2/actor10.pickle','rb') as f:
    actor_dict = pickle.load(f)

kr_actor10 = []
with open('KR/kr-author10.txt','r') as kr:
    while True:
        line = kr.readline()
        if not line:
            break
        kr_actor10.append(line)

with open('./csv/only-EC-KR-actor10.csv', 'w', encoding='utf-8', newline='') as csvFile:
    wr = csv.writer(csvFile, delimiter=',')
    for k in actor_dict.keys():
        if actor_dict[k][2] == True and any(k in s for s in kr_actor10):
            idx = idx + 1
            coauthors = list(actor_dict[k][0])
            if len(coauthors) == 0:
                pass
            else:
                for coauthor in coauthors:
                    if actor_dict[coauthor][2] == True and any(coauthor in s for s in kr_actor10):
                        sum = sum + 1
                        edge = [k, coauthor]
                        wr.writerow(edge)
"""
