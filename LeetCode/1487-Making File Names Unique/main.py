"""  
Given an array of strings names of size n. You will create n folders in your file system such that, 
at the ith minute, you will create a folder with the name names[i].

Since two files cannot have the same name, if you enter a folder name which is previously used, 
the system will have a suffix addition to its name in the form of (k), where, k is the smallest positive integer 
such that the obtained name remains unique.

Return an array of strings of length n where ans[i] is the actual name the system will assign to the ith folder 
when you create it.

Example 4:

Input: names = ["wano","wano","wano","wano"]
Output: ["wano","wano(1)","wano(2)","wano(3)"]
Explanation: Just increase the value of k each time you create folder "wano".
Example 5:

Input: names = ["kaido","kaido(1)","kaido","kaido(1)"]
Output: ["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
Explanation: Please note that system adds the suffix (k) to current name even it contained the same suffix before.
"""


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        lookup, res = {}, []

        for name in names:
            if name in lookup:
                val = lookup[name]
                name_new = f'{name}({val})'

                while name_new in lookup:
                    val += 1
                    name_new = f'{name}({val})'

                res.append(name_new)
                lookup[name_new] = 1
                lookup[name] = val + 1

            else:
                res.append(name)
                lookup[name] = 1

        return res
