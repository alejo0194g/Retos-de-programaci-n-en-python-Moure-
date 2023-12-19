"""/*
 * Reto #7
 * CONTANDO PALABRAS
 * Fecha publicación enunciado: 14/02/22
 * Fecha publicación resolución: 21/02/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""

def contador_palabras(cadenaPalabras):

    cadenaPalabras=cadenaPalabras.lower().replace(".","").replace(",","")
    listaPalabras = cadenaPalabras.split()

    frecuenciaPalab = []
     
    for w in listaPalabras:
        frecuenciaPalab.append(listaPalabras.count(w))

    print("Cadena\n" + cadenaPalabras +"\n")
    print("Lista\n" + str(listaPalabras) + "\n")
    print("Frecuencias\n" + str(frecuenciaPalab) + "\n")

texto="it was the best. of times it was the worst of times,it was the age. of wisdom it was the age of foolishness"
contador_palabras(texto)