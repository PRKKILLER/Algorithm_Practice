"""  
Follow up questions:

1. Imagine you are given a real file system, how will you search files? DFS or BFS ?
In general, BFS will use more memory then DFS. 
However BFS can take advantage of the locality of files in inside directories, 
and therefore will probably be faster

2. If the file content is very large (GB level), how will you modify your solution?
In a real life solution we will not hash the entire file content, since it's not practical. 
Instead we will first do a sanity check: make use of meta data, like file size before really reading the big file. 
Files with different sizes are guaranteed to be different. 

For the files that have the same size, We will than hash a small part of the files with equal sizes 
(using MD5 for example, SHA256 is another more optimal way to hash file). 
Only if the md5 is the same, we will compare the files byte by byte

3. If you can only read the file by 1kb each time, how will you modify your solution?
This won't change the solution. We can create the hash from the 1kb chunks, 
and then read the entire file if a full byte by byte comparison is required.

4. What is the time complexity of your modified solution? 
   What is the most time consuming part and memory consuming part of it? How to optimize?
Time complexity is O(n^2 * k) since in worse case we might need to compare every file to all others. 
k is the file size

Comparing the file (by size, by hash and eventually byte by byte) is the most time consuming part.
Generating hash for every file will be the most memory consuming part.
如果是remote file system, 那么get_sub_dir()也会是bottleneck

How to make sure the duplicated files you find are not false positive?
We will use several filters to compare: File size, Hash and byte by byte comparisons.
We need to compare the content chunk by chunk when we find two "duplicates" using checkSum.
"""
import os
import hashlib
from collections import defaultdict


class FindDuplicateFiles:
    def __init__(self, path: str = None):
        self.root_path = path
        self.files_path = []
        self.dupFilesMap = defaultdict(list)

    def findDuplicates(self):
        if not self.root_path: return []

        # using dfs to find all files in the root_path
        self.getAllFiles()
        # get file -> size mapping
        fileSizeMap = self.getAllFilesBySize()

        for size in fileSizeMap:
            if len(fileSizeMap[size]) < 2:
                continue
            filesPaths = fileSizeMap[size]
            for f in filesPaths:
                hashCode = self.hashFile(f)
                self.dupFilesMap[hashCode].append(f)
        
        res = [self.dupFilesMap[val] for val in self.dupFilesMap if len(self.dupFilesMap[val]) > 1]

    def getAllFiles(self):
        stk = [self.root_path]
        while stk:
            cur_path = stk.pop()
            if os.path.isfile(cur_path):
                self.files_path.append(cur_path)
            elif os.path.isdir(cur_path):
                sub_paths = os.listdir(cur_path)
                for p in sub_paths:
                    stk.append(os.path.join(cur_path, p))

    def getAllFilesBySize(self):
        fileSizeMap = defaultdict(list)

        for f in self.files_path:
            file = open(f, 'rb')
            f_size = len(file) # get metadata
            fileSizeMap[f_size].append(f)

        return fileSizeMap


    # source: https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
    def hashFile(self, path):
        hash_sha256 = hashlib.sha256()
        with open(path, 'rb') as file:
            for chunk in iter(lambda: file.read(1024), b''):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest() # return the hex string

if __name__ == "__main__":
    duplicate_finder = FindDuplicateFiles('./Resources/Dropbox')
    dup_files = duplicate_finder.findDuplicates()
