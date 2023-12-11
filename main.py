import streamlit as st 
import pandas as pd
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
#set the backgroung style sheet
sns.set_style("whitegrid")
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.offline as py
from plotly.graph_objs import Scatter, Layout
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.figure_factory as ff
import joblib
from donnees import display_data,display_stats
def load_data():
    column_names = ["ID", "Age", "Gender", "Education", "Country", "Ethnicity",
                    "Nscore", "Escore", "Oscore", "Ascore", "Cscore",
                    "Impulsive", "SS",
                    "Alcohol", "Amphet", "Amyl", "Benzos", "Caff",
                    "Cannabis", "Choc", "Coke", "Crack", "Ecstasy",
                    "Heroin", "Ketamine", "Legalh", "LSD", "Meth",
                    "Mushrooms", "Nicotine", "Semer", "VSA"]
    # Chargement des données
    data = pd.read_csv('C:/Users/user/OneDrive - De Vinci/Desktop/Semestre7/python for data/Projet/drug+consumption+quantified/drug_consumption.data', header=None, names=column_names)
    # Mapping for each column
    age_map = {-0.95197: "18-24", -0.07854: "25-34", 0.49788: "35-44", 1.09449: "45-54", 1.82213: "55-64", 2.59171: "65+"}
    gender_map = {0.48246: "Female", -0.48246: "Male"}
    education_map = {-2.43591: "Left school before 16 years", -1.73790: "Left school at 16 years", -1.43719: "Left school at 17 years", -1.22751: "Left school at 18 years", -0.61113: "Some college or university, no certificate or degree", -0.05921: "Professional certificate/ diploma", 0.45468: "University degree", 1.16365: "Masters degree", 1.98437: "Doctorate degree"}
    country_map = {-0.09765: "Australia", 0.24923: "Canada", -0.46841: "New Zealand", -0.28519: "Other", 0.21128: "Republic of Ireland", 0.96082: "UK", -0.57009: "USA"}
    ethnicity_map = {-0.50212: "Asian", -1.10702: "Black", 1.90725: "Mixed-Black/Asian", 0.12600: "Mixed-White/Asian", -0.22166: "Mixed-White/Black", 0.11440: "Other", -0.31685: "White"}
    nscore_map = {-3.46436: 12, -3.15735: 13, -2.75696: 14, -2.52197: 15, -2.42317: 16, -2.34360: 17, -2.21844: 18, -2.05048: 19, -1.86962: 20, -1.69163: 21, -1.55078: 22, -1.43907: 23, -1.32828: 24, -1.19430: 25, -1.05308: 26, -0.92104: 27, -0.79151: 28, -0.67825: 29, -0.58016: 30, -0.46725: 31, -0.34799: 32, -0.24649: 33, -0.14882: 34, -0.05188: 35, 0.04257: 36, 0.13606: 37, 0.22393: 38, 0.31287: 39, 0.41667: 40, 0.52135: 41, 0.62967: 42, 0.73545: 43, 0.82562: 44, 0.91093: 45, 1.02119: 46, 1.13281: 47, 1.23461: 48, 1.37297: 49, 1.49158: 50, 1.60383: 51, 1.72012: 52, 1.83990: 53, 1.98437: 54, 2.12700: 55, 2.28554: 56, 2.46262: 57, 2.61139: 58, 2.82196: 59, 3.27393: 60}
    escore_map = {-3.27393: 16, -3.00537: 18, -2.72827: 19, -2.53830: 20, -2.44904: 21, -2.32338: 22, -2.21069: 23, -2.11437: 24, -2.03972: 25, -1.92173: 26, -1.76250: 27, -1.63340: 28, -1.50796: 29, -1.37639: 30, -1.23177: 31, -1.09207: 32, -0.94779: 33, -0.80615: 34, -0.69509: 35, -0.57545: 36, -0.43999: 37, -0.30033: 38, -0.15487: 39, 0.00332: 40, 0.16767: 41, 0.32197: 42, 0.47617: 43, 0.63779: 44, 0.80523: 45, 0.96248: 46, 1.11406: 47, 1.28610: 48, 1.45421: 49, 1.58487: 50, 1.74091: 51, 1.93886: 52, 2.12700: 53, 2.32338: 54, 2.57309: 55, 2.85950: 56, 3.00537: 58, 3.27393: 59}
    oscore_mapping = {v[1]: v[0] for v in [(24, -3.27393), (26, -2.85950), (28, -2.63199), (29, -2.39883), (30, -2.21069), (31, -2.09015), (32, -1.97495), (33, -1.82919), (34, -1.68062), (35, -1.55521), (36, -1.42424), (37, -1.27553), (38, -1.11902), (39, -0.97631), (40, -0.84732), (41, -0.71727), (42, -0.58331), (43, -0.45174), (44, -0.31776), (45, -0.17779), (46, -0.01928), (47, 0.14143), (48, 0.29338), (49, 0.44585), (50, 0.58331), (51, 0.72330), (52, 0.88309), (53, 1.06238), (54, 1.24033), (55, 1.43533), (56, 1.65653), (57, 1.88511), (58, 2.15324), (59, 2.44904), (60, 2.90161)]}
    cscore_mapping = {v[1]: v[0] for v in [(17, -3.46436), (19, -3.15735), (20, -2.90161), (21, -2.72827), (22, -2.57309), (23, -2.42317), (24, -2.30408), (25, -2.18109), (26, -2.04506), (27, -1.92173), (28, -1.78169), (29, -1.64101), (30, -1.51840), (31, -1.38502), (32, -1.25773), (33, -1.13788), (34, -1.01450), (35, -0.89891), (36, -0.78155), (37, -0.65253), (38, -0.52745), (39, -0.40581), (40, -0.27607), (41, -0.14277), (42, -0.00665), (43, 0.12331), (44, 0.25953), (45, 0.41594), (46, 0.58489), (47, 0.7583), (48, 0.93949), (49, 1.13407), (50, 1.30612), (51, 1.46191), (52, 1.63088), (53, 1.81175), (54, 2.04506), (55, 2.33337), (56, 2.63199), (57, 3.00537), (59, 3.46436)]}
    ascore_mapping = {-3.46436: 12, -3.15735: 16, -3.00537: 18, -2.90161: 23, -2.78793: 24, -2.70172: 25, -2.53830: 26, -2.35413: 27, -2.21844: 28, -2.07848: 29, -1.92595: 30, -1.77200: 31, -1.62090: 32, -1.47955: 33, -1.34289: 34, -1.21213: 35, -1.07533: 36, -0.91699: 37, -0.76096: 38, -0.60633: 39, -0.45321: 40, -0.30172: 41, -0.15487: 42, -0.01729: 43, 0.13136: 44, 0.28783: 45, 0.43852: 46, 0.59042: 47, 0.76096: 48, 0.94156: 49, 1.11406: 50, 1.28610: 51, 1.45039: 52, 1.61108: 53, 1.81866: 54, 2.03972: 55, 2.23427: 56, 2.46262: 57, 2.75696: 58, 3.15735: 59, 3.46436: 60}
    ss_mapping = {-2.07848: 3.77, -1.54858: 4.62, -1.18084: 7.00, -0.84637: 8.97, -0.52593: 11.19, -0.21575: 11.83, 0.07987: 11.62, 0.40148: 13.21, 0.76540: 11.19, 1.22470: 11.14, 1.92173: 5.46}
    impulsive_mapping = {-2.55524: 1.06, -1.37983: 14.64, -0.71126: 16.29, -0.21712: 18.83, 0.19268: 13.63, 0.52975: 11.46, 0.88113: 10.34, 1.29221: 7.85, 1.86203: 5.52, 2.90161: 0.37}
    alcohol_mapping, amphet_mapping, amyl_mapping, benzos_mapping = {"CL0": 1.80, "CL1": 1.80, "CL2": 3.61, "CL3": 10.50, "CL4": 15.23, "CL5": 40.27, "CL6": 26.79}, {"CL0": 51.78, "CL1": 12.20, "CL2": 12.89, "CL3": 10.50, "CL4": 3.98, "CL5": 3.24, "CL6": 5.41}, {"CL0": 69.23, "CL1": 11.14, "CL2": 12.57, "CL3": 4.88, "CL4": 1.27, "CL5": 0.74, "CL6": 0.16}, {"CL0": 53.05, "CL1": 6.15, "CL2": 12.41, "CL3": 12.52, "CL4": 6.37, "CL5": 4.46, "CL6": 5.04}
    ss_mapping = {-2.07848: 3.77, -1.54858: 4.62, -1.18084: 7.00, -0.84637: 8.97, -0.52593: 11.19, -0.21575: 11.83, 0.07987: 11.62, 0.40148: 13.21, 0.76540: 11.19, 1.22470: 11.14, 1.92173: 5.46}
    caff_mapping, cannabis_mapping, choc_mapping, coke_mapping = {"CL0": 1.43, "CL1": 0.53, "CL2": 1.27, "CL3": 3.18, "CL4": 5.62, "CL5": 14.48, "CL6": 73.47}, {"CL0": 21.91, "CL1": 10.98, "CL2": 14.11, "CL3": 11.19, "CL4": 7.43, "CL5": 9.81, "CL6": 24.56}, {"CL0": 1.70, "CL1": 0.16, "CL2": 0.53, "CL3": 2.86, "CL4": 15.70, "CL5": 36.23, "CL6": 42.81}, {"CL0": 55.07, "CL1": 8.49, "CL2": 14.32, "CL3": 13.69, "CL4": 5.25, "CL5": 2.18, "CL6": 1.01}
    crack_mapping, ecstasy_mapping, heroin_mapping, ketamine_mapping = {"CL0": 86.31, "CL1": 3.55, "CL2": 5.94, "CL3": 3.13, "CL4": 0.48, "CL5": 0.48, "CL6": 0.11}, {"CL0": 54.16, "CL1": 5.99, "CL2": 12.41, "CL3": 14.69, "CL4": 8.28, "CL5": 3.34, "CL6": 1.11}, {"CL0": 85.15, "CL1": 3.61, "CL2": 4.99, "CL3": 3.45, "CL4": 1.27, "CL5": 0.85, "CL6": 0.69}, {"CL0": 79.05, "CL1": 2.39, "CL2": 7.53, "CL3": 6.84, "CL4": 2.23, "CL5": 1.75, "CL6": 0.21}
    legalh_mapping, lsd_mapping, meth_mapping, mushrooms_mapping = {"CL0": 58.04, "CL1": 1.54, "CL2": 10.50, "CL3": 17.14, "CL4": 5.84, "CL5": 3.40, "CL6": 3.55}, {"CL0": 56.71, "CL1": 13.74, "CL2": 9.39, "CL3": 11.35, "CL4": 5.15, "CL5": 2.97, "CL6": 0.69}, {"CL0": 75.81, "CL1": 2.07, "CL2": 5.15, "CL3": 7.90, "CL4": 2.65, "CL5": 2.55, "CL6": 3.87}, {"CL0": 52.10, "CL1": 11.09, "CL2": 13.79, "CL3": 14.59, "CL4": 6.10, "CL5": 2.12, "CL6": 0.21}
    nicotine_mapping, semer_mapping, vsa_mapping = {"CL0": 22.71, "CL1": 10.24, "CL2": 10.82, "CL3": 9.81, "CL4": 5.73, "CL5": 8.33, "CL6": 32.36}, {"CL0": 99.58, "CL1": 0.11, "CL2": 0.16, "CL3": 0.11, "CL4": 0.05, "CL5": 0.00, "CL6": 0.00}, {"CL0": 77.19, "CL1": 10.61, "CL2": 7.16, "CL3": 3.24, "CL4": 0.69, "CL5": 0.74, "CL6": 0.37}


    # Apply the mappings
    data["Age"] = data["Age"].map(age_map)
    data["Gender"] = data["Gender"].map(gender_map)
    data["Education"] = data["Education"].map(education_map)
    data["Country"] = data["Country"].map(country_map)
    data["Ethnicity"] = data["Ethnicity"].map(ethnicity_map)
    data["Nscore"] = data["Nscore"].map(nscore_map)
    data['Escore'] = data['Escore'].map(escore_map)
    data["Oscore"] = data["Oscore"].map(oscore_mapping)
    data["Cscore"]=data["Cscore"].map(cscore_mapping)
    data["Ascore"]=data["Ascore"].map(ascore_mapping)
    data['Impulsive'] = data['Impulsive'].map(impulsive_mapping)
    data['SS'] = data['SS'].map(ss_mapping)
    #data['SS']= data['SS'].map(ss_mapping)
    data['Alcohol'] = data['Alcohol'].map(alcohol_mapping)
    data['Amphet'] = data['Amphet'].map(amphet_mapping)
    data['Amyl'] = data['Amyl'].map(amyl_mapping)
    data['Benzos'] = data['Benzos'].map(benzos_mapping)
    data['Caff'] = data['Caff'].map(caff_mapping)
    data['Cannabis'] = data['Cannabis'].map(cannabis_mapping)
    data['Choc'] = data['Choc'].map(choc_mapping)
    data['Coke'] = data['Coke'].map(coke_mapping)
    data['Crack'] = data['Crack'].map(crack_mapping)
    data['Ecstasy'] = data['Ecstasy'].map(ecstasy_mapping)
    data['Heroin'] = data['Heroin'].map(heroin_mapping)
    data['Ketamine'] = data['Ketamine'].map(ketamine_mapping)
    data['Legalh'] = data['Legalh'].map(legalh_mapping)
    data['LSD'] = data['LSD'].map(lsd_mapping)
    data['Meth'] = data['Meth'].map(meth_mapping)
    data['Mushrooms'] = data['Mushrooms'].map(mushrooms_mapping)
    data['Nicotine'] = data['Nicotine'].map(nicotine_mapping)
    data['Semer'] = data['Semer'].map(semer_mapping)
    data['VSA'] = data['VSA'].map(vsa_mapping)
    data = data.sort_values(by=['Age', 'Gender','Country','Education'])
    # List of drug columns in the new dataset
    new_drug_columns = ['Alcohol', 'Amphet', 'Amyl', 'Benzos', 'Caff', 'Cannabis', 'Choc', 'Coke',
                    'Crack', 'Ecstasy', 'Heroin', 'Ketamine', 'Legalh', 'LSD', 'Meth',
                    'Mushrooms', 'Nicotine', 'Semer', 'VSA']

    # List of personality traits columns
    personality_traits = ['Nscore', 'Escore', 'Oscore', 'Ascore', 'Cscore', 'Impulsive', 'SS']
    return data

if __name__ == "__main__":
    data = load_data()
    display_data(data)
    display_stats(data)