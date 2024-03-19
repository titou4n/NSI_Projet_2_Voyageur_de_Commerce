def recup_graph():
  '''
  Fonction pour recupérer le graphe
  Complexité mathématique :  O(n²)
  '''
  graph = {
      "Paris": {
          "Lille": 204,
          "Strasbourg": 398,
          "Clermont-F": 346,
          "Marseille": 660,
          "Rennes": 307
      },
      "Lille": {
          "Paris": 204,
          "Strasbourg": 410,
          "Clermont-F": 542,
          "Marseille": 835,
          "Rennes": 443
      },
      "Strasbourg": {
          "Paris": 398,
          "Lille": 410,
          "Clermont-F": 471,
          "Marseille": 615,
          "Rennes": 700
      },
      "Clermont-F": {
          "Paris": 346,
          "Lille": 542,
          "Strasbourg": 471,
          "Marseille": 330,
          "Rennes": 447
      },
      "Marseille": {
          "Paris": 660,
          "Lille": 835,
          "Strasbourg": 615,
          "Clermont-F": 330,
          "Rennes": 766
      },
      "Rennes": {
          "Paris": 307,
          "Lille": 443,
          "Strasbourg": 700,
          "Clermont-F": 447,
          "Marseille": 766
      }
  }
  return graph