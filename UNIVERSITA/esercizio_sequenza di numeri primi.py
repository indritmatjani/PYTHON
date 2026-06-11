print("SEQUENZA DI NUMERI PRIMI")

def primo(n):
    div=2
    while div<n:
        if n%div==0:
            return False
        div+=1
    return True

def main():
    print("SEQUENZA NUMERI PRIMI")

    num=0
    while num<=3:
        num=int(input("fino a che numero vuoi elencare i numeri primi? "))

    print("elenco numeri primi da 1 a ",num)
    print("1, 2",end=", ")
    for i in range (3,num+1,2):
            if primo(i):
                print(i,end=", ")

main()
