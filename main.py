from calculadora import Calculadora
import sys

def main():

    try:
        n1:float= float(sys.argv[1])
        n2:float = float(sys.argv[2])
        op:str = sys.argv[3]
        
        calculadora: Calculadora = Calculadora()
        print(calculadora.calcular(n1,n2,op))
    except Exception:
        print("None")

if __name__ == "__main__":
    main()