a = [1, 2, 3, 4, 5, 6]

def find_indx_by_id(pk, items: list):
    i = 0

    for v in items:
        if id(v) == pk:
            return i
        i += 1

pk = id(a[2])
indx = find_indx_by_id(pk, a)

next_indx = indx + 1 if len(a) > indx + 1 else len(a) - 1
prev_indx = indx - 1 if indx - 1 > 0 else 0

# print(
#     'prev_indx', prev_indx,
#     'current', a[indx], 
#     'prev', a[prev_indx],
#     'next', a[next_indx],
# )
