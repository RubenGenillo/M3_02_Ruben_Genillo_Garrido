#Identifico el error en el siguiente código y lo evaluo con excepciones especificas para evitarlo
def main():
    try:
        lista = [4, 7, 30, 23, 5]
        lista[10]
    except IndexError:
        return "No existe un elemento en la lista en la posicion 10"

if __name__ == "__main__":
    print(main())