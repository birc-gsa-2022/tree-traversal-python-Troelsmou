"""A module for breadth-first traversal of trees."""

from collections import deque
from typing import Iterable
from tree import T


def bf_order(t: T or None) -> Iterable[int]:
    if t == None:
        return []

    node_queue = deque([t])
    output_list = []

    while node_queue:
        if isinstance(node_queue[0], T):
            current_node = node_queue.popleft()
            output_list.append(current_node.val)
            node_queue.append(current_node.left)
            node_queue.append(current_node.right)
        else:
            node_queue.popleft()
    return output_list

tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))

print(bf_order(tree))
