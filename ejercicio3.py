#Identifico el error en el siguiente código y lo evaluo con excepciones especificas para evitarlo
def main():    
    try:
        paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
        paises["alemania"]
    except KeyError:
        return 'No existe la clave introducida'

if __name__ == "__main__":
    print(main())
