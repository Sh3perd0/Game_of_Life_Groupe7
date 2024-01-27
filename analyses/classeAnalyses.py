import matplotlib.pyplot as plt

class NewCourbe:
    def __init__(self, titre, X ,Y, ax):
        # option du graphique
        ax.plot(X, Y)
        ax.set_title(titre)
        ax.legend()