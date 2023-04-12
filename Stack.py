class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for t in tokenList:
        if str(t) not in "()*/+-":
            postfixList.append(t)
        elif t == "(":
            opStack.push("(")
        elif t == ")":
            top = opStack.pop()
            while top != "(":
                postfixList.append(top)
                top = opStack.pop()
        else:
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[t]:
                postfixList.append(opStack.pop())
            opStack.push(t)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    opStack = ArrayStack()
    result = 0
    for t in tokenList:
        if str(t) not in "()*/+-":
            opStack.push(int(t))
        else:
            Y = opStack.pop()
            X = opStack.pop()
            if t == "+":
                result = X + Y
            elif t == "-":
                result = X - Y
            elif t == "*":
                result = X * Y
            else:
                result = X / Y
            opStack.push(result)

    return opStack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val