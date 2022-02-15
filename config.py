# Modulo 10 Kata
# Elaborado por: Josue Santillan Garcia
# Ejercicio: Controlando excepciones.

# Primer version de control de excepciones
# def main():
#   try:
#       configuration = open('config.txt')
#   except FileNotFoundError:
#       print("Couldn't find the config.txt file!")

# Segunda version del control de excepciones
# def main():
#   try:
#       configuration = open('config.txt')
#   except Exception:
#       print("Couldn't find the config.txt file!")

# Tercer version del control de excepciones
# def main():
#   try:
#       configuration = open('config.txt')
#   except FileNotFoundError:
#       print("Couldn't find the config.txt file!")
#   except IsADirectoryError:
#       print("Found config.txt but it is a directory, couldn't read it")

# Version final del control de excepciones
# def main():
#   try:
#       configuration = open('config.txt')
#   except FileNotFoundError:
#       print("Couldn't find the config.txt file!")
#   except IsADirectoryError:
#       print("Found config.txt but it is a directory, couldn't read it")
#   except (BlockingIOError, TimeoutError):
#       print("Filesystem under heavy load, can't complete reading configuration file")

# Otra manera de controlar excepciones
def main():
    try:
        open("config.txt")
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt but couldn't read it")


if __name__ == '__main__':
    main()