def suma_N_numeros(N):
    s=0
    for i in range (1,N+1):
        s=s+i
    return s

def main():
    #escribe tu código abajo de esta línea
        
    N=int(input("Dame un número: "))
    suma=suma_N_numeros(N)
    print(suma)
    







if __name__=='__main__':
    main()
