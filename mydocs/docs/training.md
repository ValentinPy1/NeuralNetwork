# Documentation du script Trainer
Le script trainer permet de charger un modèle préalablement sauvegardé et de l'entraîner sur un jeu de données. Il prend en compte divers paramètres et options pour personnaliser le processus d'entraînement.

## Utilisation

Usage: ./trainer <model> <dataset> <epochs>
    -s <split> (default: 0.9)
        split the dataset into a training set and a validation set
    -b <batch_size> (default: 64)
        set the batch size for training
    -l <learning_rate> (default: 0.001)
        set the learning rate for training
    -e <early_stop> (default: 0)
        stop training if test accuracy does not improve for <early_stop> epochs
    -v (verbose)
        print loss and accuracy after each epoch
    -p (progress bar)
        show progression during an epoch

## Fonctions

`main(argv) -> None`

La fonction principale du script qui prend les arguments en ligne de commande et lance le processus d'entraînement.

Paramètres
argv (list): Liste des arguments de la ligne de commande.

Exemple

./trainer my_model.pkl my_dataset.pkl 50 -s 0.8 -b 32 -l 0.01 -e 5 -v -p

## Paramètres

model (str): Le chemin vers le fichier contenant le modèle à charger et entraîner.
dataset (str): Le chemin vers le fichier contenant le jeu de données sur lequel entraîner le modèle.
epochs (int): Le nombre d'époques pour l'entraînement.

## Options

-s <split>: Spécifie la proportion du jeu de données à utiliser pour l'ensemble d'entraînement (par défaut: 0.9).
-b <batch_size>: Définit la taille du lot (batch size) à utiliser pour l'entraînement (par défaut: 64).
-l <learning_rate>: Définit le taux d'apprentissage pour l'entraînement (par défaut: 0.001).
-e <early_stop>: Arrête l'entraînement si la précision sur le jeu de test ne s'améliore pas pendant <early_stop> époques (par défaut: 0).
-v: Active l'affichage détaillé de la perte et de la précision après chaque époque.
-p: Active la barre de progression pour suivre la progression pendant une époque.

