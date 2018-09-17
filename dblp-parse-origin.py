# -*- coding: utf-8 -*-
from lxml import etree
import os, sys
from unidecode import unidecode


# @func: fast_iter
# @param context : iterparsed (chunk of xml) data
# @param func : handler
# @desc: Read xml chunk. After read, clear and delete chunk to release memory.
#		Also, replace html encoding to similar ascii code

def fast_iter(context, func, *args, **kwargs):
    collaborations = [u'phdthesis', u'inproceedings', u'incollection', u'proceedings',
                      u'mastersthesis', u'article']
    # xml categories
    author_array = []
    title = ''
    year = ''
    i = 0
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
            year = elem.text

        if elem.tag in collaborations:
            if len(author_array) is not 0 and title is not '':
                # rejected paper has no author or title
                # it should be check
                i = i + 1
                print(i)

                for a in author_array:
                    if journal == "ICGA":
                        f = open('ICGA','W')
                        f.write(a)
                        f.write(journal)
                        f.write(year)
                        f.write("---")
                        f.close()


                # write into kv file

                title = ''
                del author_array[:]

        elem.clear()
        while elem.getprevious() is not None:
            del elem.getparent()[0]
    del context
    # clear chunks


# @func: process_element
# @param elem : parsed data of chunk
# @param fout : file name to write
# @desc: It is handler to write content. just write content to file
def process_element(elem, fout):
    #print >> fout, elem
    pass

if __name__ == "__main__":
    fout = open('parsed_data.txt', 'w')
    context = etree.iterparse('dblp.xml', load_dtd=True, html=True)
    # To use iterparse, we don't need to read all of xml.
    fast_iter(context, process_element, fout)