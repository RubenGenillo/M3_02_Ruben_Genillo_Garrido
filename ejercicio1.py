#Identifico el error en el siguiente código y lo evaluo con excepciones especificas para evitarlo
def main():
    try: 
        numero = 7/0
    except ZeroDivisionError: 
        return "No se puede dividir entre cero"

if __name__ == "__main__":
    print(main())