datos = ["semieje mayor", "periodo orbital",
         "masa del cuerpo que es el foco de la orbita"]
datos_disp = []
datos_resul = ""

semieje_mayor = 0.0
periodo = 0.0
masa_centro = 0.0
G = 6.673*10**(-11)
k = 4*3.141592653589793**2

def asigna(i,opcion):
    if i == datos[0]:
        semieje_mayor = float(opcion)
    if i == datos[1]:
        periodo = float(opcion)
    if i == datos[2]:
        masa_centro = float(opcion)
            
    

contexto = "para seleccionar datos o unidades introduzca"
explicacion = "el número a la izquierda de estos cuando aparezcan"
aja = "teclea enter para continuar"
instruccion = "seleccione los datos que dispone,"
espera = "teclear enter después de cada número que introduzca"
unidades = "este programa solo acepta y devuelve valores en las siguientes unidades"
cuales = "kilometros para distancia, días para tiempo y kilogramos para masa"
que = "escriba el valor de"


print(contexto, explicacion)
print(aja)
print("")
for d in datos:
    print(datos.index(d) + 1 , d)
print("")
print(0, "siguiente")
print("")
print(instruccion, espera)

while 1 == 1:
    
    entrada = "no"
    while "no" == entrada:
        opcion1 = input().strip()
        for i in range(len(datos) + 1):
            if opcion1 == str(i):
                break
        else:
            print("entrada no valida, intente de nuevo")
            continue
        entrada = "si"
    # esto hizo que no arroje error si el input no es un número
        
    if "0" == opcion1:
        break
    datos_disp.append(datos[int(opcion1) - 1])
    
print(unidades, cuales)
print("")

for x in datos_disp:
    print(que, x)
    
    entrada = "no"
    while "no" == entrada:
        opcion2 = input().strip()
        try:
            float(opcion2)
        except:
            print("entrada no valida, intente de nuevo")
            continue
        else:
            entrada = "si"
    """el bloque try evalúa si el código dentro da error, si sí, se ejecuta el código
    dentro del bloque except, si no, se ejecuta el codigo dentro del bloque else"""
            
    asigna(x,opcion2)

if bool(semieje_mayor) and bool(periodo):
    datos_resul = datos[2]
if bool(semieje_mayor) and bool(masa_centro):
    datos_resul = datos[1]
if bool(masa_centro) and bool(periodo):
    datos_resul = datos[0]
    
       
if datos_resul == datos[0]:
    semieje_mayor = ((G*masa_centro*periodo**2)/k)**(1/3)
    print(datos_resul,semieje_mayor)
if datos_resul == datos[1]:
    periodo = ((k*semieje_mayor**3)/(G*masa_centro))**(1/2)
    print(datos_resul,periodo)
if datos_resul == datos[2]:
    masa_centro = (k*semieje_mayor**3)/(G*periodo**2)
    print(datos_resul,masa_centro)    
    
    


    

    

    




    


    

        
