"""  
给一个文件和一个byte数组，判断这个byte数组是否在文件里出现过？本质是字符串匹配

考点：利用rolling hash将时间复杂度优化为O(N)
"""

from collections import deque

class RollingHash:
    def __init__(self, initailByte, a=31):
        self.a = a
        self.modulus = 2 ** 31
        self.initailByte = initailByte
        self.L = len(self.initailByte)
        self.aL = pow(self.a, self.L, self.modulus)
        self.curHash = None

    def hash(self):
        hashVal = 0
        for i in range(len(self.initailByte)):
            hashVal = (hashVal * self.a + self.initailByte[i]) % self.modulus

        self.curHash = hashVal
        return hashVal

    def rollingHash(self, removed, incoming):
        self.curHash = (self.curHash * self.a - removed * self.aL + incoming) % self.modulus
        return self.curHash

# def read_in_chunks(file_object, chunk_size=1024):
#     """Lazy function (generator) to read a file piece by piece.
#     Default chunk size: 1k."""
#     while True:
#         data = file_object.read(chunk_size)
#         if not data:
#             break
#         yield data

def containsBytesFileRollingHash(file_path, pattern):
    my_hash = RollingHash(pattern)
    pattern_hash = my_hash.hash()
    L = len(pattern)

    with open(file_path, 'rb') as f:
        initial_chunk = f.read(L)
        my_hash = RollingHash(initial_chunk)

        file_hash = my_hash()
        if file_hash == pattern_hash:
            return True

        f.seek(L, 0)
        window = deque(list(initial_chunk))
        for b in f.read(1):
            remove = window.popleft()
            window.append(b)
            file_hash = my_hash.rollingHash(remove, b)
            if file_hash == pattern_hash:
                return True

    return False



