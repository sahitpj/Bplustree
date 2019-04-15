import math


class Node(object):
    def __init__(self, parent, degree):
        self.parent = parent
        self.degree = degree
        self.previous_node = None
        self.next_node = None
        self.keys = list()
        self.children = list()
        self.t = 'node'

    def property(self):
        return len(self.children) >= int(math.ceil(self.degree/2))

    def creation_insert(self, key, child1, child2):
        self.keys.append(key)
        self.children.append(child1)
        self.children.append(child2)


    def update_keys(self):
        if self.children[0].t == 'leaf':
            if self.property():
                l = list()
                for child in self.children:
                    l.append(child.keys[-1])
                self.keys = l[: len(self.children)-1]
            else:
                self.bring_down_adjust()

    def insert(self, key, child):
        flag = 0
        for i in range(len(self.keys)):
            if self.keys[i] > key:
                self.keys = self.keys[:i] + [key] + self.keys[i:]  
                if self.children[i].keys[-1] > child.keys[0]:
                    self.children = self.children[:i] + [child] + self.children[i:]
                else:
                    self.children = self.children[:i+1] + [child] + self.children[i+1:]
                
                flag = 1
                break
        if flag == 0:
            self.keys.append(key)
            self.children.append(child)
        if len(self.keys) >= self.degree:
            root = self.balance()
        else:
            root = 0
        if child.t == 'leaf':
            self.update_keys()
        return root




    def balance(self):
        index = (self.degree+1)//2
        r = self.keys[index-1]
        new_node = Node(self.parent, self.degree)
        new_node.keys = self.keys[index:]
        self.keys = self.keys[:index-1]
        new_node.children = self.children[index: ]
        for child in new_node.children:
            child.parent = new_node
        self.children = self.children[:index]
        if self.parent == None:
            node_p = Node(None, self.degree)
            node_p.creation_insert(r, self, new_node)
            self.parent = node_p
            new_node.parent = node_p
            return node_p
        else:
            root = self.parent.insert(r, new_node)
            return root
        

    def remove_adjust(self):
        if self.children[0].t == 'leaf':
            self.update_keys()
            if self.parent == None:
                return self.children[0].parent
        if self.parent.parent == None:
            return self.parent
        else:
            return self.parent.remove_adjust()


    def bring_down_adjust(self):
        flag = 0
        if self.parent == None:
            self.keys = self.children[0].keys
            self.children = []
        elif len(self.parent.keys) == 1:
            if self.parent.children.index(self) == 0:
                left_node = self.parent.children[1]
                self.keys.extend(self.parent.keys)
                self.merge(left_node, 1)
            else:
                left_node = self.parent.children[0]
                left_node.keys.extend(self.parent.keys)
                self.merge(left_node, -1)
            for child in self.children:
                child.parent = self
            self.update_keys()
            self.parent = None
        else:
            ind = self.parent.children.index(self) 
            if ind < len(self.parent.children) - 1:
                right_node = self.parent.children[ind+1]
                self.keys.extend(self.parent.keys[ind])
                self.merge(right_node, 1)
            # print(left_node.keys, "ln keys")
            else:
                left_node = self.parent.children[ind-1]
                left_node.extend(self.parent.keys[ind])
                self.merge(left_node, -1)
            for child in self.children:
                child.parent = self
            self.parent.bring_down_adjust()


    def merge(self, node, order):
        if order == 1:
            self.keys = self.keys + node.keys
            self.children[0].next_leaf = node.children[0]
            node.children[0].previous_leaf = self.children[0]
            self.children = self.children + node.children
        else:
            self.keys =  node.keys + self.keys 
            node.children[0].next_leaf = self.children[0]
            self.children[0].previous_leaf = node.children[0]
            self.children =  node.children + self.children


class Leaf(Node):
    def __init__(self, previous_leaf, next_leaf, parent, degree):
        self.parent = parent
        self.degree = degree
        self.previous_leaf = previous_leaf
        self.next_leaf = next_leaf
        self.parent = parent
        self.degree = degree
        self.keys = list()
        self.t = 'leaf'
        
    def size(self):
        return len(self.keys)

    def property(self):
        return len(self.keys) >= self.degree//2


    def get(self, key):
        try:
            index = self.keys.index(key)
            return index, key
        except:
            return -1, key

    def insert(self, key):
        flag = 0
        for i in range(len(self.keys)):
            if self.keys[i] > key:
                self.keys = self.keys[:i] + [key] + self.keys[i:]
                flag = 1
                break
        if flag == 0:
            self.keys.append(key)
        if len(self.keys) >= self.degree:
            # print(self.keys, "keys\n")
            root = self.balance()
            return root 
        else:
            return 0

    def balance(self):
        index = (self.degree+1)//2
        r = self.keys[index-1]
        print(self.next_leaf)
        if self.next_leaf == None or len(self.next_leaf.keys) + len(self.keys)-index > self.degree-1:
            new_leaf = Leaf(self, None, self.parent, self.degree)
            try:
                self.next_leaf.previous_leaf = new_leaf
            except:
                None
            new_leaf.next_leaf = self.next_leaf
            self.next_leaf = new_leaf
            new_leaf.keys = self.keys[index:]
            self.keys = self.keys[:index]
            if self.parent == None:
                node_p = Node(None, self.degree)
                node_p.creation_insert(r, self, new_leaf)
                self.parent = node_p
                new_leaf.parent = node_p
                return node_p
            else:
                root = self.parent.insert(r, new_leaf)
                return root
        else:
            next_leaf = self.next_leaf
            for key in self.keys[index:]:
                for i in range(len(next_leaf.keys)):
                    if next_leaf.keys[i] > key:
                        next_leaf.keys = next_leaf.keys[:i] + [key] + next_leaf.keys[i:]
                        flag = 1
                        break
                if flag == 0:
                    next_leaf.keys.append(key)
            self.keys = self.keys[:index]
            n = self.parent
            n.update_keys()
            while( n.parent != None):
                n = n.parent
            return n


    def merge(self, leaf, order):
        if order == 1:
            self.keys = self.keys + leaf.keys
        else:
            self.keys = leaf.keys + self.keys


    def remove(self, value):
        self.keys.remove(value)
        p = self.parent
        if self.property() == False:
            if self.next_leaf != None:
                if self.next_leaf.parent == p:
                    if len(self.keys) + len(self.next_leaf.keys) <= self.degree-1:
                        self.merge(self.next_leaf, 1)
                        p.children.remove(self.next_leaf)
                        self.next_leaf = self.next_leaf.next_leaf
                    elif (len(self.keys) + len(self.next_leaf.keys))//2 >= self.degree//2:
                        count = 0
                        while len(self.keys) < self.degree//2:
                            self.keys.append(self.next_leaf.keys[count])
                            count += 1
                        self.next_leaf.keys = self.next_leaf.keys[count:]
            elif self.previous_leaf != None:
                if self.previous_leaf.parent == p:
                    if len(self.keys) + len(self.previous_leaf.keys) <= self.degree-1:
                        self.merge(self.previous_leaf, -1)
                        p.children.remove(self.previous_leaf)
                        self.previous_leaf = self.previous_leaf.previous_leaf
                        self.previous_leaf.next_leaf = self
                    elif (len(self.keys) + len(self.previous_leaf.keys))//2 >= self.degree//2:
                        print(self.previous_leaf.keys)
                        count = -1
                        while len(self.keys) < self.degree//2:
                            self.keys = [self.previous_leaf.keys[count]] + self.keys
                            count -= 1
                        self.previous_leaf.keys = self.previous_leaf.keys[:count+1]
                        print(self.previous_leaf.keys)
        if p.parent == None:
            p.update_keys()
            return p 
        else:
            return p.remove_adjust()


                

