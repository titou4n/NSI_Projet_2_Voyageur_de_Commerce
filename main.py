from generate_path import generate_all_paths
from recup_graph import recup_graph
import time


def choice_start_city():
  '''
  Fonction pour définir la ville de départ
  Complexité mathématique :  O(1)
  '''
  print("\n1.Paris")
  print("2.Strasbourg")
  print("3.Clermont-F")
  print("4.Lille")
  print("5.Marseille")
  print("6.Rennes")
  start_city = str(input("Choisir une ville de départ : "))
  if start_city == "1":
    return "Paris"
  if start_city == "2":
    return "Strasbourg"
  if start_city == "3":
    return "Clermont-F"
  if start_city == "4":
    return "Lille"
  if start_city == "5":
    return "Marseille"
  if start_city == "6":
    return "Rennes"
  else:
    print("Choix non valide")
    return choice_start_city()


def distance_between_cities(city_1, city_2, graph):
  '''
  Calcule la distance entre deux villes.
  Arguments:
      ville_1 (str): Nom de la première ville.
      ville_2 (str): Nom de la deuxième ville.
      graph (dict): Dictionnaire des distances entre les villes.
  Return:
      float: La distance entre les deux villes, ou None si la distance n'est pas trouvée.
  Complexité mathématique :  O(1)
  '''
  if city_1 in graph and city_2 in graph[city_1]:
    return graph[city_1][city_2]
  elif city_2 in graph and city_1 in graph[city_2]:
    return graph[city_2][city_1]
  else:
    return None


def verif_path(path, graph):
  '''
  Fonction pour vérifier si un chemin est valide.
  Argument:
      path (list) : liste du chemin.
      graph (dict): Dictionnaire des distances entre les villes.
  Return:
      True  : si le chemin est valide
      False : si le chemin n'est pas valide
  Complexité mathématique :  O(n)
  '''
  if len(path) != len(graph) + 1 or path[0] != path[-1]:
    return False
  else:
    lst_city_use = []
    for i in range(len(path) - 1):
      if path[i] in lst_city_use:
        return False
      else:
        lst_city_use.append(path[i])
    return True


def calculate_distance_path(path, graph):
  '''
  Fonction pour calculer la distance d'un chemin.
  Argument:
      path (list) : liste du chemin.
      graph (dict): Dictionnaire des distances entre les villes.
  Return:
      int : la distance d'un chemin
  Complexité mathématique :  O(n)
  '''
  distance_total = 0
  for i in range(len(path) - 1):
    distance = distance_between_cities(path[i], path[i + 1], graph)
    distance_total += distance
  return distance_total


def main():
  '''
  Fonction pour définir le meilleur tour ou chemin fermé
  En km
  En choisissant une ville de départ
  Complexité mathématique :  O(n!)
  '''
  #____________________Initialisation____________________#
  start_city = choice_start_city()  # O(1)
  start_time = time.time()  # O(1)
  graph = recup_graph() # O(n²)
  all_paths = generate_all_paths(graph=graph, start_city=start_city) # O(n!)
  if len(all_paths) == 0:  # O(n) avec n tout les chemins
    print("Aucun chemin trouvé")
  else:
    #____________________Recuperer_la_moitié_des_chemins_générés____________________#
    paths = all_paths[:len(all_paths) // 2]  # O(n) avec n tout les chemins
    #_____On_initialise_une_distance_et_un_chemin_____#
    distance_shortest_path = calculate_distance_path(
        path=paths[0],
        graph=graph)  # O(n)
    name_shortest_path = paths[0]
    #____________________Parcours_de_tous_les_chemins____________________#
    for path in paths:  # O(n**3)
      # Bouble for donc n * calculate_distance_path(path, graph)
      # Avec verif_path(path, graph) -> O(n)
      # Avec calculate_distance_path(path, graph) -> O(n)
      # Donc O(n*n*n)=O(n**3)
      #__________Verification_du_chemin__________#
      if verif_path(path=path, graph=graph): # O(n)
        #_____Calcul_la_distance_du_chemin_____#
        distance = calculate_distance_path(path=path,
                                           graph=graph)  # O(n)
        if distance_shortest_path > distance:
          distance_shortest_path = distance
          name_shortest_path = path
    #____________________Affichage_du_chemin_avec_une distance_acceptable____________________#
    print(f"\nLe chemin le plus court ou avec une distance accepetable, en partant de {start_city} est :")
    for i in range(len(name_shortest_path)):
      print(f" -> {name_shortest_path[i]}", end="")
    print(f"\nAvec une distance de {distance_shortest_path} km")
    end_time = time.time()
    print(f"\nTemps d'execution : {end_time - start_time} secondes")


if __name__ == "__main__":
  while True:
    main()
