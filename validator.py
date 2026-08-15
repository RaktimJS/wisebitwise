__import__('os').system('cls')




class TokenData():
    def __init__(self, token = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        '(', ')',
        '~', '^', '&', '|'
    ]):
        self.tokenChar = token

        if self.tokenChar in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            self.tokenType = "VARIABLE"
        elif self.tokenChar in ['^', '&', '|']:
            self.tokenType = "BINARY_OPERATOR"
        elif self.tokenChar == "~":
            self.tokenType = "UNARY_OPERATOR"
        elif self.tokenChar == "(":
            self.tokenType = "LPAREN"
        elif self.tokenChar == ")":
            self.tokenType = "RPAREN"

    def type(self):
        return self.tokenType

    def token(self):
        return self.tokenChar


# Tokeniser
def tokeniser(exp:str):
    cleanExp = exp.strip().upper().replace(" ", "")

    tokens = []
    validTokens = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        '(', ')',
        '~', '^', '&', '|'
    ]

    for i in cleanExp:
        if i not in validTokens:
            print(f"Invalid Token '{i}' at position {exp.index(i)}")
            return

        tokens.append(TokenData(i))

    return tokens
