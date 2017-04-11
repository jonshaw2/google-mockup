class MyDictionary:
    def __init__(self):
        self.key = []
        self.values = []

    def insert_element(self,key, values):
        # Insert the element into the dictionary.
        self.key.append(key)
        self.values.append(values)

    def find_element(self,key):
        # Finds the element assciated with the key.
        # Returns None if key doesn't exist.
        for i in range(len(self.key)):
            if (self.key[i]) == key:
                return self.values[i]
        return None

    def remove_element(self,key):
        # Finds element associated with key
        # Removes element if element is found.
        for i in range(len(self.key)):
            if (self.key[i]) == key:
                del self.key[i]
                del self.values[i]
                break

    def get_keys(self):
        return self.key

    def elements(self):
        return self.values

    def isEmpty(self):
        # Returns if the element list is empty.
        return self.size() == 0

    def size(self):
        # Returns the size of the elements list.
        return len(self.values)


dictionary = MyDictionary()
dictionary.insert_element('email', 'tamby@hirewire.com')
dictionary.insert_element('password','chicken_nugget$')
dictionary.insert_element('phone', '9737574181')

child_dictionary = MyDictionary()
child_dictionary.insert_element('another_value','test')

dictionary.insert_element('child', child_dictionary)

for key in dictionary.get_keys():
    print(dictionary.find_element(key))

dictionary.remove_element('phone')

print("==========\n\n")

for key in dictionary.get_keys():
    print(dictionary.find_element(key))

if dictionary.find_element('email') == 'tamby@hirewire.com':
    print('yay')
