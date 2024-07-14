import streamlit as st
from logica import inquilinos_compatibles
from functions import generar_grafico_compatibilidad, generar_tabla_compatibilidad, obtener_id_inquilinos

# Configurar la página para utilizar un layout más amplio.

st.set_page_config(layout="wide")

resultado = None

# Mostrar una gran imagen en la parte superior.
st.image('./src/portada2.PNG', use_column_width=True)

# Insertar un espacio vertical de 60px
st.markdown(f'<div style="margin-top: 60px;"></div>', unsafe_allow_html=True)

# Configurar el sidebar con inputs y un botón.
with st.sidebar:
    st.header("Who is already living in the apartment?")
    inquilino1 = st.text_input("Host 1")
    inquilino2 = st.text_input("Host 2")
    inquilino3 = st.text_input("Host 3")
    
    num_compañeros = st.text_input("How many new roommates do you want to search for?")
    
    if st.button('Find new roommates'):
        # Verifica que el número de compañeros sea un valor válido
        try:
            topn = int(num_compañeros)
        except ValueError:
            st.error("Please enter a valid number for the number of roommates.")
            topn = None
        
        # Obtener los identificadores de inquilinos utilizando la función
        id_inquilinos = obtener_id_inquilinos(inquilino1, inquilino2, inquilino3, topn)

        if id_inquilinos and topn is not None:
            # Llama a la función inquilinos_compatibles con los parámetros correspondientes
            resultado = inquilinos_compatibles(id_inquilinos, topn)

# Verificar si 'resultado' contiene un mensaje de error (cadena de texto)
if isinstance(resultado, str):
    st.error(resultado)
# Si no, y si 'resultado' no es None, mostrar el gráfico de barras y la tabla
elif resultado is not None:
    cols = st.columns((1, 2))  # Divide el layout en 2 columnas
    
    with cols[0]:  # Esto hace que el gráfico y su título aparezcan en la primera columna
        st.write("Compatibility level of each new roommate:")
        fig_grafico = generar_grafico_compatibilidad(resultado[1])
        st.pyplot(fig_grafico)
    
    with cols[1]:  # Esto hace que la tabla y su título aparezcan en la segunda columna
        st.write("Comparison between roommates:")
        fig_tabla = generar_tabla_compatibilidad(resultado)
        fig_tabla.update_layout(height=380)

        st.plotly_chart(fig_tabla, use_container_width=True)
