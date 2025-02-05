from functools import lru_cache

# @lru_cache(maxsize=10**10)
def recursion_solve(items, index, capacity):
    if index == len(items) or capacity == 0:
        return [], 0, capacity
    if capacity < 0:
        return [], -1, -1

    nt_items, nt_value, nt_cap = recursion_solve(items,
                        index + 1,
                        capacity)
    if items[index].weight > capacity:
        return nt_items, nt_value, nt_cap

    t_items, t_value, t_cap = recursion_solve(items,
                        index + 1,
                        capacity - items[index].weight)

    t_value += items[index].value

    if t_value > nt_value:
        return t_items + [index], t_value, t_cap

    return nt_items, nt_value, nt_cap

def dp_solve(items, index, capacity):


def check_taken(items, value, weight):
    i_cache = [[0] for i in range(weight)] * len(items)
    pass