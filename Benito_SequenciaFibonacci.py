n1 = int(input("Digite o valor de n1: "))
cont = 0

fibonacci = 1
fibonacci2 = 0
fibonacci3 = 0

while n1 >= cont:
    if n1 == fibonacci3:
        print(f"{n1} faz parte a sequência fibonacci!")
    fibonacci3 = fibonacci + fibonacci2
    fibonacci2 = fibonacci
    fibonacci = fibonacci3
