import collections

class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item


skd = StrKeyDict([('1', 'one'), ('2', 'two')])
print(skd)
print(skd[1])
skd[4] = 'four'
print(skd)
# print(skd[5])   # keyerror

print(skd.get(5))
print(skd.update({'4': 'Four'}))
print(skd)
