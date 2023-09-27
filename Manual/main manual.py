from os import system
system("cls")

from constantes import *
from colores import *
import pygame, sys
from datos import lista

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
    pregunta_actual.append(e_lista['pregunta'])
    pregunta_actual.append(e_lista['a'])
    pregunta_actual.append(e_lista['b'])
    pregunta_actual.append(e_lista['c'])
    pregunta_actual.append(e_lista['correcta'])
    preguntas.append(pregunta_actual)

score = 0
intentos = 2
pregunta_actual = 0

fuente = pygame.font.SysFont("Arial", 30)
pregunta = preguntas[pregunta_actual][0]
etiqueta_pregunta = fuente.render(str(pregunta), True, BLACK)
opcion_a = fuente.render("A. " + preguntas[pregunta_actual][1], True, BLACK)   
opcion_b = fuente.render("B. " + preguntas[pregunta_actual][2], True, BLACK)                                   
opcion_c = fuente.render("C. " + preguntas[pregunta_actual][3], True, BLACK) 
puntaje = fuente.render("Puntaje: " + str(score), True, BLACK) 

def verificar_respuesta(respuesta):
    global score, intentos, opcion_a, opcion_b, opcion_c
    if respuesta == preguntas[pregunta_actual][4]:  # correcto
        if intentos > 0:
            intentos = 0
            score += 10
        if respuesta == 'a':
            opcion_a = fuente.render("A. " + preguntas[pregunta_actual][1], True, GREEN)
            opcion_b = fuente.render("", True, BLACK)
            opcion_c = fuente.render("", True, BLACK)
        elif respuesta == 'b':
            opcion_a = fuente.render("", True, BLACK)
            opcion_b = fuente.render("B. " + preguntas[pregunta_actual][2], True, GREEN)
            opcion_c = fuente.render("", True, BLACK)
        elif respuesta == 'c':
            opcion_a = fuente.render("", True, BLACK)
            opcion_b = fuente.render("", True, BLACK)
            opcion_c = fuente.render("C. " + preguntas[pregunta_actual][3], True, GREEN)
        efecto_correcto = pygame.mixer.Sound("Preguntados\Archivos\correcto.mp3")
        efecto_correcto.set_volume(0.1)
        efecto_correcto.play()
    else:  # incorrecto
        intentos -= 1
        if respuesta == 'a':
            opcion_a = fuente.render("", True, BLACK)
        elif respuesta == 'b':
            opcion_b = fuente.render("", True, BLACK)
        elif respuesta == 'c':
            opcion_c = fuente.render("", True, BLACK)
        efecto_incorrecto = pygame.mixer.Sound("Preguntados\Archivos\incorrecto.mp3")
        efecto_incorrecto.set_volume(0.1)
        efecto_incorrecto.play()



screen_width = screen.get_width()#ancho
screen_height = screen.get_height()#alto
surface = pygame.Surface((screen_width, screen_height))#Fondo
for y in range(screen_height):
    r = CYAN[0] + (MAGENT[0] - CYAN[0]) * y // screen_height
    g = CYAN[1] + (MAGENT[1] - CYAN[1]) * y // screen_height
    b = CYAN[2] + (MAGENT[2] - CYAN[2]) * y // screen_height
    color = (r, g, b)
    pygame.draw.line(surface, color, (0, y), (screen_width, y))


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:  # salir con esc
                pygame.quit()
                sys.exit()
        #print(evento) #ES LA POSICION

        if evento.type == pygame.MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pos()
            x = click[0]
            y = click[1]
            
            if 100 <= x <= 300 and 400 <= y <= 450:#Pregunta
                pregunta_actual += 1
                intentos = 2
                pregunta = preguntas[pregunta_actual][0]
                etiqueta_pregunta = fuente.render(str(pregunta), True, BLACK)
                opcion_a = fuente.render("A. " + preguntas[pregunta_actual][1], True, BLACK)   
                opcion_b = fuente.render("B. " + preguntas[pregunta_actual][2], True, BLACK)                                   
                opcion_c = fuente.render("C. " + preguntas[pregunta_actual][3], True, BLACK) 
                puntaje = fuente.render("Puntaje: " + str(score), True, BLACK)             
            elif x >= 400 and x <= 600 and y >= 400 and y <= 450:#Reiniciar
                score = 0
                intentos = 2
                pregunta_actual = 0
                pregunta = preguntas[pregunta_actual][0]
                etiqueta_pregunta = fuente.render(str(pregunta), True, BLACK)
                opcion_a = fuente.render("A. " + preguntas[pregunta_actual][1], True, BLACK)   
                opcion_b = fuente.render("B. " + preguntas[pregunta_actual][2], True, BLACK)                                   
                opcion_c = fuente.render("C. " + preguntas[pregunta_actual][3], True, BLACK) 
                puntaje = fuente.render("Puntaje: " + str(score), True, BLACK) 
            elif 50 <= x <= 200 and 200 <= y <= 230:
                if verificar_respuesta('a'):
                    pregunta_actual += 1
                    if pregunta_actual >= len(preguntas):
                        break
            elif 50 <= x <= 200 and 260 <= y <= 280:
                if verificar_respuesta('b'):
                    pregunta_actual += 1
                    if pregunta_actual >= len(preguntas):
                        break
            elif 50 <= x <= 200 and 310 <= y <= 335:
                if verificar_respuesta('c'):
                    pregunta_actual += 1
                    if pregunta_actual >= len(preguntas):
                        break


    screen.blit(surface, (0, 0))

    boton_pregunta = pygame.draw.rect(screen, ORANGE, (100, 400, 200, 50))
    boton_reiniciar = pygame.draw.rect(screen, ORANGE, (400, 400, 200, 50))
    fuente = pygame.font.SysFont("Arial", 30)
    etiqueta_boton_pregunta = fuente.render("Pregunta", True, WHITE)
    reiniciar = fuente.render("Reiniciar", True, WHITE)

    screen.blit(etiqueta_boton_pregunta, (150, 405))#texto pregunta
    screen.blit(reiniciar, (450, 405))#texto reiniciar
    screen.blit(etiqueta_pregunta, (50, 100))
    screen.blit(opcion_a, (50, 200))   
    screen.blit(opcion_b, (50, 250))
    screen.blit(opcion_c, (50, 300))
    screen.blit(puntaje, (10, 10))


    screen.blit(icono, (408, 200))
    screen.blit(titulo, (280, 2))

    pygame.display.flip()



