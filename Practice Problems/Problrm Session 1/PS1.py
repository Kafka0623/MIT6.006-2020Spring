def reorder_students(L):
    """
    输入: L | 链表, 有 L.head (头结点) 和 L.size (长度)
    输出: None | 原地修改链表，使后半部分反转
    """
    if L.size <= 1:
        return

    # 1. 找到中点 (slow 停在前半部分最后一个节点)
    slow = L.head
    fast = L.head
    while fast and fast.next:
        fast = fast.next.next
        if fast and fast.next:   # 让 slow 停在 n/2 节点
            slow = slow.next

    # 2. 反转后半段链表 (从 slow.next 开始)
    prev = None
    curr = slow.next
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # 3. 接回前半部分和反转后的后半部分
    slow.next = prev
