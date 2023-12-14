# Documentation du Module Neural Network

## Network

La classe `Network` représente un réseau de neurones composé de différentes couches.

### Méthodes

#### `__init__(self, layers) -> None`

Initialise le réseau avec une liste de couches.

#### `forward(self, input) -> ndarray`

Calcule la propagation avant du réseau en passant l'entrée à travers toutes les couches.

#### `backward(self, output_error, learning_rate) -> ndarray`

Effectue la rétropropagation à travers le réseau en ajustant les paramètres des couches.

## Model

La classe `Model` encapsule un réseau de neurones, une fonction de perte, et fournit des méthodes pour l'entraînement et l'évaluation.

### Méthodes

#### `__init__(self, network, loss, x_test, y_test) -> None`

Initialise le modèle avec un réseau, une fonction de perte, et des données de test.

#### `train(self, x_train, y_train, epochs, batch_size=64, learning_rate=0.001, early_stop=0, verbose=True, progress_bar=False) -> None`

Entraîne le modèle sur les données d'entraînement pour un nombre d'époques donné.

#### `evaluate(self, x_test, y_test) -> None`

Évalue le modèle sur des données de test en calculant la perte et la précision.

#### `predict_one(self, x) -> ndarray`

Effectue une prédiction pour une seule entrée.

#### `predict(self, x_test) -> ndarray`

Effectue des prédictions pour un ensemble de données.

#### `test_accuracy(self, x_test, y_test) -> float`

Calcule la précision du modèle sur un ensemble de données de test.

#### `save(self, path) -> None`

Sauvegarde le modèle dans un fichier spécifié par le chemin.

#### `load(path) -> Model`

Charge un modèle à partir d'un fichier spécifié par le chemin (méthode statique).
