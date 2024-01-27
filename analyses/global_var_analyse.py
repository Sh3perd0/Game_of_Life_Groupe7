

running = True
playing = True

time = 0

Day =  []
masse_moyenne = []
energie_moyenne = []
vitesse_moyenne = []
bob_time_life = []
nb_bob = []
perception_moyen = []

nb_descendant = 0
nb_food_eat = 0
nb_canibalisme = 0


titres = ["masse moyenne en fonction du temps","energie en fonction du temps", "vitesse moyenne en fonction du temps","perception moyenne", "nombre de bob en fonction du temps"]
Y_graphiques = [masse_moyenne,energie_moyenne,perception_moyen, vitesse_moyenne,nb_bob]

def newValue(time, m_masse,m_energie,m_speed,pop_bob,perception):
    Day.append(time)
    masse_moyenne.append(m_masse)
    energie_moyenne.append(m_energie)
    vitesse_moyenne.append(m_speed)
    nb_bob.append(pop_bob)
    perception_moyen.append(perception)

