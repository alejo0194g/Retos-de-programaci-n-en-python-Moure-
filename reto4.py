"""/*
 * Reto #4
 * ÁREA DE UN POLÍGONO
 * Fecha publicación enunciado: 24/01/22
 * Fecha publicación resolución: 31/01/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""

def area_poligono():
    opc=input("El area de cual poligono quieres calcular?:\n 1: Triangulo \n 2: Cuadrado \n 3: Rectangulo \n Ingresa el número:")

    if opc=="1":
        base=float(input("Ingresa la base (b): "))
        altura=float(input("Ingresa la altura (h): "))
        area=(base*altura)/2
        print("El área del triangulo es: "+ str(area))
        return area
    elif opc=="2":
        lado=float(input("Ingresa el lado(l): "))
        area=lado*lado
        print("El área del cuadrado es: "+ str(area))
        return area
    elif opc=="3":
        base=float(input("Ingresa la base (b): "))
        altura=float(input("Ingresa la altura (h): "))
        area=base*altura
        print("El área del rectangulo es: "+ str(area))
        return area
    
    else:
        print("El valor ingresado es incorrecto, vuelve a intentarlo!")


area_poligono()