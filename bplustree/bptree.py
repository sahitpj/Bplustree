from .node import Node, Leaf


class Bplustree(object):
    def __init__(self, degree):
        self.degree = degree
        self.root = Leaf(None, None, None, self.degree)

    def search(self, value, node):
        while node.t != 'leaf':
            flag = 0
            for i in range(len(node.keys)):
                if node.keys[i] >= value:
                    node = node.children[i]
                    flag = 1
                    break
            if flag == 0 and len(node.children) > len(node.keys):
                node = node.children[len(node.keys)] 
        print("searching for item {}".format(value), node.keys)
        try:
            index = node.keys.index(value)
            return index, node, 1
        except:
            return 0, node, 0


    def insert(self, value):
        d, leaf, r = self.search(value, self.root)
        if r == 1:
            print('{} is already present in the tree'.format(value))
        else:
            l = leaf.insert(value)
            print("{} has been successfully added to the tree".format(value))
            if l != 0:
                self.root = l

    def delete(self, value):
        d, leaf, r = self.search(value, self.root)
        if r == 1:
            l = leaf.remove(value)
            print("{} has been successfully deleted from the tree".format(value))
            if l != 0:
                self.root = l
        else:
            print('{} is not present in the tree'.format(value))