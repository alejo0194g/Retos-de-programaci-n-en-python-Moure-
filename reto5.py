"""/*
 * Reto #5
 * ASPECT RATIO DE UNA IMAGEN
 * Fecha publicación enunciado: 01/02/22
 * Fecha publicación resolución: 07/02/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
 * - Nota: Esta prueba no se puede resolver con el playground online de Kotlin. Se necesita Android Studio.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */
"""
from fractions import Fraction
from decimal import Decimal
import cv2
import matplotlib.pyplot as plt

def aspect_ratio(url='Retos_Maure_2022\mouredev_github_profile.png'):
    im = cv2.imread(url)
    
    #Mostrar imagen
    plt.xticks([]), plt.yticks([])
    plt.imshow(im)
    plt.show()
    print(type(im))
    print(im.shape)
    print(type(im.shape))
    h, w, c = im.shape
    print('width:  ', w)
    print('height: ', h)
    print('channel:', c)
    print("El aspect ratio de la imagen es: " + str(Fraction(str(w/h)).limit_denominator(100)))

aspect_ratio()