class PrefixCodeTree:
    def __init__(self):
        self.left = None
        self.right = None
        self.symbol = None

    def insert(self, codeword, symbol):
        if self.symbol:
            raise Exception('Invalid prefix')
        if not codeword:
            self.symbol = symbol
        else:
            prefix = codeword[0]
            if str(prefix) == '0':
                if not self.left:
                    self.left = PrefixCodeTree()
                self.left.insert(codeword[1:], symbol)
            else:
                if not self.right:
                    self.right = PrefixCodeTree()
                self.right.insert(codeword[1:], symbol)

    def decode(self, encodedData, datalen):
        value = int.from_bytes(encodedData, 'big')
        print(value)
        binary = ''
        current = self
        res = ''
        for j in range(8 * len(encodedData)):
            binary = str(value >> j & 1) + binary
        for c in binary[:datalen]:
            if c == '0':
                current = current.left
            else:
                current = current.right
            if current.symbol:
                res += current.symbol
                current = self
        return res
