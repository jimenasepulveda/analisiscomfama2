#1. importo a pandas 
import pandas as pd 

#2. traigo la fuente de datos 
edadesCasa1=[25,25,25,25,25]
edadesCasa2=[1,4,24,26,70]

#3. genero los dataframes
dataframe1=pd.DataFrame(edadesCasa1)
dataframe2=pd.DataFrame(edadesCasa2)

#4. analisis descriptivo de los datos
analisis1=dataframe1.describe ()
analisis2=dataframe2.describe()

#5. mostrar resultados 
print(analisis1)
print(analisis2)