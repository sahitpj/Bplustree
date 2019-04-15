
def print_tree(node, dl, count):
    print(dl*count ,node.keys)
    count += 1
    if node.t == 'node':
        for child in node.children:
            print_tree(child, dl, count)


