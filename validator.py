__import__('os').system('cls')




class TokenData():
    def __init__(self, token):
        self.token = token
        self.nextTokenExpected = []

        if self.token in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            self.tokenType = "VARIABLE"
            self.nextTokenExpected = ["BINARY_OPERATOR", "RPAREN", "END"]
        elif self.token in ['^', '&', '|']:
            self.tokenType = "BINARY_OPERATOR"
            self.nextTokenExpected = ["VARIABLE", "LPAREN", "UNARY_OPERATOR"]
        elif self.token == "~":
            self.tokenType = "UNARY_OPERATOR"
            self.nextTokenExpected = ["VARIABLE", "UNARY_OPERATOR", "LPAREN"]
        elif self.token == "(":
            self.tokenType = "LPAREN"
            self.nextTokenExpected = ["VARIABLE", "LPAREN", "UNARY_OPERATOR"]
        elif self.token == ")":
            self.tokenType = "RPAREN"
            self.nextTokenExpected = ["BINARY_OPERATOR", "RPAREN", "END"]
        elif self.token == "<":
            self.tokenType = "START"
            self.nextTokenExpected = ["VARIABLE", "LPAREN", "UNARY_OPERATOR"]
        elif self.token == ">":
            self.tokenType = "END"
            self.nextTokenExpected = [None]

    def type(self):
        return self.tokenType

    def tokenChar(self):
        return self.token

    def expected(self):
        return self.nextTokenExpected


# Tokeniser
def tokeniser(exp:str):
    cleanExp = ("<" + exp +  ">").strip().upper().replace(" ", "")

    global tokens
    tokens = []
    validTokens = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        '(', ')',
        '~',
        '^', '&', '|',
        "<", ">"
    ]

    for i in cleanExp:
        if i not in validTokens:
            print(f"Invalid Token '{i}' at position {exp.index(i)}")
            return

        tokens.append(TokenData(i))

    return tokens


# Syntax validator
def synataxValidator(exp:str):
    data = tokeniser(exp)
    size = len(tokens) - 1
    expectation = ["VARIABLE", "LPAREN", "UNARY_OPERATOR"]
    i = 1
    depth = 0

    while i <= size:
        if tokens[i].type() == "END":
            break
        else:
            if tokens[i].type() in expectation:
                expectation = tokens[i].expected()
            else:
                print(f"Unexpected token : '{tokens[i].tokenChar()}' at position {i}")
                return

            if tokens[i].type() == "LPAREN":
                depth += 1
            elif tokens[i].type() == "RPAREN":
                depth -= 1

        i += 1

    if depth > 0:
        print("Unclosed parantheses found")
    elif depth < 0:
        print("Closed an unopened parantheses")
