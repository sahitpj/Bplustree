from bplustree import Bplustree
from utils import print_tree


tree = Bplustree(4)

# print(tree.root.keys)
# tree.insert(5)
tree.insert(7)
print("\n")

print_tree(tree.root, '   ', 0)

tree.insert(8)
print("\n")

print_tree(tree.root, '   ', 0)

tree.insert(9)
print("\n")

print_tree(tree.root, '   ', 0)

tree.insert(10)
print("\n")

print_tree(tree.root, '   ', 0)

tree.insert(13)
print("\n")

print_tree(tree.root, '   ', 0)

tree.insert(14)
# # tree.insert(10)
print("\n")

print_tree(tree.root, '   ', 0)


# # tree.insert(6)
# # tree.insert(4)
tree.insert(1)


print("\n")

print_tree(tree.root, '   ', 0)

tree.insert(2)

print("\n")

print_tree(tree.root, '   ', 0)


tree.insert(3)
tree.insert(5)
tree.insert(6)

print("\n")

print_tree(tree.root, '   ', 0)

tree.delete(14)

print("\n")

print_tree(tree.root, '   ', 0)

tree.delete(1)

print("\n")

# tree.delete(7)

print_tree(tree.root, '   ', 0)




tree.delete(7)

print("\n")

# tree.delete(7)

print_tree(tree.root, '   ', 0)


tree.delete(8)

print("\n")

# tree.delete(7)

print_tree(tree.root, '   ', 0)


tree.delete(3)
tree.delete(2)

print("\n")
print_tree(tree.root, '   ', 0)

tree.delete(5)

print("\n")

tree.delete(9)

print_tree(tree.root, '   ', 0)

# print(tree.root.keys)
print("done")