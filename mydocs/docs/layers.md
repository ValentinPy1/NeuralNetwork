# Documentation des Layers

## Layer

La classe de base pour toutes les couches du réseau.

### Méthodes

#### `__init__(self) -> None`

Initialise les attributs `input` et `output`.

#### `forward(self, input) -> ndarray`

Calcule la propagation avant (forward) de la couche. Cette méthode est abstraite.

#### `backward(self, output_gradient, learning_rate) -> ndarray`

Calcule la rétropropagation (backward) de la couche. Cette méthode est abstraite.

## Dense

Une couche Dense (complètement connectée) du réseau.

### Méthodes

#### `__init__(self, input_size, output_size, beta1=0.9, beta2=0.999, epsilon=1e-8) -> None`

Initialise les poids, les biais et les paramètres d'optimisation de la couche Dense.

#### `forward(self, input) -> ndarray`

Calcule la propagation avant de la couche Dense.

#### `backward(self, output_gradient, learning_rate) -> ndarray`

Calcule la rétropropagation de la couche Dense.

## Dropout

Une couche de dropout pour régulariser le réseau.

### Méthodes

#### `__init__(self, drop_rate) -> None`

Initialise la couche de dropout avec un taux de dropout donné.

#### `forward(self, input) -> ndarray`

Calcule la propagation avant de la couche de dropout.

#### `backward(self, output_gradient, learning_rate) -> ndarray`

Calcule la rétropropagation de la couche de dropout.
