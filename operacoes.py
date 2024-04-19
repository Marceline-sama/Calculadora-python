class Operacoes:
    def soma(self, num1, num2):
        return num1 + num2
    
    def sub(self, num1, num2):
        return num1 - num2
        
    def multi(self, num1, num2):
        return num1 * num2
        
    def div(self, num1, num2):
        #if num1 < num2:
            #return 0
        if num2 == 0:
            return 0
        else:
            return num1 / num2
