from calculator.controller import CalculatorController
#컨트롤러를 인스턴스화 한다
if __name__ == '__main__':

    num1 = int(input('1st number?'))
    op = input('연산자?')
    num2 = int(input('2nd number?'))
    calc = CalculatorController(num1,num2)
    print(calc.exec(op))