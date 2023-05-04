def addition(a,b):
        return a+b
def soustraction(a,b):
        return a-b
def multiplication(a,b):
        return a*b
def division(a,b):
        if b==0:
                return "Invalide !!"
        else:
                return a/b
def modulo(a,b):
        if b==0:
                return "Invalide !!"
        else:
                return a%b
def puissance(a,b):
        return a**b

if __name__=="__main__":
        print("c'est un module")
