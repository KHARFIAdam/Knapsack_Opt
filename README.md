# Solveur du Problème du Sac à Dos 🚀

Ce dépôt contient une solution au classique **Problème du Sac à Dos** en utilisant diverses techniques d'optimisation, notamment l'**Algorithme Génétique (GA)**, la **Recherche Tabou**, et la **Programmation Linéaire** avec un solveur. L'objectif de ce projet est de résoudre efficacement le **problème du sac à dos 0/1** avec différentes approches et de comparer leurs performances et leur précision.

## Présentation du Problème 🎒

Le **Problème du Sac à Dos** consiste à sélectionner un sous-ensemble d'objets ayant des poids et des valeurs donnés afin de maximiser la valeur totale sans dépasser une limite de poids. Ce problème d'optimisation combinatoire est couramment utilisé dans des domaines tels que l’allocation des ressources, la logistique, et bien plus encore.

### Définition du Problème :
- Vous disposez de `n` objets, chacun avec un poids et une valeur spécifiques.
- Un sac à dos peut supporter un poids maximal `W`.
- L’objectif est de trouver le sous-ensemble d’objets qui maximise la valeur totale sans dépasser la limite de poids.

Formellement :

$$ \text{Maximiser} \quad \sum_{i=1}^{n} v_i x_i $$  
$$ \text{Sous contrainte} \quad \sum_{i=1}^{n} w_i x_i \leq W $$  

Où :
- $$ \(v_i\) $$ = valeur de l'objet \(i\)
- \(w_i\) = poids de l'objet \(i\)
- \(x_i\) = variable binaire (1 si l'objet \(i\) est sélectionné, 0 sinon)
- \(W\) = capacité maximale du sac à dos

---

## Techniques d'Optimisation Utilisées 🧠

Ce projet applique trois méthodes (dont 2 métaheuristiques) distinctes pour résoudre le problème du sac à dos :

### 1. **Algorithme Génétique (GA)** 🧬

Les algorithmes génétiques sont inspirés de la sélection naturelle et utilisent une approche basée sur une population. Dans cette implémentation :
- Les solutions sont encodées sous forme de chaînes binaires.
- Les parents sont sélectionnés en fonction de leur valeur de fitness (valeur totale), et les descendants sont créés par croisement et mutation.
- Les meilleurs individus sont sélectionnés pour la génération suivante.

### 2. **Recherche Tabou** 🔄

La recherche tabou est un algorithme de recherche locale qui améliore la performance des méthodes de recherche basiques en utilisant des structures de mémoire (listes taboues) pour éviter de revisiter les solutions précédentes. L’algorithme :
- Démarre avec une solution initiale et explore le voisinage de manière itérative.
- Évite les cycles en gardant en mémoire les derniers déplacements effectués.

### 3. **Programmation Linéaire avec un Solveur** 📊

La programmation linéaire (PL) permet de résoudre le problème sous forme d’un ensemble d’équations et d’inégalités linéaires. Cette méthode utilise un solveur pour obtenir une solution optimale en :
- Définissant les variables de décision, la fonction objectif et les contraintes.
- Utilisant la **méthode du Simplex** ou un autre solveur PL pour trouver l’optimum efficacement.

---

## Installation 🔧

Pour exécuter ce projet en local, suivez les étapes ci-dessous :

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/KHARFIAdam/Knapsack_Opt
   cd Knapsack_Opt