"""A module for depth-first (in-order) traversal of trees."""

from typing import Iterable
from tree import T

def in_order(t: T or None) -> Iterable[int]:
    if t == None:
        return []
    output_list = list()
    stack = list()
    current_node = t
    while True:
        if current_node != None:
            stack.append(current_node)
            current_node = current_node.left
        elif stack:
            popped = stack.pop()
            output_list.append(popped.val)
            current_node = popped.right
        else:
            break

    return output_list



tree = T(2, T(1, None, None), 
    T(4, T(3, None, None), T(5, None, None)))

print(in_order(tree))
