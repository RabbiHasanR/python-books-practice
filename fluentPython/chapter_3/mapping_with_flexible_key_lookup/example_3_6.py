class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            print(key)
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
    
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d)
print(d[2])
print(d[4])
print(d['1'])