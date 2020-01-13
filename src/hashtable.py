
# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def _hash_mod(self, key):
        return self._hash_djb2(key) % self.capacity


    def insert(self, key, value):
        hashIndex = self._hash_mod(key)
        current = self.storage[hashIndex]
        while current:
            if current.key == key:
                current.value = value
                return
            elif current.next: 
                current = current.next
            else: 
                current.next = LinkedPair(key, value)
                return

        self.storage[hashIndex] = LinkedPair(key,value)



    def remove(self, key):
        hashIndex = self._hash_mod(key)
        current = self.storage[hashIndex]
        if current.key == key:
            self.storage[hashIndex] = current.next
            return
        while current:
            prev = current
            current = current.next
            if current.key == key:
                prev.next = current.next
                return
        else: 
            print("Warning! Key not found")
            return None

    def retrieve(self, key):
        hashIndex = self._hash_mod(key)
        current = self.storage[hashIndex]
        if current:
            while current:
                if current.key == key:
                    return current.value
                else: 
                    current = current.next
        else: return None



    def resize(self):
        self.capacity = 2 * self.capacity
        prevStorage = self.storage
        self.storage =  [None] * self.capacity
        for i in prevStorage:
            while i:
                self.insert(i.key, i.value)
                i = i.next
        return


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
