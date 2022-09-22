"""A module for breadth-first traversal of trees."""

from collections import deque
from typing import Iterable
from tree import T


def bf_order(t: T or None) -> Iterable[int]:
    if t == None:
        return []

    node_queue = [t]
    output_list = []

    while node_queue:
        if isinstance(node_queue[0], T):
            current_node = node_queue.pop(0)
            output_list.append(current_node.val)
            node_queue.append(current_node.left)
            node_queue.append(current_node.right)
        else:
            node_queue.pop(0)
    return output_list # FIXME

list(bf_order(None))