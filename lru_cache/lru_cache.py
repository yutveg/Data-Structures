from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.length = 0
        self.dll = DoublyLinkedList()
        self.cache = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if(key not in self.cache):
            return None
        # move node accessed to front of DLL
        node_accessed = self.cache[key]
        self.dll.move_to_front(node_accessed)
        return node_accessed.value
       

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    #add to DLL, and to dict
    def set(self, key, value):
        # if key in cache delete node for that key then add new to head
        if(key in self.cache):
            self.dll.delete(self.cache[key])
            new_node = self.dll.add_to_head(value)
            self.cache[key] = new_node

        elif(self.length == self.limit):
            # delete least recently used entry if full from DLL and dict
            value_to_delete = self.dll.remove_from_tail() 
            key_to_delete = list(self.cache.keys())[list(self.cache.values()).index(value_to_delete)]
            del self.cache[key_to_delete]
            
            # add new node and dict key/value pair for new entry
            new_node = self.dll.add_to_head(value)
            self.cache[key] = new_node

        else:
            self.length += 1
            new_node = self.dll.add_to_head(value)
            self.cache[key] = new_node
