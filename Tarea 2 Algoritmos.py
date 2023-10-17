def es_numero(Expresion_Junta, i):
    
    #Esta función recibe un string con todo el contenido a la derecha del "=" y un índice i, 
    #Junta el numero y lo retorna como entero.
    #También actualiza el indice i, que es el encargado de recorrer la Expresión.

    #Creamos la lista y unimos los elementos que coinciden
   Numero = []
   while i < len(Expresion_Junta) and Expresion_Junta[i].isdigit():
      Numero.append(Expresion_Junta[i])
      i += 1

    #Unimos la lista y lo convertimos en int.
   Numero_Junto = ""
   for k in Numero:
      Numero_Junto += k
   
   return int(Numero_Junto), i


def es_Letra(Expresion_Junta, i):
   # Devuelve un string de caracteres, el cual corta cuando detecta un espacio o un signo de operación, junto con el indice i actualizado
   # Recibe la misma expresión que la función anterior, pero esta lee mas que números y funciona para reconocer las variables.

   # Creamos la lista y unimos los elementos que coinciden.
   Letra = []
   while i < len(Expresion_Junta) and Expresion_Junta[i] != " " and Expresion_Junta[i] != "+" and Expresion_Junta[i] != "-" and Expresion_Junta[i] != "*" and Expresion_Junta[i] != "/" and Expresion_Junta[i] != "^" :
      Letra.append(Expresion_Junta[i])
      i += 1

   # Unimos la lista y retornamos el string.
   Letras_Juntas = ""
   for k in Letra:
      Letras_Juntas += k
   
   return Letras_Juntas, i


def procesar_comando(comando, dicc_var):
    # Esta función recibe un comando en string y el diccionario de variables. Con él, 
    # procesa el comando, imprime el resultado de la expresión
    # y posiblemente modifica el diccionario. La función retorna el diccionario
    # La función procesa el comando e imprime el resultado


    # Creamos las listas vacías de variable y expresión
    variable = []
    Expresion = []

    # Estas 2 partes separan el comando en el "="  
    # y guardan cada parte termino a termino en una lista
    # la parte de la izquierda se almacena en variable
    # la parte derecha se almacena en Expresion
    for i in range(0,len(comando)):
        if comando[i] == "=":
            break
        elif comando[i] == " ":
           None
        else:
            variable.append(comando[i])

    j = len(comando) - 1
    if j == -1:
       return None
    else:
        while comando[j] != "=" and j >= 0:
            if comando[j] == " ":
               j = j - 1
            else:
                Expresion.insert(0,comando[j])
                j = j - 1

    Variable_Junta = ""
    Expresion_Junta = ""

    # En esta parte se juntan los elementos de la lista
    for i in variable:
       Variable_Junta += i
    
    for i in Expresion:
       Expresion_Junta += i

    # Se inicia el contador del resultado de la calculadora
    # Se inician los contadores para los ciclos while  
    # Se define el operador "+" como el inicial. 

    Resultado = 0
    i = 0
    j = 0
    operador = "+"

    # Ciclo while que lleva la calculadora, 
    # maneja los errores de sintaxis 
    # y actualiza los valores del resultado y el diccionario
    while i < len(Expresion_Junta):
        # Este ciclo while se encarga de revisar la variable, la cual recorre con el indice j
        # En caso de existir un error rompe el ciclo y retorna el error correspondiente.
        while j <len(Variable_Junta):
           # Revisa que no inicie por un número.
           if Variable_Junta[0].isdigit():
              Resultado = ("Error: Variable inválida, las variables no pueden comenzar por un numero: " + Variable_Junta[j:])
              break
           # Revisa que no inicie con un guion bajo.
           elif Variable_Junta[0] == "_":
                Resultado = ("Error: Variable inválida, las variables no pueden comenzar por un guion bajo: "+ Variable_Junta[j:])
                break 
           # Las próximas 3 hacen avanzar el indice, ya que son caracteres permitidos.
           elif Variable_Junta[j].isalpha():
              j += 1
           elif Variable_Junta[j].isdigit():
              j += 1
           elif Variable_Junta[j] == "_":
              j += 1
           # Si encuentra cualquier otro carácter no permitido.
           else: 
              Resultado = ("Error: Sintaxis incorrecta "+ Variable_Junta[j:]+" Por favor revise su entrada.")
              break 
                
        # Entramos al ciclo while principal
        # En este ciclo se observa el operador activo 
        # y cual es el carácter que sigue
        # si es dígito(un número) o una letra (una variable)
        # Comienzan los que empiezan por un dígito(Son números)
        if operador == "+" and Expresion_Junta[i].isdigit():
            # Suma
            # Se utiliza la función es_numero para operar con ese numero y se almacena en num
            num, i = es_numero(Expresion_Junta, i)
            # Se comprueba que sea un int para realizar la operación
            # Si no es un numero, entonces es un error.
            if type(Resultado) == int:
              Resultado += num
            else:
              Resultado = Resultado

        elif operador == "-" and Expresion_Junta[i].isdigit():
           # Resta
           # Se utiliza la función es_numero para operar con ese numero y se almacena en num
           num, i = es_numero(Expresion_Junta,i)
           # Se comprueba que sea un int para realizar la operación
           # Si no es un numero, entonces es un error.
           if type(Resultado) == int:
              Resultado -= num
           else:
              Resultado = Resultado

        elif operador == "*" and Expresion_Junta[i].isdigit():
           # Multiplicación
           # Se utiliza la función es_numero para operar con ese numero y se almacena en num
           num, i = es_numero(Expresion_Junta,i)
           # Se comprueba que sea un int para realizar la operación
           # Si no es un numero, entonces es un error.
           if type(Resultado) == int:
              Resultado *= num
           else:
              Resultado = Resultado
           
        elif operador == "/" and Expresion_Junta[i].isdigit():
           # División
           # Se utiliza la función es_numero para operar con ese numero y se almacena en num
           num, i = es_numero(Expresion_Junta,i)
           # Se comprueba que sea un int para realizar la operación.
           # Si no es un numero, entonces es un error.
           if type(Resultado) == int:
              Resultado = int(Resultado/num)
           else:
              Resultado = Resultado

        elif operador == "^" and Expresion_Junta[i].isdigit():
           # Potencia
           # Se utiliza la función es_numero para operar con ese numero y se almacena en num
           num, i = es_numero(Expresion_Junta,i)
           # Se comprueba que sea un int para realizar la operación.
           # Si no es un numero, entonces es un error.
           if type(Resultado) == int:
              Resultado **= num
           else:
              Resultado = Resultado

        # Comienzan los que empiezan por una letra(Son Variables).  
        elif operador == "+" and Expresion_Junta[i].isalpha():
            # Suma
            # Se utiliza la función es_Letra y se almacena en letra(Se buscan variables en la expresión)
            letra, i = es_Letra(Expresion_Junta, i)
            # Busca la variable en el diccionario.
            if letra in dicc_var:
                # Si la variable esta en el diccionario se guarda el valor en ltr    
                ltr = dicc_var[letra]
                # Si el valor almacenado es un int se opera 
                if type(ltr) == int:
                   Resultado += ltr
                else:
                    Resultado = (("Error: La variable "+letra+" no esta definida."))
            # En otro caso retorna error indicando cual es la variable que no esta definida.        
            else: 
               Resultado=("Error: La variable "+letra+" no esta definida.")
               break
        
        elif operador == "-" and Expresion_Junta[i].isalpha():
            # Resta
            # Se utiliza la función es_Letra y se almacena en letra(Se buscan variables en la expresión)
            letra, i = es_Letra(Expresion_Junta, i)
            # Busca la variable en el diccionario.
            if letra in dicc_var:    
                # Si la variable esta en el diccionario se guarda el valor en ltr
                ltr = dicc_var[letra]
                # Si el valor almacenado es un int se opera 
                if type(ltr) == int:
                   Resultado -= ltr
                else:
                    Resultado = (("Error: La variable "+letra+" no esta definida."))
            # En otro caso retorna error indicando cual es la variable que no esta definida.         
            else: 
               Resultado=("Error: La variable "+letra+" no esta definida.")
               break
        
        elif operador == "*" and Expresion_Junta[i].isalpha():
            # Multiplicación
            # Se utiliza la función es_Letra y se almacena en letra(Se buscan variables en la expresión)
            letra, i = es_Letra(Expresion_Junta, i)
            if letra in dicc_var:
                # Si la variable esta en el diccionario se guarda el valor en ltr    
                ltr = dicc_var[letra]
                # Si el valor almacenado es un int se opera
                if type(ltr) == int:
                   Resultado *= ltr
                else:
                    Resultado = (("Error: La variable "+letra+" no esta definida."))
            # En otro caso retorna error indicando cual es la variable que no esta definida.         
            else: 
               Resultado=("Error: La variable "+letra+" no esta definida.")
               break
        
        elif operador == "/" and Expresion_Junta[i].isalpha():
            # División
            # Se utiliza la función es_Letra y se almacena en letra(Se buscan variables en la expresión)
            letra, i = es_Letra(Expresion_Junta, i)
            if letra in dicc_var:    
                # Si la variable esta en el diccionario se guarda el valor en ltr
                ltr = dicc_var[letra]
                # Si el valor almacenado es un int se opera
                if type(ltr) == int:
                   Resultado = int(Resultado/ltr)
                else:
                    Resultado = (("Error: La variable "+letra+" no esta definida."))
            # En otro caso retorna error indicando cual es la variable que no esta definida.         
            else: 
               Resultado=("Error: La variable "+letra+" no esta definida.")
               break
        
        elif operador == "^" and Expresion_Junta[i].isalpha():
            # Potencia
            # Se utiliza la función es_Letra y se almacena en letra(Se buscan variables en la expresión)
            letra, i = es_Letra(Expresion_Junta, i)
            if letra in dicc_var:    
                # Si la variable esta en el diccionario se guarda el valor en ltr
                ltr = dicc_var[letra]
                # Si el valor almacenado es un int se opera
                if type(ltr) == int:
                   Resultado **= ltr
                else:
                    Resultado = (("Error: La variable "+letra+" no esta definida."))
            # En otro caso retorna error indicando cual es la variable que no esta definida.         
            else: 
               Resultado=("Error: La variable "+letra+" no esta definida.")
               break
        # En los próximos se revisa que operación sigue y se encarga de cambiar el operador
        # Para seleccionar cual de las condiciones anteriores hay que utilizar  
        # Luego actualiza el indice para continuar con el ciclo while  
        elif Expresion_Junta[i] == "+":
            operador = "+"
            i += 1

        elif Expresion_Junta[i] == "-":
           operador = "-"
           i += 1

        elif Expresion_Junta[i] == "*":
           operador = "*"
           i += 1

        elif Expresion_Junta[i] == "/":
           operador = "/"
           i += 1
        
        elif Expresion_Junta[i] == "^":
           operador = "^"
           i += 1

        elif Expresion_Junta[i] == " ":
           i += 1
        # Este ultimo se encarga de revisar que en la expresión no existan caracteres no permitidos.
        # Establece el error para printearlo.
        else:
           Resultado = ("Error: Sintaxis incorrecta: "+Expresion_Junta[i:]+" Por favor revise su entrada.")
           break
    # Printea los resultados de nuestra calculadora    
    print(Resultado)
    # Actualiza el diccionario
    dicc_var[Variable_Junta] = Resultado
    # Retorna el diccionario
    return dicc_var
    

def calculadora(lista_comandos):
  # Creamos una lista vacía
  SinError = []
  # Este ciclo rellena la lista con los comandos omitiendo cuando el comando es ""(es decir, vacío)
  for k in range(0,len(lista_comandos)):
     if lista_comandos[k] != "":
        SinError.append(lista_comandos[k])
     else:
        None
  # Reemplazamos la lista de comandos original
  lista_comandos = SinError
    
  # Este diccionario almacena las variables que se vayan definiendo en la calculadora
  # Este diccionario se inicializa cuando se usa la calculadora
  vars = dict()

  # Se procesan todos los comandos de la lista (lista de string)
  for i in range(0, len(lista_comandos)):
    vars = procesar_comando(lista_comandos[i], vars)


 
#EJEMPLO 1:
lista = ["n=5","hanoi=2^n-1","var_1 = 23 - 13 + hanoi2 * 2","h2 = hanoi /2","","n"]
calculadora(lista)

