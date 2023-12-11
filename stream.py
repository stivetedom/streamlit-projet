import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from main import load_data, display_data, display_stats

def display_statistics(data):
    st.sidebar.subheader("Statistiques")

    # Liste des graphiques disponibles
    graph_options = [
        "Informations de base",
        "Distribution des caractéristiques catégorielles",
        "Boîtes à moustaches pour les caractéristiques numériques",
        "Matrice de corrélation des caractéristiques numériques",
        "Diagramme en paires (Optionnel)",
        "Relation entre les caractéristiques catégorielles et une caractéristique numérique spécifique"
    ]

    # Menu déroulant pour choisir le graphique
    selected_option = st.sidebar.selectbox("Sélectionnez le type de graphique", graph_options)

    # Condition pour afficher le graphique correspondant
    if st.sidebar.button("Afficher le graphique"):
        st.subheader(selected_option)

        if selected_option == "Informations de base":
            st.write(data.info())
            st.write(data.describe())
        elif selected_option == "Distribution des caractéristiques catégorielles":
            categorical_columns = ['Age', 'Gender', 'Country', 'Ethnicity', 'Education']
            for col in categorical_columns:
                plt.figure(figsize=(10, 4))
                sns.countplot(x=col, data=data)
                plt.title(f'Distribution of {col}')
                plt.xticks(rotation=45)
                st.pyplot()
        # Ajoutez d'autres conditions pour les autres options de graphiques

if __name__ == "__main__":
    data = load_data()

    st.set_page_config(
        page_title="Drogue App",
        page_icon="🚬",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("Analyse de la consommation de drogue")

    # Afficher les données
    st.sidebar.subheader("Visualisation des Données")
    display_data(data)

    # Bouton pour afficher les statistiques
    display_statistics(data)

    # Afficher les statistiques par défaut
    display_stats(data)



