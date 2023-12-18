# Documentation de la Configuration pour lancer un reseau de neurones

## Configuration

Dans un fichier de configuration en yml, on peut définir les paramètres suivants:
    - le name
    - le layer
    - le loss

### Exemple de fichier de configuration

```yml
model:
    name: 'my_model'
    layers:
        - Input: [897]
        - Dense: 200
        - Act: 'tanh'
        - Dropout: 0.5
        - Dense: 100
        - Act: 'tanh'
        - Dense: 4
        - Act: 'sigmoid'
    loss: 'binary_crossentropy'
```

### Explication du fichier de configuration

#### model

Le model est un dictionnaire qui contient les paramètres suivants:
    - name: le nom du model
    - layers: la liste des layers
    - loss: la fonction de loss

#### layers

La liste des layers est une liste de dictionnaires qui contient les paramètres suivants:
    - Input: la taille de l'input
    - Dense: la taille de la couche dense
    - Act: la fonction d'activation
    - Dropout: le pourcentage de dropout

#### loss

La fonction de loss est une chaîne de caractères qui contient le nom de la fonction de loss.

## Utilisation

`./generator <yaml_config>`
