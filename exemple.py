# Les données intéressantes à observer sont initialisées à partir de la ligne 28 

# Pour l'import, assurez vous de l'avoir installé.
# (dans Tools -> Manage packages..., recherchez numpy et installez le)
import numpy as np

class Node:

    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, new_node):
        if self.head:
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next
                
            new_node.prev = last_node
            last_node.next = new_node
        
        else: self.head = new_node

# Variables builtin simples
a = 42
b = "Hello world"

lst = []
lst.append(a)
lst.append(b)

dic = {}
dic[a] = b
dic[b] = a
dic["lst"] = lst

t = (a, b)

s = {a, b, t}

# Variable d'import simples
na = np.array(lst)

# Objets créés simples
node1 = Node(a)
node2 = Node(b)
node3 = Node(lst)

# Variables builtin complexes
lst_complex = []
lst_complex.append(a)
lst_complex.append(node1)
lst_complex.append(node2)

dic_complex = {}
dic_complex[a] = node1
dic_complex[b] = node2
dic_complex["lst"] = node3

t_complex = (node1, node2)

s_complex = {node1, node2, node3}

# Variable d'import complexe
na = np.array([node1, node2, node3])

# Objet créé complexe
linked_list = LinkedList()
linked_list.insert(node1)
linked_list.insert(node2)
linked_list.insert(node3)
