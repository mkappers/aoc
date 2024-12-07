import operator

class OperatorNode:
    ops = {"+": operator.add, "*": operator.mul}
    def __init__(self, value):
        self.value = value
        self.children = None

    def operator_children(self, operators, value):
        self.children = {}
        for op in operators:
            self.children[op] = OperatorNode(ops[op](self.value, value))
