# APP El inquilino ideal

Caso práctico que combina data science, análisis de datos y el sector inmobiliario. Se quiere mostrar como usar Data Science para solucionar problemas complejos en un contexto de negocio real.

El caso deberá analizar y responder qué compañero resulta idóneo de entre 12000 posibles candidatos según las respuestas dadas a un total de 17 preguntas para compartir un piso con varias habitaciones dónde mínimo alguna de ellas ya está ocupada.

Veremos cómo transformar un desafío del mundo real en una solución práctica usando herramientas de Data Science como Python, Pandas, Streamlit y Numpy. Además, se hace uso de Streamlit para crear una aplicación interactiva tras procesar el dataset y extraer la solución con los inputs que el usuario introduzca

## Tecnologías utilizadas

- Python
- Pandas
- Numpy
- Scikit-learn
- Matplotlib
- Seaborn
- Plotly
- Streamlit

## Ejemplo de uso

![header_photo](https://github.com/CarlEstP/app_inquilino_ideal/blob/main/src/exa.PNG)

- _Caso práctico adaptado de la propuesta del canal DS4B_ \*

## Descripción de la lógica de la app

1 Arranca la app desde app.py generando el frontend con la ayuda de streamlit

2 Se accede al archivo de funciones.py para reformatear los identificadores de inquilino introducidos en el formulario

3 Se ejecuta la función de buscar los inquilinos compatibles (Acceder al jupyter notebook de logica.ipynb para más detalles):

- Se usa la librería OneHotEncoder y se calcula la matriz de similaridad utilizando el punto producto
- Se define el rango de destino, se encuentra el mínimo y máximo valor y se reescala la matriz
- Se crea un nuevo dataframe con Pandas
- Se buscan los inquilinos compatibles teniendo en cuenta cuántos inquilinos ya residen y cuántos hay que añadir a la vivienda.
- La función devolverá una lista con los inquilinos compatibles, y los datos de similaridad

4 Si hay resultado válido se muestra la tabla y el gráfico de compatibilidad
