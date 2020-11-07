class SingleLinkedListNode(object):
    """A model of single linked list node and inheriting object parent class"""

    def __init__(self, value, nxt):
        """Initializing attibutes for single linked list node"""
        self.value = value
        self.next = nxt
    
    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"