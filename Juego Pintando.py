from turtle import *
from freegames import vector
import math

#Esta función crea una linea recta
def line(start, end):
    "Draw line from start to end."
    up() #Deja de pintar
    goto(start.x, start.y) #Se va a donde se hizo clic
    down() #Comienza a pintar
    goto(end.x, end.y) #Va a donde se hizo el segundo clic

#Esta función crea un cuadrado
def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill() #Comienza a llenarlo del color guardado

    #Este for avanza la distancia entre clics y después gira 90
    #grados para repetir la acción hasta completar el cuadrado
    for count in range(4): 
        forward(end.x - start.x)
        left(90)

    end_fill() #Se termina de llenar y aparece el color
    
#Esta función crea un circulo
def circle(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    #Aunque hay una función para circulo funciona de la misma
    #manera y no es más eficiente. La distancia que avanza se
    #calculó despejando la fórmula de diametro para conseguir
    #que el círculo al final tuviera un radio igual a la distancia
    #entre los dos clics.
    for count in range(90):
        forward( (end.x - start.x)*2*math.pi/90)
        left(4) #Gira 4 grados a la izquierda
                

    end_fill()
    

#Esta función crea un rectángulo
def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    for count in range (2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)
        
    end_fill()
        

#Esta función crea un triángulo
def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)
        

    end_fill()

#Esta función guarda la posición inicial cuando haces click
def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

#Esta función guarda la tecla presionada
def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line} #Parámetros iniciales
setup(420, 420, 370, 0) #Crea el espacio inicial con esas medidas
onscreenclick(tap) #Cuando se hace click se guarda la posición
listen() #Esta linea "escucha" todo lo que se escribe para cambiar figura o color
onkey(undo, 'u') #Deshace la accion anterior presionando "u"
#Las siguientes lineas tienen la estructura:
#onkey(lambda: color('color_name'), 'Tecla')
#y cambian el color al presionar esa tecla
onkey(lambda: color('black'), 'K') 
onkey(lambda: color('white'), 'W') 
onkey(lambda: color('green'), 'G') 
onkey(lambda: color('blue'), 'B') 
onkey(lambda: color('red'), 'R')
onkey(lambda: color('magenta'), 'M')
#Las siguientesl lineas tienen la estructura:
#onkey(lambda: store('shape', funcion_forma), 'Tecla')
#y llaman a la función de dicha forma al presionar la tecla adecuada
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()