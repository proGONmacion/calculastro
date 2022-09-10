Contexto

Es una calculadora con la que puedes obtener información de la orbita elíptica de un planeta o satelite, como el tiempo de orbita, semi eje mayor o menor, afelio, perihelio, y como extra la masa del cuerpo que orbitan, solo hay que introducir los datos necesarios. En actualizaciones más avanzadas se podrá comparar 2 orbitas con puntos de intersección para comprobar si hay colisión de astros.


Algoritmo pseudo código

#variables
data_disp
data_req
#listas
data = [periodo, afelio, perihelio, ... ]
data_resul = [..., ...]

definir fórmulas de elipses y órbitas

imprimir data
preguntar: seleccione los tipos de datos que dispone
indexar lista
guardar en data_disp
preguntar: seleccione las unidades de los datos que dispone
preguntar: introduzca los datos que dispone
si data_disp = data_req
   imprimir data_resul
preguntar: que seleccione los tipos de datos que desea obtener
indexar data_resul
preguntar: seleccione las unidades que desa obtener
imprimir resultado
preguntar: si quiere cambiar unidades obtenidas
    preguntar: si quiere cambiar tipos de datos
        preguntar: si quiere iniciar nuevo calculo


