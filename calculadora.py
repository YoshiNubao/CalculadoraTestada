class Calculadora():
    def __init__(self) -> None:
        self.ops = {}
        self.ops["*"] = lambda x,y: x*y 
        self.ops["/"] = lambda x,y: x/y if y!=0 else None
        self.ops["+"] = lambda x,y: x+y
        self.ops["-"] = lambda x,y: x-y
        self.ops["^"] = lambda x,y: x**y

    def calcular(self, n1:float, n2:float, op:str) -> float:
        if op not in self.ops.keys():
            return None

        return self.ops[op](n1,n2)