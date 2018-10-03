import pickle
import time

"""
    재귀적으로 탐색해서 추가 데이터를 수집하기 위한 코드

"""

start_time = time.time()

# TODO
# 논문 : [논문 개수], 유전 알고리즘 관련 논문인가]
# 저자 : [{공저자들}, {논문들}, 유전 알고리즘 관련 저자인가]
# 유전 알고리즘 저자만 수집해서 리스트로 저장
# 리스트를 순회하면서 해당 저자의 공저자 리스트에서 공저자를 순회
# 공저자가 유전 알고리즘 관련 저자면 패스
# 공저자가 유전 알고리즘 관련 저자가 아니면 논문 리스트를 순회해서 유전 알고리즘 관련 논문이 있는지
EC_Keywords = ['evolutionary computation', 'genetic programming', 'genetic algorithm'
               'evolutionary computing', 'evolutionary programming', 'evolutionary algorithm'
               'ant colony optimization', 'aritifical immune systems', 'artificial life',
               'cultural algorithms', 'differential evolution', 'dual-phase evolution',
               'estimation of distribution algorithms', 'evolution strategy', 'gene expression programming',
               'grammatical evolution', 'learnable evolution model', 'learning classifier systems',
               'memetic algorithms', 'particle swarm optimization', 'swarm intelligence',
               'self-organization', 'self-organizing maps', 'competitive learning', 'fitness function']

with open('actor/actor90.pickle','rb') as f:
    actor_dict = pickle.load(f)

with open('paper/paper90.pickle', 'rb') as f:
    paper_dict = pickle.load(f)

EC_actor_list = []
EC_paper_list = [] # 유명 EC에 논문을 쓴 저자와 논문들, 변하면 안된다.
EC_actor_recursive_list = []
EC_paper_recursive_list = []

for k in actor_dict.keys():
    if actor_dict[k][2] == True:
        EC_actor_list.append(k) # 유명 EC에 논문을 쓴 저자
        Papers = list(actor_dict[k][1]) # 유명 EC에 논문을 쓴 저자의 논문 리스트

        for paper in Papers: # 해당 저자의 논문 리스트를 순회
            for keyword in EC_Keywords:
                if keyword in paper: # 키워드가 논문에 존재한다면
                    paper_dict[paper][1] = True
                    break # 키워드가 하나라도 존재하면 바로 유전 알고리즘 관련 논문이 된다.

for k in paper_dict.keys():
    if paper_dict[k][1] == True:
        EC_paper_list.append(k)

print('---Initial Sample---')
print(len(EC_actor_list))
print(len(EC_paper_list))
# EC_paper_list, EC_actor_list가 안 변함
# actor_dict과 paper_dict이 변했다.

def recursive_check(actor_dict, paper_dict, EC_actor, count):

    if count == 0:
        Papers = list(actor_dict[EC_actor][1])

        for paper in Papers:
            for keyword in EC_Keywords:
                if keyword in paper:
                    paper_dict[paper][1] = True
                    actor_dict[EC_actor][2] = True
                    break
        return

    else:
        actors = list(actor_dict[EC_actor][0]) # 공저자를 리스트로
        if(len(actors) == 0):
            Papers = list(actor_dict[EC_actor][1])

            for paper in Papers:
                for keyword in EC_Keywords:
                    if keyword in paper:
                        paper_dict[paper][1] = True
                        actor_dict[EC_actor][2] = True
                        break
            return;

        for actor in actors:
            recursive_check(actor_dict, paper_dict, actor, count-1)

for EC_actor in EC_actor_list:
    recursive_check(actor_dict, paper_dict, EC_actor, 3)


"""

for a in EC_actor_list: # EC에 논문을 하나라도 쓴 저자를 순회
    coauthors = list(actor_dict[a][0]) # 공저자들
    papers = list(actor_dict[a][1]) # 논문들

    for b in coauthors: # 해당 저자의 공저자를 순회
        if actor_dict[b][2] == True:
            # 큰 EC에 논문을 쓴 저자의 공저자 중 큰 EC에 논문을 쓴 저자
            pass
        else:
            papers = list(actor_dict[b][1]) # 공저자의 논문 집합
            for paper in papers:
                for keyword in EC_Keywords:
                    if keyword in paper:
                        paper_dict[paper][1] = True
                        actor_dict[b][2] = True
                        break

"""

for k in actor_dict.keys():
    if actor_dict[k][2] == True:
        EC_actor_recursive_list.append(k)

for k in paper_dict.keys():
    if paper_dict[k][1] == True:
        EC_paper_recursive_list.append(k)

print("---Final sample---")
print(len(EC_actor_recursive_list))
print(len(EC_paper_recursive_list))

end_time = time.time()

print("%s seconds" %(end_time - start_time))

with open('./actor-recursive-3/actor90.pickle', 'wb') as handle:
    pickle.dump(actor_dict, handle)

with open('./paper-recursive-3/paper90.pickle', 'wb') as handle:
    pickle.dump(paper_dict, handle)


#Initial_actor_dict[a][0] = Initial_actor_dict[a][0] | diff
#Initial_actor_dict[a][1] = Initial_actor_dict[a][1] | {title}
#Initial_actor_dict[a][2] = Initial_actor_dict[a][2] or isInitial

#Initial_actor_dict[a] = [set(author_array) - {a}, {title}, isInitial]

