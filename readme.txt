Création d'un aglorithme génétique pour projet en interne chez Adludio. 

- 1Dim
la fonction "fitness" à minimiser est en réalité la distance entre deux points dans l'espace. 
Ces "points" correspondent à la position d'un individu. 
Chaque individu est codé sous forme de bitcode. ex : [1,0,1,0,1,0,1,1,1,0]
On divise donc le vecteur et on converti celui ci en décimal afin d'obtenir des coordonnées x et y pour cet individu. 

- XDim
On retrouve le même fonctionnement mais cette fois, on coupe le vecteurs en X (multiple de 2) et on calcule la distance entre différents critères. 
