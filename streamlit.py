from email.policy import default
import streamlit as st
import pandas as pd
import plotly.express as px



read_col = ['AÑO','DEPARTAMENTO','MUNICIPIO','APROBACIÓN', 'APROBACIÓN_TRANSICIÓN', 'APROBACIÓN_PRIMARIA', 'APROBACIÓN_SECUNDARIA', 'APROBACIÓN_MEDIA']
df = pd.read_csv("https://raw.githubusercontent.com/JJPC98/DiplomadoPython/main/MEN_ESTADISTICAS_EN_EDUCACION_EN_PREESCOLAR__B_SICA_Y_MEDIA_POR_MUNICIPIO_LIMPIO.csv" , usecols=read_col)  

# Using object notation
genre_bar = st.sidebar.radio(
            "Navigate",
            ('Homepage','Exploracion'))

if genre_bar == 'Homepage':
    st.title("Estadísticas de aprobación escolar 📊 (DASHBOARD) 📊" ) 
    st.write('📌 ABOUT US')
    st.write('Este DASHBOARD fue elaborado con fines académicos, con el propósito de mostrar cual es la tasa de aprobación escolar en todos los departamentos de Colombia. Nuestro equipo está conformado por: Juan Ramos, Jeremías Palacio, Jesús Hoyos, Camilo Ganem y Yesica Durango')
    agree = st.checkbox('Display Data')

    if agree:
        st.dataframe(df)
    agree_columns = st.checkbox('Columns')
    if agree_columns:
        st.write(df.columns)

    genre = st.radio(
        "¿Qué dimensión quieres ver?",
        ('Row', 'Colomns'))

    if genre == 'Row':
        st.write('Cantidad de filas del Dataframe')
        st.write(df.shape[0])
    else:
        st.write('Cantidad de columnas del Dataframe')
        st.write(df.shape[1])

    agree_describe = st.checkbox('📈 Estadísticas Generales 📈')
    if agree_describe: 
        st.write(df.describe())

else:

    st.sidebar.header('Ingrese los datos')
    DEPARTAMENTO = st.sidebar.multiselect("Selecciona departamento:", options=df['DEPARTAMENTO'].unique() , default =df['DEPARTAMENTO'].unique() )
    df_selection = df.query("DEPARTAMENTO == @DEPARTAMENTO")

    # st.dataframe(df_selection)
    st.title("🔍 Exploración de datos (graficas)") 

    dataframe_depatamento = (
    df_selection.loc[:,['DEPARTAMENTO','APROBACIÓN']].groupby('DEPARTAMENTO').mean('APROBACIÓN')
    )

    fig = px.bar(
        dataframe_depatamento,
        x = "APROBACIÓN",
        y = dataframe_depatamento.index,
        orientation = "h",
        title= "<b> Nivel de aprobación a nivel departamental </b>",
        color_discrete_sequence = ["#FF4B4B"] * len(dataframe_depatamento),
        template = "plotly_white"
    )

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis = (dict(showgrid=False))
    )

    AÑO = st.sidebar.multiselect("Selecciona los años:", options=df['AÑO'].unique() , default =df['AÑO'].unique() )
    df_selection_año = df.query("AÑO == @AÑO")

    dataframe_año = (
        df_selection_año.loc[:,['AÑO','APROBACIÓN']].groupby('AÑO').mean('APROBACIÓN')
        )

    fig_2 = px.line(
        dataframe_año,
        x = dataframe_año.index,
        y = "APROBACIÓN",
        title= "<b> Serie de tiempo (aprobación con respecto el año) </b>",
        color_discrete_sequence = ["#FF4B4B"] * len(dataframe_depatamento),
        template = "plotly_white"
    )


    st.plotly_chart(fig)
    st.plotly_chart(fig_2)

    st.sidebar.title('📩 Contact us')

























# option = st.sidebar.selectbox(
#      'Elija un departamento',
#      ('Amazonas', 'Antioquia', 'Arauca', 'Atlantico', 'Bogota DC', 'Bolivar', 'Boyaca', 
#      'Caldas', 'Caquetá', 'Casanare', 'Cauca', 'Cesar', 'Choco', 'Cordoba', 'Cundinamarca', 'Guainia', 
#      'Guaviare', 'Huila', 'La Guajira', 'Magdalena', 'Meta', 'Nariño', 'Norte de Santander', 'Putumayo', 
#      'Quindio', 'Risaralda', 'San Andres y Providencia', 'Santander', 'Sucre', 'Tolima', 'Valle del Cauca',
#      'Vaupés', 'Vichada'))

#     selected_year = st.sidebar.selectbox('AÑO', list(reversed(range(2011,2025))))
