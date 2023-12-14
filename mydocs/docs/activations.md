# Documentation des Layers avec Activation Functions

## Activation

La classe `Activation` est une couche d'activation générique qui applique une fonction d'activation pendant la propagation avant et sa dérivée pendant la rétropropagation.

### Méthodes

#### `__init__(self, activation, activation_prime) -> None`

Initialise la couche d'activation avec les fonctions d'activation et leurs dérivées.

- `activation`: Fonction d'activation à appliquer.
- `activation_prime`: Dérivée de la fonction d'activation.

#### `forward(self, input) -> ndarray`

Calcule la propagation avant de la couche d'activation en appliquant la fonction d'activation.

#### `backward(self, output_gradient, learning_rate) -> ndarray`

Calcule la rétropropagation de la couche d'activation en multipliant le gradient de sortie par la dérivée de la fonction d'activation.

## Tanh

La classe `Tanh` est une couche d'activation qui applique la fonction tangente hyperbolique (tanh).

### Méthodes

#### `__init__(self) -> None`

Initialise la couche Tanh en utilisant la fonction `tanh` et sa dérivée.

## Sigmoid

La classe `Sigmoid` est une couche d'activation qui applique la fonction sigmoïde.

### Méthodes

#### `__init__(self) -> None`

Initialise la couche Sigmoid en utilisant la fonction sigmoïde et sa dérivée.

## ReLU

La classe `ReLU` est une couche d'activation qui applique la fonction Rectified Linear Unit (ReLU).

### Méthodes

#### `__init__(self) -> None`

Initialise la couche ReLU en utilisant la fonction ReLU et sa dérivée.
