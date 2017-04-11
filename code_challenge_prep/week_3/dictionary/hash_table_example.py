class MyHashTable:
    def __init__(self):
        # Nothing
        pass


    def myhash(self, value):
        # Assume value is a string
        # Return hashed value.
        return (ord(value[0].lower())-97)

    def securityHash(self, value):
        return value[0:3]

    def fullnameHash(self, value):
        multiply = self.myhash(value[0])
        for x in range(1, len(value)):
            if value[x]== ' ':
                multiply *= self.myhash(value[x+1])
        return multiply

test = MyHashTable()
print(test.myhash('jpple'))
print(test.myhash('epple'))
print(test.myhash('uack'))
print(test.securityHash('123'))
print(test.fullnameHash('Tamby Kojak bac'))
