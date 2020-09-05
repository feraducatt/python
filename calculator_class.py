# a calculator class that takes an equation with +, -, ?, *, (, ) signs in the form of a space-separated string
# the class solves the equation in order of operations
class Calculator(object):

    def evaluate(self, string):
        self.eq = string.split()
        self.parse(self.eq)
        return float(self.eq[0])

    def parse(self, eq):
        multInd = len(eq)
        divInd = len(eq)
        addInd = len(eq)
        subInd = len(eq)

        if "(" in eq:
            parInd1 = eq.index("(")
            parInd2 = eq.index(")")
            answer = self.parse(eq[parInd1 + 1:parInd2])
            self.eq = eq[0:parInd1] + answer + eq[parInd2 + 1:len(eq)]
            self.parse(self.eq)
            return self.eq

        if "*" in eq:
            multInd = eq.index("*")
        if "/" in eq:
            divInd = eq.index("/")

        if multInd < divInd:
            answer = self.mult(multInd, eq)
            self.eq = eq[0:multInd - 1] + [answer] + eq[multInd + 2:len(eq)]
            self.parse(self.eq)
            return self.eq

        if multInd > divInd:
            answer = self.div(divInd, eq)
            self.eq = eq[0:divInd - 1] + [answer] + eq[divInd + 2:len(eq)]
            self.parse(self.eq)
            return self.eq

        if "+" in eq:
            addInd = eq.index("+")
        if "-" in eq:
            subInd = eq.index("-")

        if addInd < subInd:
            answer = self.add(addInd, eq)
            self.eq = eq[0:addInd - 1] + [answer] + eq[addInd + 2:len(eq)]
            self.parse(self.eq)
            return self.eq

        if addInd > subInd:
            answer = self.sub(subInd, eq)
            self.eq = eq[0:subInd - 1] + [answer] + eq[subInd + 2:len(eq)]
            self.parse(self.eq)
            return self.eq

    def add(self, int,eq):
        a, b = self.intIt(int,eq)
        return a + b

    def sub(self, int,eq):
        a, b = self.intIt(int, eq)
        return a - b

    def mult(self, int,eq):
        a, b = self.intIt(int, eq)
        return a * b

    def div(self, int,eq):
        a, b = self.intIt(int, eq)
        return a / b

    def intIt(self, index,eq):
        return float(eq[index - 1]), float(eq[index + 1])




#print(Calculator().evaluate("2 * ( 6 - 1 ) / ( 2 * 5 ) + 2"))
#print(2*( 6 - 1 ) / ( 2 * 5 )+2)
#print(Calculator().evaluate("2 * ( 5 - 1 ) / ( 2 * 5 ) + 2"))
#print(2*( 5 - 1 ) / ( 2 * 5 )+2)
