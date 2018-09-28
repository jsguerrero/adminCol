\c appcolonias

\echo colonias_cat_pais
\copy colonias_cat_pais FROM 'datosCP/catpais.csv' DELIMITERS ',' CSV;

\echo colonias_cat_estado
\copy colonias_cat_estado FROM 'datosCP/catestado.csv' DELIMITERS ',' CSV;

\echo colonias_cat_municipio
\copy colonias_cat_municipio FROM 'datosCP/catmunicipio.csv' DELIMITERS ',' CSV;

\echo colonias_cat_codigo_postal
\copy colonias_cat_codigo_postal FROM 'datosCP/catcodigopostal.csv' DELIMITERS ',' CSV;

\echo colonias_cat_tipo_asentamiento
\copy colonias_cat_tipo_asentamiento FROM 'datosCP/cattipoasentamiento.csv' DELIMITERS ',' CSV;

\echo colonias_cat_asentamiento
\copy colonias_cat_asentamiento FROM 'datosCP/catasentamiento2.csv' DELIMITERS ',' CSV;
