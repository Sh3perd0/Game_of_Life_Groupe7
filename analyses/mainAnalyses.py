
import numpy as np
import analyses.global_var_analyse as gva
import matplotlib.pyplot as plt
from constant.settings import *
from analyses.classeAnalyses import NewCourbe

def show_analyses():
    nb_figure = len(gva.Y_graphiques)

    # Création de la figure et des sous-graphiques
    figure, axes = plt.subplots(nb_figure, 1, sharex=True)

    #création des différentes courbes
    for i in range(nb_figure):
        NewCourbe(gva.titres[i],gva.Day,gva.Y_graphiques[i],axes[i])

    #calcul de la moyenne de vie des bobs
    moyenne_de_vie = 0
    for k in range(len(gva.bob_time_life)):
        moyenne_de_vie += gva.bob_time_life[k]
    moyenne_de_vie = moyenne_de_vie/len(gva.bob_time_life)

    print("moyenne de vie des bobs en tick : "+str(moyenne_de_vie)+" et en jour : "+str(moyenne_de_vie/TICK))
    print("nombre de descendant total : "+str(gva.nb_descendant))
    print("nombre de nourriture mangé : "+str(gva.nb_food_eat))
    print("cas de cannibalisme : "+str(gva.nb_canibalisme))
    plt.tight_layout()
    plt.show()