#format_results.py
def format_results(results):
    # Inicializa una cadena vacía para almacenar el resultado formateado.
    formatted_output = ""

    # Itera sobre cada elemento en los resultados.
    # 'results' es un diccionario que contiene listas asociadas a claves como 'nom', 'data', etc.
    for x in range(len(results["nom"])):
        formatted_output += "---------------\n" #Línea divisora para cada conjunto de reultados.
        formatted_output += f"Nombre: {results['nom'][x]}\n" #Nombre extraido.
        formatted_output += f"Fecha: {results['data'][x]}\n" #Fecha estraida.
        formatted_output += f"Sitio web: {results['pagina'][x]}\n" #Sitio Web estraida.
        formatted_output += f"Captura de pantalla: {results['captura'][x]}\n\n" #Path de las capturas realizadas.
    # Devuelve la cadena formateada con todos los resultados.
    return formatted_output

#j4rin4
