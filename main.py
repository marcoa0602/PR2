url = 'https://raw.githubusercontent.com/marcoa0602/PR2/main/Datos/datos_brutos.csv?token=GHSAT0AAAAAACF4WCPNC4XFSRPO72TSEA7SZG6LEVQ'

from ETL import tuberia_de_datos
tuberia = tuberia_de_datos(url)

from ML import clasificacion
score = clasificacion(tuberia)
score