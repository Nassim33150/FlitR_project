from sqlalchemy import create_engine
import pandas as pd

# Chargement du fichier CSV dans un DataFrame pandas
df = pd.read_csv('/root/FlitR_project/data/df_encoded.csv')

# Connexion à la base de données
engine = create_engine('mysql+pymysql://nassim:adamou33@localhost:3306/SystemeRecommandation')
con = engine.connect()

# Importation du DataFrame dans la base de données
df.to_sql(name='dataframe', con=con, if_exists='append', index=False)

# Fermeture de la connexion
con.close()
