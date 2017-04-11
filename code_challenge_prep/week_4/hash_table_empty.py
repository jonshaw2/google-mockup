class MyHashTable:
    def __init__(self):
        self.buckets = [None] * 26

    def my_hash(self, value):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        first_letter = value[0]
        return alphabet.index(first_letter.lower())

    def insert(self, value):
        # Inserts value into the correct bucket.
        index = self.my_hash(value)
        if self.buckets[index] == None:
            self.buckets[index]=[]

        self.buckets[index].append(value)

    def exists(self, value):
        # Returns true if the value exists in the bucket.
        index = self.my_hash(value)
        # for i in range(len(self.buckets[index])):
        #     if self.buckets == value:
        #         return True
        if self.buckets[index] == None:
            self.buckets[index]=[]

        elif value in self.buckets[index]:
            return True
        return False

hash_table = MyHashTable()
hash_table.insert('Hello World')
hash_table.insert('Bob')
hash_table.insert('Bib')
hash_table.insert('Cathy')
hash_table.insert('Zebra')

print(hash_table.exists('Hello World'))

print(hash_table.buckets)
