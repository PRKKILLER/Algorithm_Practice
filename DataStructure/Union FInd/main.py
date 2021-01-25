"""  
UnionFind / Disjoint Set data structure implementation.
"""


class UnionFind:
    def __init__(self, size: int):
        # number of elements in this union find
        self.size = size
        # used to track the size of each of the component
        # each group is originally of size one
        self._sz = [1 for _ in range(self.size)]
        # id[i] points to the parent of i, if id[i] == i, then i is a root node
        # link to itself (originally self root)
        self._id = [i for i in range(self.size)]
        # track the number of groups in the union find
        self._num_groups = self.size

    # Find which group/set 'p' belongs to, takes amortized const time
    def find(self, p: int) -> int:
        root = p
        while root != self._id[root]:
            root = self._id[root]

        # compress the path leading back to the root
        # doing this is called "path compression"
        # and is what gives us amortized constant time complexity
        while p != root:
            next = self._id[p]
            self._id[p] = root
            p = next

        return root

    # Return whether or not elem p and elem q are in the same group
    def is_connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    # Return the size of the group that elem p belongs to
    def groupSize(self, p: int) -> int:
        return self._sz[self.find(p)]

    # Unify the groups containing elem p and q
    def unify(self, p: int, q: int) -> None:
        if self.connected(p, q):
            return

        root1, root2 = self.find(p), self.find(q)

        if self._sz[root1] < self._sz[root2]:
            self._sz[root2] += self._sz[root1]
            self._id[root1] = self._id[root2]
        else:
            self._sz[root1] += self._sz[root2]
            self._id[root2] = self._id[root1]

        self._num_groups -= 1
