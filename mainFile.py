import os
import xml.etree.ElementTree as etree
from collections import defaultdict

a_store = defaultdict(list)
b_store = defaultdict(list)
c_store = defaultdict(list)
d_store = defaultdict(list)


# Toate documentele care conțin elementul(tag-ul) “document”
def a(collection_path, tag_name):
    answer = []
    if len(a_store[tag_name]):
        return a_store[tag_name]

    for file_name in os.listdir(collection_path):
        root = etree.parse(collection_path + "/" + file_name).getroot()
        element = root.find(".//" + tag_name)
        if element is None:
            continue
        answer.append(file_name)
        a_store[tag_name].append(file_name)

        # add file to global store, so the next search will take data from store
    a_store[tag_name].append("rwturnwd from a_store")
    return answer


# Toate documentele care conțin cuvântul “proiect” sub elementul “word”.
def b(collection_path, tag_name, tag_content):
    answer = []
    frecvency = {}

    if len(b_store[tag_name + "_" + tag_content]):
        return b_store[tag_name + "_" + tag_content]

    for file_name in os.listdir(collection_path):
        root = etree.parse(collection_path + "/" + file_name).getroot()
        for element in root.findall(".//" + tag_name):
            if element.text.find(tag_content):
                if file_name in frecvency:
                    continue
                answer.append(file_name)
                frecvency[file_name] = True
                b_store[tag_name + "_" + tag_content].append(file_name)
                continue
    b_store[tag_name + "_" + tag_content].append("this data is from store")
    return answer


# Toate documentele care conțin un anumit număr de elemente.
def c(collection_path, elem_count):
    answer = []

    if len(c_store[elem_count]):
        return c_store[elem_count]
    for file_name in os.listdir(collection_path):
        root = etree.parse(collection_path + "/" + file_name).getroot()
        if len(root.findall(".//")) >= elem_count:
            answer.append(file_name)
            c_store[elem_count].append(file_name)
    c_store[elem_count].append("this data is from store")
    return answer


def node_ident(node, ident):
    id_necessary_depth = False
    if ident == 0:
        return True
    if len(node):
        for child in node:
            id_necessary_depth = node_ident(child, ident - 1)
            if id_necessary_depth:
                break
    return id_necessary_depth


# Toate documentele care au o adâncime a arborelui XML mai mare de 5.
def d(collection_path, depth):
    answer = []

    if len(d_store[depth]):
        return d_store[depth]

    for file_name in os.listdir(collection_path):
        root = etree.parse(collection_path + "/" + file_name).getroot()
        if node_ident(root, depth):
            answer.append(file_name)
            d_store[depth].append(file_name)
    d_store[depth].append("this data is from store")
    return answer
#
# a('xmlCollection', "document")
# b('xmlCollection', "word", "proiect")
# c('xmlCollection', 1000)
# d('xmlCollection', 5)
