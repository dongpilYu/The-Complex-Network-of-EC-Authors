"""
    내가 프로젝트에서 진행해야 하는 내용은 무엇인가
    해가 갈수록 어떻게 변해왔는가
    10년 전과 지금
    gephi를 사용하면 그래프를 입력으로 넣으면 분석해준다.
    시간의 흐름에 따라 최근 트렌드를 분석
    세상이 어떻게 바뀌는지 확인

    2006년 6월 - 2018년 8월

    EC 분야로 제한을 한다.
    Co-authorship network

    There are several interesting facts that can be computed on
    these co-authorship networks
    1. what kind of macroscopic values they yield
    2. which are the most outstanding actors and edges within this network

    Scientific-collaboration network in EC has been gathered from DBLP
    Defining a collection of terms
    - GECCO
    - PPSN
    - EuroGP
    - Evolutionary Computation
    - Genetic Programming ...

    total papers 6199
    total authors 5492
    mean papers per author(PA) 2.9
    mean authors per paper(AP) 2.56
    collaborators per author(CA) 4.2
    size of the giant component 3686
    as a percentage 67.1%
    2nd largest component 36
    clustering coefficient(CC) 0.808
    mean distance 6.1
    diameter(maximum distance) 18

    일단 dblp에서 논문의 수, 저자 수 등을 구하고 이 수치들을 구해야 한다.
    이후 논문에서 다른 DB의 데이터들과 비교 분석한 것이 있는데, 마찬가지로
    새롭게 구한 것들과 비교 분석한다.

    또 actors with the highest centrality in the giant component of the EC network
    이 과정에서 Betweeness, closeness, co-authors의 수를 구한다.

    이후에 proceedings를 제거하고 다시 구한다.

    끝

"""

import xml.etree.ElementTree as ET

tree = ET.parse("dblp.xml")
note = tree.getroot()

print(note.items())