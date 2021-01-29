# Q1 explain the image formation in the eye. What are the differences in focusing between the ordinary cameras and the human eyes?

TODO
vidéo convolution vs correlation
vidéo expliquant le chromacity color diagram
Explain the principles of halftoning.
Recherche sur Radiance, Liminance, Brightness
Slides(18 -24) and slide 33

The image formation in the eye :
La rétine contient 2 types de photorecepteurs:
    -  batonnet (100 millions) distribué dans la rétine (intensité de lumière)
    -  cône (6.5 millions) distribué dans la fovéa (couleur)

Le système visuel humain fonctionne de cette façon:
    1. L'énergie lumineuse est concentrée dans la lentille à l'intérieur du capteur et de la rétine
    2. Le capteur de l'oeil répond à la lumière par une réaction électrochimique qui envoie un signal électrique au cerveau(à travers le nerf optique)
    3. Le cerveau utilise les signaux pour créer des schéma neurologique que nous percevons en tant qu'image.

**Example**
    On regarde un arbre de 15 m à une distance de 100 m, H est la hauteur de l'objet dans la rétine.

**What are the differences in focusing between the ordinary cameras and the human eyes?**
1. La première différence se trouve dans la tentille. Dans le système visuel humain, la lentille est flexible alors que pour la plus part des caméras, la lentille est fixe (cela existe pour les caméras les plus chères mais pas autant que pour l'oeil humain)
2. La deuxième différence se trouve au niveau des élément photo sensibles. Dans l'oeil, il n'y a pas de répartition uniforme mais dans les appareils si (c'est dans une petit zone de fovea pas plus grande que 0.15 mm)
3. La troisèime différence se trouve dans la façon de percevoir la lumière. Le champ d'intensité lumineus de l'oeil peut s'adapter (dans un ordre de 1010). L'intensité perçue par l'oeil (brillance subjective) est un logarithm de l'intensité de la lumière incidente dans l'oeil.

# Q2 HVS. Explain the fundamentals of color vision.  Explain the additive and subtractive color mixings.

Explain the fundamentals of color vision.

Objectively, we can distinguish:
La lumière acromatic (sans couleur): caractérisé par l'intensité de la lumière. cela varie entre noir et blanc avec des nuances de gris
La lumière cromatique (couleur): qui sert à distinguer et percevoir les couleurs

**Cela est caractérisé par 3 grandeurs**
1. **Radiance** c'est la quantité totale d'énergie emmise par une source lumineuse (mesuré en Watt).
2. **Liminance** est une mesuer de la quatité d'énergie qu'un observateur perçois depuis la source lumineuse. on peut considéré cela philtré par l'oeil humain (lumens)
3. **Brightness** est une évaluation subjective de ce qu'est la source de radiation dont nous parlons.

**There are two ways to consider the color vision:**
Il y a deux façon de considérer la vision des couleurs
1. On peut le considéere comme une partie du spectre électromagnétique et depuis la perspective de la percéption par l'oeil humain et l'interpretation par le cerveau humain.
2. On peut le considérer comme une part de la façon dont la couleur est créée en tant que tell par les couleur primaire ou par le mélange des couleur (composition additive/soustractive)

La couleur est la façon dont nos yeux et notre cerveau perçoivent la lumière.
La lumière est une onde et comme tout type d'onde, chaque particule, a une logueur d'onde.
Techniquement, le champ de vision des êtres humains est très étroit comparé au spectre électromagnétique entier

La couleur que nous voyons est basée sur des longueurs d'ondes de la lumière. Aussi, plus il y a de lumière, plus on voit de couleurs. La plus part des coleur sont une combinaison de plusieurs longeurs d'ondes.

exemple du blanc et du prisme de Newton.

La couleur est perçue quand la lumière atteint les cônes de nos yeux.

**3 types de cones**
Chacun des trois type de cônes sont sensibles à des longeurs d'onde de mesure différentes.

L-cones – sensible à  high-wavelength
M-cones – sensible à  medium-wavelength
S-cones – sensible à  short-wavelength

In normal human most of receptors are Red colors(%65)
%65 “Red”(not exact)
%33 “Green”(not exact)
2%  “Blue” (not exact)

Mais dans les caméra digitals on a deux fois plus de récepteur vert que le reste.
La plus grande concentration de récepteurs pour une personne normale se trouve dans la Fovea et pas ailleurs dans la rétine.

Les cônes sont codés dans l'ADN (le dalotnisme est potentiellement d'origine génétique)
Soit la personne n'a pas tout les type de cône soit ceux-ci sont endommagés.

The distribution of cone cells in the fovea of a person with
normal color vision (left) and a colorblind (protanopic) retina.

**Conclusion:**
Il n'y a pas de cône S dans la fovea.
Les daltoniens n'ont pas de cône L

**Explain the additive and subtractive color mixings.**
Additive color mixings:
La combinaison devint plus claire à mesure qu'on ajoute des couleurs.

subtractive color mixings:
La combinaision devient plus sombre à mesure qu'on ajoute des couleurs.

# Q3 HVS. Explain the CMYK model.
C'est pour:
- cyan
- Magenta
- yellow (jaune)
- black (on retient seulement le k pour une raison qu j'ignore)

Contrairement au RGB (red, green, blue) qui servent à afficher/représenter les coureurs sur un écran.
Alors que RGB est une composition additive, Le CMYK est une composition soustractive.
CMYK représente les pigments de couleur alors que le rgb représente la lumière.

**Exemplify the reflection of colors.**
Exemple avec une pomme. un objet blanc et noir.

**Explain the principles of halftoning.**

La couleure noir est un supplément car elle coûte peu à produir et prend moins de temps pour imprimer du papier.

# Q4 HVS. Explain the chromaticity color diagram.
All physiquly existing colors appeared on this normalized x, y plain.

**What is the achievable color gamut?**

**Which factors determine the achievable color gamut for the screens and printers?**

Gamut of the screen is larger than the gamut of the printer . printer can reproduce less color

--------------------------------------------------------------------------------------------------------Chapitre 6
# Q15. Explain the difference between the convolution and correlation. Give examples
and explain the practical usage of both.

**Give examples**
Important : If the filter is symmetric the result of coevolution and correlation will be the
same.

# Q16.Explain the border effects during the computation of 2D convolution. Define the
total size of filtered images. Give examples.
We don’t know the pixel intensity of the borders so we do some padding
operation.
Handling the border effect (for example)
1. Zero padding
2. Periodic extension
3. Symmetrically flip
Zero padding : around the image I create a virtual border( the half of filter-1)
One ligne of image

cropped

Periodic extension : I can create just image repeat it multiply time .
One ligne of image

cropped

Here we see we take the same signal (line) and we repeat it . we can
see our intensity is very small but intensity from the previous period is
very high and if I need to multiply all these values on filter coefficients, I
will have a jump near de edges so as result we have a border effect

near the edges of the image due such kind of the periodical extension . (happens in Fourier
transformations )

1

N

Symmetrically flip :

explication….
M

total size of filtered images : If i compute with all of my border effect
-a

a
Filter size

m× n

M×N
Image size
Resulting image size Sv × Sh
Sv =m+ M −1
Sh=+ N − 1

Exemples :

# Q17. Explain the main properties of convolution. Complexity of convolution in 2D.
1. The Commutative property (general form)
∞

g ( x )=f ( x ) ∗h ( x )=

∞

∑

f ( m ) h ( x − m ) ↔ h ( x ) ∗ f ( x )=

m=− ∞

f (x)

h(x)

g(x)

h(x) g( x)

f ( x −k ) h ( k ) k=x − m
m=x − k
x=− ∞

∑

|

f (x)

2. The associative property

g ( x )=f ( x ) ∗ ( h1 ( x ) ∗ h2 ( x ) ) ↔ ( f ( x ) ∗ h1 ( x ) ) ∗ h2 ( x )
f (x)

h1 ( x )

g(x)

h2 ( x )

f (x)

g(x)
h1 ( x ) ∗ h2 ( x )

f (x)

h2 ( x )

g(x)

h1 ( x )

f (x)

g(x)
h2 ( x ) ∗ h1 ( x )

3. The distributive property

g ( x )=f ( x ) ∗ ( h1 ( x ) +h2 ( x )) =f ( x ) ∗h 1 ( x ) +f ( x ) ∗ h2 ( x )

f (x)

h1 ( x )

g(x)

f (x)

h2 ( x )

g(x)

h1 ( x )+ h2 ( x )

Property 1: Generally if we have the convolution between f(x) and g(x) it means we can
interchange the sense what is the signal, what is the filter -- > Filtering the signal by filter and
filtering the filter by signal.
Property 2 : we have two filter h1 and h2 and our signal f(x). we can convolve one filter with
another filter create a new virtual filter and convolve the signal with h result . otherwise we
can convolve our signal with filter h1 then convolve with the second filter or convolve our
signal with filter h2 then convolve with the first filter.
Remarque: property 2 is true for convolution but its not true for correlation . for correlation if I
replace the order it not the same due to the fact the filter is not flip.
Property 3
In case de correlation For pattern recognition et for classification it is ok but not for edge
detection of filtering (property 1 et 2)
Property

Convolution

Correlation

Commutative

f ∗ h=h ∗ f

Does not hold

Associative

f ∗ ( h1 ∗h 2 )=( f ∗ h1 ) ∗ h2

Does not hold

Distributive

f ∗ ( h1 +h2 ) =f ∗ h1 +f ∗ h2

fo ( h1 +h 2) =fo h1 + fo h2

the Correlation will be a Somme of Correlation here (Distribution), But it’s not generally true if
I would just apply the Associative or Commutative property. You can also thank from the
inner product point.

The Correlation is the expected value between the signal X and Y (E(XYT]) it’s not will be the
same result if I just interchange E[YXT].

Complexity of convolution in 2D :
# Q18. Explain the advantages of separable filters for the computation of 2D
convolution. Complexity of separate convolution computation in 2D.

# Q19. Explain the low-pass filtering. Provide the examples of smoothing filters.

# Q20.Explain the high-pass filtering. Provide the examples of sharpening filters.
Derivatives.


