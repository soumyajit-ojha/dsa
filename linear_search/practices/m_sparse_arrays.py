# There is a collection of input strings and a collection of query strings.
# For each query string, determine how many times it occurs in the list of input strings.
# Return an array of the results.

# Example:
#   string_list = ["ab", "ab", "abc"]
#   queries = ["ab", "abc", "bc"]
#   output = [2, 1, 0]

def query_count(str_list: list[str], queries = list[str]) -> list[int]:
    map = {}
    print("before", map)
    for st in str_list:
        map[st] = map.get(st, 0) + 1
    print("after map", map)

    return [map.get(s, 0) for s in queries]

str_l = ["ab", "ab", "abc"]
q = ["ab", "abc", "bc"]
res = query_count(str_list=str_l, queries=q)
print(res)
