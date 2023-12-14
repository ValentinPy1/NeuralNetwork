# Documentation des Fonctions de Perte (Loss) en Machine Learning

## Loss

La classe de base `Loss` représente une fonction de perte générique utilisée dans l'apprentissage automatique.

### Méthodes

#### `loss(self, y_true, y_pred) -> float`

Calcule la perte entre les valeurs réelles (`y_true`) et les valeurs prédites (`y_pred`).

#### `gradient(self, y_true, y_pred) -> ndarray`

Calcule le gradient de la fonction de perte par rapport aux prédictions (`y_pred`).

## MeanSquaredError

La classe `MeanSquaredError` est une fonction de perte qui mesure la moyenne des carrés des erreurs entre les valeurs réelles et les valeurs prédites.

### Méthodes

#### `loss(self, y_true, y_pred) -> float`

Calcule la perte de l'erreur quadratique moyenne entre les valeurs réelles et les valeurs prédites.

#### `gradient(self, y_true, y_pred) -> ndarray`

Calcule le gradient de la fonction de perte Mean Squared Error par rapport aux prédictions.

## BinaryCrossEntropy

La classe `BinaryCrossEntropy` est une fonction de perte utilisée pour les tâches de classification binaire.

### Méthodes

#### `loss(self, y_true, y_pred) -> float`

Calcule la perte de l'entropie croisée binaire entre les valeurs réelles et les valeurs prédites.

#### `gradient(self, y_true, y_pred) -> ndarray`

Calcule le gradient de la fonction de perte Binary Cross Entropy par rapport aux prédictions.
