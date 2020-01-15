import os
import xml.etree.ElementTree as etree


# Toate documentele care conțin elementul(tag-ul) “document”
def a(collection_path, tag_name):
    answer = []
    found = False
    for file_name in os.listdir(collection_path):
        root = etree.parse(collection_path + "/" + file_name).getroot()
        element = root.find(".//" + tag_name)
        if element is None:
            continue
        answer.append(file_name)
    return answer


# Toate documentele care conțin cuvântul “proiect” sub elementul “word”.
def b(collection_path, tag_name, tag_content):
    answer = []
    found = False
    for file_name in os.listdir(collection_path):
        root = etree.parse(collection_path + "/" + file_name).getroot()
        for element in root.findall(".//" + tag_name):
            if element.text == tag_content:
                answer.append(file_name)
                continue
    return answer


# Toate documentele care conțin un anumit număr de elemente.
def c(collection_path, elem_count):
    answer = []
    found = False
    for file_name in os.listdir(collection_path):
        root = etree.parse(collection_path + "/" + file_name).getroot()
        if len(root.findall(".//")) >= elem_count:
            answer.append(file_name)
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
    found = False
    for file_name in os.listdir(collection_path):
        root = etree.parse(collection_path + "/" + file_name).getroot()
        if node_ident(root, depth):
            answer.append(file_name)
            found = True
    return answer
#
# a('xmlCollection', "document")
# b('xmlCollection', "word", "proiect")
# c('xmlCollection', 1000)
# d('xmlCollection', 5)
