class LinkNode(object):
    def __init__(self, key, value, pre = None, nxt = None):
        self.key = key
        self.value = value
        self.pre = None
        self.nxt = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = {}
        self.head = LinkNode(0,0)
        self.tail = LinkNode(0,0)
        self.head.nxt = self.tail
        self.tail.pre = self.head
        
    def add(self, node):
        p = self.tail.pre
        p.nxt = node
        node.nxt = self.tail
        node.pre = p
        self.tail.pre = node
    
    def remove(self, node):
        if node == self.tail or node == self.head:
            return
        p = node.pre
        n = node.nxt
        p.nxt = n
        n.pre = p
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic.keys():
            return -1
        targetNode = self.dic[key]
        val = targetNode.value
        self.remove(targetNode)
        self.add(targetNode)
        return val
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic.keys():
            removeNode = self.dic[key]
            self.remove(removeNode)
        node = LinkNode(key, value)
        self.dic[key] = node
        self.add(node)
        if len(self.dic) > self.capacity:
            earlyNode = self.head.nxt
            self.remove(earlyNode)
            del self.dic[earlyNode.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)