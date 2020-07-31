// 61. 旋转链表
// 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

// Definition for singly-linked list.
function ListNode(val) {
    this.val = val;
    this.next = null;
}

/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
  if (!head) { return head; }

  let len = 0, tail = undefined;
  let tmp = head;
  while (true) {
    len += 1;
    if (tmp.next) { tmp = tmp.next; }
    else {
      tail = tmp;
      break;
    }
  }
  k = k % len;
  if (k === 0) { return head; }

  let mid = undefined;
  pre = head;
  tmp = head.next;
  for (let i = 1; i < len - k; i++) {
    pre = tmp;
    tmp = tmp.next;
  }
  mid = tmp;

  pre.next = tail.next;
  tail.next = head;

  return mid;
};