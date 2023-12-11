import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

def generate_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def display_data(data):
    st.title('Les données de Consommation de Drogue')

    # Générer automatiquement des couleurs pour chaque colonne
    column_colors = {col: f'background: {generate_random_color()}' for col in data.columns}

    # Ajuster la largeur du tableau pour remplir la page
    st.write(data.style.apply(lambda x: [column_colors[col] for col in data.columns], axis=1).set_table_styles([{
        'selector': 'th',
        'props': [('background', '#FFA07A')]  # Couleur de fond pour les en-têtes
    }]))
def display_stats(data):
    # ... votre code pour afficher les statistiques ici ...
    st.subheader('1. Basic Information')
    st.text(data.info())
    st.text(data.describe())
    st.subheader('2. Distribution of Categorical Features')
    categorical_columns = ['Age', 'Gender', 'Country', 'Ethnicity', 'Education']
    for col in categorical_columns:
        st.pyplot(plt.figure(figsize=(10, 4)))
        sns.countplot(x=col, data=data)
        plt.title(f'Distribution of {col}')
        plt.xticks(rotation=45)
        st.pyplot()

    st.subheader('3. Boxplots for Numerical Features')
    numeric_columns = ['Nscore', 'Escore', 'Oscore', 'Ascore', 'Cscore', 'Impulsive', 'SS']
    for col in numeric_columns:
        st.pyplot(plt.figure(figsize=(10, 4)))
        sns.boxplot(x=col, data=data)
        plt.title(f'Boxplot of {col}')
        st.pyplot()

    st.subheader('4. Correlation Matrix of Numerical Features')
    plt.figure(figsize=(10, 8))
    sns.heatmap(data[numeric_columns].corr(), annot=True, fmt='.2f', cmap='coolwarm')
    plt.title('Correlation Matrix')
    st.pyplot()

    st.subheader('5. Relationship between Categorical Features and Nscore')
    for col in categorical_columns:
        st.pyplot(plt.figure(figsize=(10, 4)))
        sns.boxplot(x=col, y='Nscore', data=data)
        plt.title(f'Nscore vs {col}')
        plt.xticks(rotation=45)
        st.pyplot()
    st.header("Drug Users vs Non-Drug Users for Each Drug")

    # List of drug columns in the new dataset
    new_drug_columns = ['Alcohol', 'Amphet', 'Amyl', 'Benzos', 'Caff', 'Cannabis', 'Choc', 'Coke',
                    'Crack', 'Ecstasy', 'Heroin', 'Ketamine', 'Legalh', 'LSD', 'Meth',
                    'Mushrooms', 'Nicotine', 'Semer', 'VSA']

    # List of personality traits columns
    personality_traits = ['Nscore', 'Escore', 'Oscore', 'Ascore', 'Cscore', 'Impulsive', 'SS']
    new_drug_use_counts = {}
    for col in new_drug_columns:
        new_drug_use_counts[col] = data[col].value_counts()

    new_plot_data = {}
    for drug, counts in new_drug_use_counts.items():
        user_count = counts.drop('CL0', errors='ignore').sum()
        non_user_count = counts.get('CL0', 0)
        new_plot_data[drug] = [user_count, non_user_count]

    new_plot_df = pd.DataFrame.from_dict(new_plot_data, orient='index', columns=['Users', 'Non-Users'])
    st.bar_chart(new_plot_df)

    # Ajout du deuxième graphique
    st.header("Drug Consumption Distribution")
    colors = sns.color_palette('husl', 7)

    plt.figure(figsize=(25, 15))

    for i, drug in enumerate(new_drug_columns, 1):
        plt.subplot(5, 4, i)
        value_counts = data[drug].value_counts().sort_index()
        value_counts.plot(kind='bar', color=colors)
        plt.title(f'{drug} Consumption')
        plt.xlabel('Class')
        plt.ylabel('Count')

    legend_text = 'CL0: Never Used\nCL1: Used over a Decade Ago\nCL2: Used in Last Decade\nCL3: Used in Last Year\nCL4: Used in Last Month\nCL5: Used in Last Week\nCL6: Used in Last Day'
    plt.text(0.8, 0.1, legend_text, fontsize=12, color='black', transform=plt.gcf().transFigure, ha='left')

    plt.tight_layout()
    st.pyplot()

    # Ajout du troisième graphique
    st.header("Correlation Between Drug Use and Personality Traits")
    drug_columns = ['Alcohol', 'Cannabis', 'Coke', 'Ecstasy', 'Nicotine']
    personality_traits = ['Nscore', 'Escore', 'Oscore', 'Ascore', 'Cscore', 'Impulsive', 'SS']

    drugs_and_personality = data[drug_columns + personality_traits]
    conversion_dict = {f'CL{i}': i for i in range(7)}
    drugs_and_personality.replace(conversion_dict, inplace=True)

    correlation_matrix = drugs_and_personality.corr()

    plt.figure(figsize=(20, 15))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title("Correlation Between Drug Use and Personality Traits")
    st.pyplot()




