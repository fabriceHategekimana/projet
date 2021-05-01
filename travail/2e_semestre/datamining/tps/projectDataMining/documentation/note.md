# Projet de datamining

## But:
Pouvoir reconnaître et classifier quatre molécules particulières (ou des heavy atoms, je ne sais plus)

## fichiers:
- **QM9.txt**:
- **properties_QM9.npz**: contient les properties des molécules
- utils.py
- smiles-rdkit.ipynb

## Type de data
|      |
|------|
| LogP |
| RBN  |
| MW   |
| RN   |

## Format de données

**SMILE (=simplified molecular_input line entry system):**  
Format qui repésente les molécules sous forme de chaine de caractère (forma ASCII)

Hot je ne sais plus quoi:
Format util pour l'annalyse.


## Évaluation
- compréhention du problème
- modélisation du problème 
- Approche: modèles testés
- Modèle final sélectionné
- Comprendre en profondeur les algos utilisés

## Fonctions utiles
smile_to_hot()
load_data()

## Point d'ombre:
cross-validation
basline algorithme

## Final submission:
Name1_Name2_DM_project.
- scripts
- dataset

## À chercher
RDkit

### Représentation smile
- Capital letter
- Hydrogen ignored
- single bond ignored
- double =
- triple #
- quadruple $
- Aromacity ?
