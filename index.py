import pandas as pd

from apicall import get_api_call

from rdflib import Graph, Literal, Namespace, RDF, URIRef
from datetime import datetime


storage_options = {'User-Agent': 'Mozilla/5.0'}


df = pd.read_csv(get_api_call(
    ["tcrse_2weZeH"],
    format="csv"
),storage_options=storage_options)

# Crear un grafo RDF
g = Graph()

# Definir un namespace para los términos RDF
ns = Namespace("https://datos.gob.ar/series/api/series/?ids=tcrse_2weZeH/")

# Iterar sobre las filas del DataFrame y agregar triples RDF al grafo
for index, row in df.iterrows():
    # Convertir el índice de tiempo a un formato compatible con RDF (puede que necesites ajustar esto según tu caso)
    fecha = datetime.strptime(row['indice_tiempo'], '%Y-%m-%d')
    
    # Construir el URI para la observación
    observacion_uri = ns[str(index)]
    
    # Agregar triple RDF para el índice de tiempo
    g.add((observacion_uri, ns['fecha'], Literal(fecha)))
    
    # Agregar triple RDF para el valor de producción y procesamiento de alimentos
    g.add((observacion_uri, ns['produccion_y_procesamiento_de_alimentos'], Literal(row['151_produccion_y_procesamiento_de_alimentos'])))


g.print()
# Guardar el grafo RDF en un archivo
g.serialize(destination='tu_archivo.rdf', format='xml')
# pd.set_option('display.max_rows', 100)  # Esto mostrará hasta 100 filas
# pd.set_option('display.max_columns', 2)


# print(df)

