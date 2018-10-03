# -*- coding: utf-8 -*-
# This code is referenced by songmw90's project
# [https://github.com/songmw90/dblp-parser/blob/master/dblp-parse.py]

from lxml import etree
import os, sys
from unidecode import unidecode
import pickle

# @func: fast_iter
# @param context : iterparsed (chunk of xml) data
# @param func : handler
# @desc: Read xml chunk. After read, clear and delete chunk to release memory.
#		Also, replace html encoding to similar ascii code
"""
    전체를 탐색해서 
    {저자 :({공저자 a, 공저자 b}, {논문1, 논문2}, 유전 알고리즘 관련 저자인가})
    {논문 : 저자 수, 유전 알고리즘 관련 논문인가} 를 연도별로 1980이전, 1980~1990, 1990~2000, 2000~2010, 2010~
    5개로 분류해서 10개의 딕셔너리를 만든다. 
    중간에 꺼질 수 있기 때문에, 지속적으로 딕셔너리를 저장하는 파일을 만든다. 
    
    한 번의 순회로 해당 딕셔너리를 만들면, 시기별로 전체 논문이 몇 개인지,
    전체 저자가 몇 명인지, 저자 당 평균 논문의 개수, 논문 당 평균 저자 수, 
    평균 공저자 수 등을 알 수있다.
    
    중간에 꺼질 수 있기 때문에 file offset을 저장하도록 하자
    
"""
def make_dict(Initial_actor_dict, Initial_paper_dict, author_array, title, isInitial):

    for a in author_array:
        if Initial_actor_dict.get(a):
            #diff = Initial_actor_dict[a][0] - {a}
            diff = set(author_array) - {a}

            Initial_actor_dict[a][0] = Initial_actor_dict[a][0] | diff
            Initial_actor_dict[a][1] = Initial_actor_dict[a][1] | {title}
            Initial_actor_dict[a][2] = Initial_actor_dict[a][2] or isInitial
        # dong이 chang과 is it worth 논문을 씀
        # dong이 hyun과 oh good 논문을 씀
        #
        else:
            Initial_actor_dict[a] = [set(author_array) - {a}, {title}, isInitial]

    Initial_paper_dict[title] = [len(author_array), isInitial]


def fast_iter(context, func, *args, **kwargs):
    # *args : 가변형 인자
    # **Kwargs : 키워드 인자, 사전형으로 값이 전달
    # 디폴트와 가변형, 키워드 인자를 복합적으로 가지고 있는 함수는
    # 다음과 같은 순서로 나열해야 한다. 일반 > 디폴트 > 키워드

    timing = 0

    Initial_actor_dict_10 = {}
    Initial_actor_dict_00 = {}
    Initial_actor_dict_90 = {}
    Initial_actor_dict_80 = {}
    Initial_actor_dict_70 = {}

    Initial_paper_dict_10 = {}
    Initial_paper_dict_00 = {}
    Initial_paper_dict_90 = {}
    Initial_paper_dict_80 = {}
    Initial_paper_dict_70 = {}

    Special = []
    with open("special.txt", "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.split('\n')[0]
            Special.append(line)

    collaborations = [u'phdthesis', u'inproceedings', u'incollection', u'proceedings',
                      u'mastersthesis', u'article', u'book']
    # u'www', u'book'는 제거
    # collaborations = [u'inproceedings', u'article']
    # xml categories
    author_array = []
    title = ''
    journal = ''
    year = ''
    isInitial = False
    start = 0
    # read chunk line by line
    # we focus author and title
    for event, elem in context:

        if elem.tag == 'author':
            author_array.append(unidecode(elem.text))

        if elem.tag == 'title':
            if elem.text:
                title = unidecode(elem.text)

        if elem.tag == 'journal' or elem.tag == 'booktitle':
            journal = elem.text

        if elem.tag == 'year':
            year = int(elem.text)

        if elem.tag in collaborations:
            timing = timing + 1
            if len(author_array) is not 0 and title is not '':
                # rejected paper has no author or title
                # it should be check

                if journal in Special:
                    isInitial = True
                    # 미리 정의한 학회, 저널에 속한 논문으로
                    # 해당 논문을 쓴 저자는 유전 알고리즘 관련 저자가 된다.

                if timing > start:
                    """
                    if year < 1980:
                        make_dict(Initial_actor_dict_70, Initial_paper_dict_70, author_array, title, isInitial)

                    elif year < 1990:
                        make_dict(Initial_actor_dict_80, Initial_paper_dict_80, author_array, title, isInitial)
                    """
                    if year < 2000:
                        make_dict(Initial_actor_dict_90, Initial_paper_dict_90, author_array, title, isInitial)
                    """
                    elif year < 2010:
                        make_dict(Initial_actor_dict_00, Initial_paper_dict_00, author_array, title, isInitial)

                    else:
                        make_dict(Initial_actor_dict_10, Initial_paper_dict_10, author_array, title, isInitial)
                    """
                    #for a in author_array:
                    #    func(a + "||" + title + "||" + journal + "||" + year, *args, **kwargs)

                title = ''
                journal = ''
                year = 0
                isInitial = False
                del author_array[:]

                if timing % 10000 == 0:
                    print(timing)

                if timing % 10000 == 0 and timing >= start:

                    
                    #with open('./actor/actor70.pickle', 'wb') as handle:
                    #    pickle.dump(Initial_actor_dict_70, handle)
                    #with open('./actor/actor80.pickle', 'wb') as handle:
                    #    pickle.dump(Initial_actor_dict_80, handle)
                    with open('./actor/actor90.pickle', 'wb') as handle:
                        pickle.dump(Initial_actor_dict_90, handle)
                    #with open('./actor/actor00.pickle', 'wb') as handle:
                    #    pickle.dump(Initial_actor_dict_00, handle)
                    #with open('./actor/actor10.pickle', 'wb') as handle:
                    #    pickle.dump(Initial_actor_dict_10, handle)


                    #with open('./paper/paper70.pickle','wb') as handle:
                    #    pickle.dump(Initial_paper_dict_70, handle)
                    #with open('./paper/paper80.pickle','wb') as handle:
                    #    pickle.dump(Initial_paper_dict_80, handle)
                    with open('./paper/paper90.pickle','wb') as handle:
                        pickle.dump(Initial_paper_dict_90, handle)
                    #with open('./paper/paper00.pickle','wb') as handle:
                    #    pickle.dump(Initial_paper_dict_00, handle)
                    #with open('./paper/paper10.pickle','wb') as handle:
                    #    pickle.dump(Initial_paper_dict_10, handle)

        elem.clear()
        while elem.getprevious() is not None:
            del elem.getparent()[0]

        # TODO
        # 딕셔너리를 저장

    del context
    # clear chunks




# @func: process_element
# @param elem : parsed data of chunk
# @param fout : file name to write
# @desc: It is handler to write content. just write content to file
def process_element(elem, fout):
    # print("writing ... " + elem)
    # print(elem, file=fout)
    pass

if __name__ == "__main__":
    fout = open('tmp.txt', 'w')
    context = etree.iterparse('dblp.xml', load_dtd=True, html=False)
    fast_iter(context, process_element, fout)
    fout.close()
