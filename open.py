# Modulo 10 Kata
# Elaborado por: Josue Santillan Garcia
# Ejercicio: Tracebacks

# def main():
#   open("/path/to/mars.jpg")

# Actualizamos la funcion main
def main():
    try:
        open("mars.jpg")
    except FileNotFoundError as err:
        print("got a problem trying to read the file:", err)

if __name__ == '__main__':
    main()