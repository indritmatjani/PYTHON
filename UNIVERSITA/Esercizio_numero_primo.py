print("NUMERO PRIMO")

def primo(n):
    div=2
    while div<n:
        if n%div==0:
            return False
        div+=1
    return True

def main():
    print("NUMERO PRIMO")

num=0
while num<=1:
    num=int(input("inserire un numero: "))

    if primo(num):
        print(num,"è un numero primo")
    else:
        print(num,"non è un numero primo")
