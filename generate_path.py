def generate_all_paths(graph, start_city, path=[]):
  '''
  Fonction pour génerer tous les chemins possibles.
  Argument:
      graph (dict): Dictionnaire des distances entre les villes.
      start_city (str): Nom de la ville de départ.
      path (list): Liste des villes visitées jusqu'à présent.
  Return:
      paths (list): Liste des chemins possibles.
  Complexité mathématique :  O(n!)
  Chaque ville est visitée une fois dans chaque chemin généré.
  Dans le pire des cas, la fonction doit générer tous les chemins possibles,
  Ce qui donne une complexité de O(n!), avec n est le nombre de villes dans le graphe
  Pour chaque ville,
  il y a n - 1 choix possibles pour la ville suivante,
  puis n - 2 pour la suivante, etc
  et ainsi de suite jusqu'à ce que toutes les villes soient visitées.
  '''
  path = path + [start_city] # met à jour le chemin parcouru jusqu'à présent en ajoutant la ville de départ à la fin
  if len(path) == len(graph): # Vérifie si toutes les villes ont été visitées en comparant la longueur du chemin actuel avec le nombre total de villes dans le graphe
    if path[0] in graph[start_city]: # Vérifie si la ville de départ est reliée à la première ville dans le chemin actuel
      return [path + [path[0]]] # retourne le chemin complet
    else: # si la ville de départ n'est pas reliée à la première ville dans le chemin actuel, cela signifie qu'il n'y a pas de chemin complet
      return [] # retourne une liste vide, indiquant qu'aucun chemin complet n'a été trouvé
  paths = [] # Initialise une liste vide pour stocker les chemins possibles
  for next_city in graph[start_city]: # Boucle à travers toutes les villes accessibles à partir de la ville de départ
    if next_city not in path: # Vérifie si la ville suivante n'a pas encore été visitée
      new_paths = generate_all_paths(graph, next_city, path) # Appelle récursivement la fonction generate_all_paths pour explorer les chemins possibles à partir de la prochaine ville.
      for new_path in new_paths: # Boucle à travers les chemins possibles obtenus à partir de la ville suivante
        paths.append(new_path) # Ajoute chaque nouveau chemin à la liste des chemins possibles
  return paths # Retourne tous les chemins possibles à partir de la ville de départ actuelle
