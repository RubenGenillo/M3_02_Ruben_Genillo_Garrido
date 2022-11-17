#Identifico el error en el siguiente código y lo evaluo con excepciones especificas para evitarlo
def main():
    try:        
        resultado = "2" + 10
    except TypeError:
        return "No puedes sumar un integer a un string"

if __name__ == "__main__":
    print(main())