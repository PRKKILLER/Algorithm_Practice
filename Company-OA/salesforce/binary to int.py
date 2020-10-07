"""  
一串每个节点不是0就是1的二进制链表，要求把整条链表对应的二进制组合转换为一个十进制数
"""

def solution(head):
    if not head: return 0

    s = ''
    while head:
        s += head.val
        head = head.next

    return int(s, 2)

if __name__ == "__main__":
    print(int('110011',2))