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
  path = path + [start_city]
  if len(path) == len(graph):
    if path[0] in graph[start_city]:
      return [path + [path[0]]]
    else:
      return []
  paths = []
  for next_city in graph[start_city]:
    if next_city not in path:
      new_paths = generate_all_paths(graph, next_city, path)
      for new_path in new_paths:
        paths.append(new_path)
  return paths