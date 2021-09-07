def main():
    #escribe tu código abajo de esta línea
    
    n=int(input("Dame un número: "))
    c=0
    while (n!=0):
        c=c+n
        n=int(input("Dame un número: "))
    print (c)    

if __name__=='__main__':
    main()
