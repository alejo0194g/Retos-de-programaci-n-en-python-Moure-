"""/*
 * Reto #10
 * EXPRESIONES EQUILIBRADAS
 * Fecha publicación enunciado: 07/03/22
 * Fecha publicación resolución: 14/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""


def balaceada(expresion):
    texto=str(expresion)
    llaveder=0
    llaveizq=0
    corder=0
    corizq=0
    parder=0
    parizq=0
    for q in texto:
       
        
        if "{"== q:
            llaveizq+=1
        elif "}"== q:
            llaveder+=1
        elif "["== q:
            corizq+=1
        elif "]"== q:
            corder+=1
        elif "("== q:
            parizq+=1
        elif ")"== q:
            parder+=1
    if corder ==corizq and parder ==parizq and llaveder ==llaveizq:
        print("Expresión equilibrada")
        
    else:
        print("Expresión no equilibrada")
        if corder !=corizq:
            print("Corchetes no equilibrados")
        if parder !=parizq:
            print("Parentesis no equilibrados")
        if llaveder !=llaveizq:
            print("Llaves no equilibradas")

balaceada("{ [ a * ( c + d ) ] - 5 }" )
        

