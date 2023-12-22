"""/*
 * Reto #16
 * EN MAYÚSCULA
 * Fecha publicación enunciado: 18/04/22
 * Fecha publicación resolución: 25/04/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""

def Mayuscula(texto):
    texto=str(texto)
    salida=[]
    mayusculas=[]
    indice=[]
    modificado=""
    
    for i,v in enumerate(texto):

        if i==0:
            mayusculas.append(texto[i].capitalize())
            indice.append(i)
            
        if v== " ":
            mayusculas.append(texto[i+1].capitalize())
            indice.append(i+1)

        salida.append(v)

    for q in range(len(mayusculas)):
        salida.pop(indice[q])
        salida.insert(indice[q],mayusculas[q])

    for q in salida:
        modificado+=q

    print(modificado)
    
Mayuscula("alejandro duque ciro, ana lucia duque ciro")