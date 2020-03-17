# 【简单】1407. 面试题 03.02. 栈的最小值
# 请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(1)。


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x: int) -> None:
        if not len(self.stack): self.stack.append([x, x])
        else:
            if x <= self.stack[-1][1]: self.stack.append([x, x])
            else: self.stack.append([x, self.stack[-1][1]])

    def pop(self) -> None:
        return self.stack.pop(-1)[0] if len(self.stack) else None

    def top(self) -> int:
        return self.stack[-1][0] if len(self.stack) else None

    def getMin(self) -> int:
        return self.stack[-1][1] if len(self.stack) else None



if __name__ == '__main__':
    obj = MinStack()
    obj.push(4)
    print(obj.top())
    print(obj.getMin())
    obj.pop()
