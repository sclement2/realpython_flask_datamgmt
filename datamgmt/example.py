import sys
import locale
from treelib import Tree, Node

# Ensure the default encoding is set to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

def create_sample_tree():
    tree = Tree()
    tree.create_node("Root", "root")  # root node
    tree.create_node("Child 1", "child1", parent="root")
    tree.create_node("Child 2", "child2", parent="root")
    tree.create_node("Grandchild 1", "grandchild1", parent="child1")
    tree.create_node("Grandchild 2", "grandchild2", parent="child1")
    return tree

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
    print(locale.getpreferredencoding())
    tree = create_sample_tree()
    tree.show(line_type='ascii')
