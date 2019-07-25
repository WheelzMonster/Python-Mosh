L'implémentation par défaut de Python est CPython, fait en C. Cela signifie que le langage Python est fait en C. Cependant, il existe également d'autres implémentations de Python :

-   Jython fait en Java (on peut donc importer un peu de Java dans un programme python)
-   IronPython fait en C# (même bénéfice que Jython mais pour C#)
-   PyPy qui est fait avec Python lui-même

Etant la version par défaut et la plus répandue, CPython est toujours mise à jour en premier.

# Comment Python est-il éxécuté ?

Les langages primaires ou bas niveaux tels que C, C++, C# Java, Python sont sous formes de textes que seuls nous comprenons, la machine ne comprend que le binaire. C'est le job du compilateur. Il convertit du code C (par exemple, mais il en va de même pour Java, C++ etc) en code binaire. Cependant, le binaire dans lequel il est transcrit est spécifique au processeur utilisé, donc a un système d'exploitation. Exemple : un programme compilé sur Windows ne fonctionne pas sur Mac.

Java à une approche différente : plutôt que de compiler le langage en binaire, il le compile en un "langage portable" appelé "Java ByteCode" qui n'est donc spécifique à aucune plateforme. Cependant, il nous reste encore à traduire le Java ByteCode en binaire. Java viens donc installé avec une JVM (Java Virtual Machine) qui permettra de faire la convertion en binaire. Quand on lance un programme Java, JVM se lance et charge le Java Bytecode durant l'exécution du programme Java, JVM va convertir chaque instructions en binaire.

On peut donc exécuter un programme Java sur n'importe quelle plateforme ayant une JVM. Cela permet donc (entre autre) l'héritage de classes Java par des classes Python et l'exécution de code Python durant le fonctionnement d’un programme Java. Il existe des JVM pour Windows, Mac etc. Python et C# on prit le même chemin, ils sont donc plateforme-indépendant.

Quand on lance un programme Python en utilisant CPython, ça va compiler notre code Python en PythonBytecode puis il va passer ce Bytecode dans PVM (Python Virtual Machine) qui finira par le convertir en binaire, puis l'exécuter.

# Pourquoi peut-on utiliser du Java dans notre programme Python en utilisant Jython ?

Quand on utilise Jython pour lancer un programme en Python, plutôt que de compiler le code en PythonBytecode comme le ferai CPython, Jython compilera le code en JavaBytecode. Donc on peut utiliser ce JavaBytecode dans une Java Virtual machine. C'est pourquoi on peut importer du code Java dans un programme python en utilisant Jython. Parce que le résultat final est du JavaBytecode qui finira par être exécuter par un JVM.

# Typage (de variable) dynamique

_pour en savoir plus sur le type de variable, aller dans ./basics/app.py c'est le début_

En ce qui concerne le typage des données, il existe deux catégories :

-   le typage statique (C++, C#, Java) où les types de variables sont déterminés lors de la compilation du programme

-   le typage dynamique (Javascript, Ruby, Python) où les types de variables sont déterminés lors de l'exécution du programme

Dans les langages utilisant un typage statique, lorsqu'on déclare une variable, il faut spécifier son type.

exemple en C# :

> int studentCount = 1000

De cette façon, le type de cette variable sera toujours un nombre entier. Le programme et le compilateur savent que `studentCount` est un nombre entier. Donc si dans la suite de notre programme on essaie de réassigner sa valeur à autre chose qu'un nombre entier (comme par exemple : `studentCount = True`) alors il y aura une erreur lors de la compilation du programme.

A l'inverse, dans les langages utilisant un typage dynamique, il n'y a pas besoin de spécifier le type de notre variable. Il faut simplement lui assigner une valeur. Le type de la variable sera déterminer lorsque le programme sera exécuter.

exemple en Python :

> studentCount = 1000

_Dans un programme utilisant un langage dynamique comme Python, si l'on souhaite connaître le type d'une variable, on peut passer sa souris dessus dans VSCode ou faire `print(type(studentCount))` pour afficher le type de la variable dans la console. Cela affichera `<class 'int'>` dans la console. Puisque Python est un langage orienté objet, on retrouve ici le concept de classe : en python il y a une classe nommmée `int` qui représente les nombres entiers. Donc toutes les variables étant des nombres entiers seront des instances de cette classe. Le chapitre sur les classes arrive après._

# Les chaînes de caractères (strings)

_Etant donné que c'est difficile d'expliquer ça sans code, pour en savoir plus sur les strings, se rendre dans ./basics/app.py puis descendre jusqu'à 'STRINGS'._

# Les 'escape sequences'

_toujours dans ./basics/app.py, descendre jusqu'à espace sequences_

# Les 'formatted strings'

_toujours dans ./basics/app.py, descendre jusqu'à formatted strings_

# Principales méthodes sur les chaînes de caractères

_toujours dans ./basics/app.py, descendre jusqu'à useful strings methods_

# Les nombres (partie cool sur le binaire et l'hexa) et les opérateurs arithmétiques

_toujours dans ./basics/app.py, descendre jusqu'à numbers_

# Principales méthodes sur les nombres

_toujours dans ./basics/app.py, descendre jusqu'à useful number methods_

# Conversion de type

_toujours dans ./basics/app.py, descendre jusqu'à type conversion_

# Conditions et opérateurs logiques

_toujours dans ./basics/app.py, descendre jusqu'à conditionnal statement and operators_








