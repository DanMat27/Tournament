# Tournament

-----------

### Descripción:
El usuario debe introducir el número de participantes del torneo a la hora de ejecutar el programa de 
la siguiente manera: 

> python3 tournament.py NUM_PARTICIPANTES  

Este número está limitado a 4 u 8 participantes.  
Tras ejecutar el programa con el número indicado, hay que introducir uno a uno por teclado los participantes
del torneo. El programa generará aleatoriamente los enfrentamientos del torneo y lo mostrará por pantalla (terminal).

-----------

### Visualización del torneo:

Torneo de 4 personas:
p1                                                                  p3
 |                                                                  |
 -----------------------                       ----------------------
                       |                       |
                       -------------------------
                       |                       |
 -----------------------                       ----------------------
 |                                                                  |
p2                                                                  p4

Torneo de 8 personas:
p8                                                                  p6
 |                                                                  |
 -----------------------                       ----------------------
                       |                       |
p3                     -------           -------                    p7
 |                     |     |           |     |                    |
 -----------------------     |           |     ----------------------
                             -------------
 -----------------------     |           |     ----------------------
 |                     |     |           |     |                    |
p2                     -------           -------                    p4
                       |                       |
 -----------------------                       ----------------------
 |                                                                  |
p1                                                                  p5

(La distribución de los participantes es un ejemplo puntual)

-----------

Para ejecutar este programa hay que utilizar Python3.
