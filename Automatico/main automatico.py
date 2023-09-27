from os import system
system("cls")

from constantes import *
from colores import *
import pygame, sys
from datos import lista

#Agustin Lopez Preguntados
pygame.init()

screen = pygame.display.set_mode(PANTALLA)
pygame.display.set_caption("Preguntados")
icono = pygame.image.load("Preguntados\Archivos\icono.png")
pygame.display.set_icon(icono)
icono = pygame.transform.scale(icono, (150, 150))
titulo = pygame.image.load("Preguntados\Archivos\preguntadosTitulo.png")
titulo = pygame.transform.scale(titulo, (250, 100))
pygame.mixer.music.load("Preguntados\Archivos\musica.mp3")
pygame.mixer.music.play(-1) 
pygame.mixer.music.set_volume(0.1)



preguntas = []
for e_lista in lista:
    pregunta_actual = []
    pregunta_actual.append(e_lista["pregunta"])
    pregunta_actual.append(e_lista["a"])
    pregunta_actual.append(e_lista["b"])
    pregunta_actual.append(e_lista["c"])
    pregunta_actual.append(e_lista["correcta"])
    preguntas.append(pregunta_actual)

score = 0
intentos = 2
pregunta_actual = 0
toques_incorrectos = 0
respuestas_incorrectas = 0


fuente = pygame.font.SysFont("Arial", 30)
pregunta = preguntas[pregunta_actual][0]
etiqueta_pregunta = fuente.render(str(pregunta), True, BLACK)
opcion_a = fuente.render("A. " + preguntas[pregunta_actual][1], True, BLACK)   
opcion_b = fuente.render("B. " + preguntas[pregunta_actual][2], True, BLACK)                                   
opcion_c = fuente.render("C. " + preguntas[pregunta_actual][3], True, BLACK) 
puntaje = fuente.render("Puntaje: " + str(score), True, BLACK) 

def actualizar_pregunta():
    """brief: la funcion actualiza(pasa a la siguiente pregunta automaticamente)
    parametros: pregunta etiqueta_pregunta opcion_a opcion_b opcion_c puntaje pregunta_actual preguntas
    return: False"""
    global pregunta, etiqueta_pregunta, opcion_a, opcion_b, opcion_c, puntaje
    pregunta = preguntas[pregunta_actual][0]
    etiqueta_pregunta = fuente.render(str(pregunta), True, BLACK)
    opcion_a = fuente.render("A. " + preguntas[pregunta_actual][1], True, BLACK)
    opcion_b = fuente.render("B. " + preguntas[pregunta_actual][2], True, BLACK)
    opcion_c = fuente.render("C. " + preguntas[pregunta_actual][3], True, BLACK)
    puntaje = fuente.render("Puntaje: " + str(score), True, BLACK)

def siguiente_pregunta():
    """brief: La función pasa a la siguiente pregunta sumando 1 al actual
    parametros: pregunta_actual respuestas_incorrectas preguntas
    return: None"""
    global pregunta_actual, respuestas_incorrectas
    pregunta_actual += 1
    if pregunta_actual >= len(preguntas):
        pregunta_actual = 0 #funciona el boton pregunta (manual)
    respuestas_incorrectas = 0  # Reiniciar el contador de respuestas incorrectas
    actualizar_pregunta()



def verificar_respuesta(respuesta):
    """brief: La función verifica si la respuesta(A,B,C) son correctas o incorrectas, dando su respectivo sonido de in/correcto
    parametros: score pregunta_actual opcion_a opcion_b opcion_c intentos respuestas_incorrectas respuesta preguntas efecto_correcto efecto_incorrecto
    return: False"""
    global score, pregunta_actual, opcion_a, opcion_b, opcion_c, intentos, respuestas_incorrectas
    if respuesta == preguntas[pregunta_actual][4]:  # Correcto
        if intentos > 0 or 1: # 1 porque por alguna razon se bugeaba en tercera pregunta
            opcion_a = fuente.render("A. " + preguntas[pregunta_actual][1], True, BLACK)
            opcion_b = fuente.render("B. " + preguntas[pregunta_actual][2], True, BLACK)
            opcion_c = fuente.render("C. " + preguntas[pregunta_actual][3], True, BLACK)
            efecto_correcto = pygame.mixer.Sound("Preguntados\Archivos\correcto.mp3")
            efecto_correcto.set_volume(0.1)
            efecto_correcto.play()
            siguiente_pregunta()
        score += 10
    else:  # Incorrecto
        intentos -= 1
        if respuesta == 'a':
            opcion_a = fuente.render("", True, BLACK)
        elif respuesta == 'b':
            opcion_b = fuente.render("", True, BLACK)
        elif respuesta == 'c':
            opcion_c = fuente.render("", True, BLACK)
        respuestas_incorrectas += 1
        efecto_incorrecto = pygame.mixer.Sound("Preguntados\Archivos\incorrecto.mp3")
        efecto_incorrecto.set_volume(0.1)
        efecto_incorrecto.play()
        if respuestas_incorrectas >= 2:# 2 oportunidades
            respuestas_incorrectas = 0
            siguiente_pregunta()


ancho_screen = screen.get_width()
altura_screen = screen.get_height()
surface = pygame.Surface((ancho_screen, altura_screen))#Fondo
for y in range(altura_screen):
    r = CYAN[0] + (MAGENT[0] - CYAN[0]) * y // altura_screen
    g = CYAN[1] + (MAGENT[1] - CYAN[1]) * y // altura_screen
    b = CYAN[2] + (MAGENT[2] - CYAN[2]) * y // altura_screen
    color = (r, g, b)
    pygame.draw.line(surface, color, (0, y), (ancho_screen, y))


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:  # Salir con Esc
                pygame.quit()
                sys.exit()
        #print(evento)

        if evento.type == pygame.MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pos()
            x = click[0]
            y = click[1]

            if 100 <= x <= 300 and 400 <= y <= 450:  # Pregunta
                siguiente_pregunta()

            elif x >= 400 and x <= 600 and y >= 400 and y <= 450:  # Reiniciar
                score = 0
                intentos = 2
                pregunta_actual = 0
                actualizar_pregunta()

            elif 50 <= x <= 200 and 200 <= y <= 230:
                verificar_respuesta('a')
            elif 50 <= x <= 200 and 260 <= y <= 280:
                verificar_respuesta('b')
            elif 50 <= x <= 200 and 310 <= y <= 335:
                verificar_respuesta('c')

    screen.blit(surface, (0, 0))

    boton_pregunta = pygame.draw.rect(screen, ORANGE, (100, 400, 200, 50))
    boton_reiniciar = pygame.draw.rect(screen, ORANGE, (400, 400, 200, 50))
    fuente = pygame.font.SysFont("Arial", 30)
    etiqueta_boton_pregunta = fuente.render("Pregunta", True, WHITE)
    reiniciar = fuente.render("Reiniciar", True, WHITE)
    puntaje = fuente.render("Puntaje: " + str(score), True, BLACK)


    screen.blit(etiqueta_pregunta, (50, 100))
    screen.blit(etiqueta_boton_pregunta, (150, 405))
    screen.blit(reiniciar, (450, 405))
    screen.blit(icono, (408, 200))
    screen.blit(titulo, (280, 2))
    screen.blit(opcion_a, (50, 200))
    screen.blit(opcion_b, (50, 250))
    screen.blit(opcion_c, (50, 300))
    screen.blit(puntaje, (10, 10))

    pygame.display.flip()

