import pandas as pd
import numpy as np

def generate_population(n=100000, seed=42):
    """
    Simula una población para una Encuesta de Ingresos.
    Estructura: 
    - 2 Regiones (Estratos)
    - 20 Municipios (Conglomerados/Clusters)
    """
    np.random.seed(seed)
    
    # 1. Definir Estratos (Regiones)
    regions = np.random.choice(['Norte', 'Sur'], size=n, p=[0.4, 0.6])
    
    # 2. Definir Municipios (Clusters) dentro de regiones
    # Norte tiene municipios 1-8, Sur tiene 9-20
    municipality = []
    for r in regions:
        if r == 'Norte':
            municipality.append(np.random.randint(1, 9))
        else:
            municipality.append(np.random.randint(9, 21))
    
    # 3. Demográficos
    age_groups = np.random.choice(['18-29', '30-49', '50+'], size=n, p=[0.3, 0.4, 0.3])
    gender = np.random.choice(['M', 'F'], size=n, p=[0.48, 0.52])
    
    # 4. Variable Objetivo: Ingreso (Correlacionado con Región y Edad para realismo)
    base_income = 15000
    income = (
        base_income 
        + (np.where(regions == 'Norte', 5000, 0)) # Norte gana más
        + (np.where(age_groups == '30-49', 8000, 0)) # Edad media gana más
        + (np.where(age_groups == '50+', 6000, 0))
        + np.random.normal(0, 4000, n) # Ruido aleatorio
    )
    income = np.maximum(income, 4000) # Evitar negativos

    # Crear DataFrame
    df = pd.DataFrame({
        'id': range(1, n + 1),
        'region': regions,           # Estrato
        'municipio': municipality,   # Cluster (PSU)
        'age_group': age_groups,     # Variable de calibración
        'gender': gender,            # Variable de calibración
        'income': income.round(2)    # Target
    })
    
    return df

if __name__ == "__main__":
    print("Generando población sintética...")
    pop = generate_population()
    pop.to_csv('data/population_census.csv', index=False)
    print("Población guardada en data/population_census.csv")
