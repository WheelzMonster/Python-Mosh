L'implémentation par défaut de Python est CPython, fait en C. Viens ensuite :

-   Jython fait en Java (on peut donc importer un peu de Java dans un programme python)
-   IronPython fait en C# (même bénéfice que Jython mais pour C#)
-   PyPy qui est fait avec Python lui-même

Etant la version la plus répandue, CPython est toujours mise à jour en premier.

# Comment Python est-il éxécuté ?

Les langages primaires ou bas niveaux tels que C, C++, C# Java, Python sont sous formes de textes que seuls nous comprenons, la machine ne comprend que le binaire. C'est le job du compilateur. Il convertit du code C (par exemple) en code binaire. Cependant, le binaire dans lequel il est transcrit est spécifique au processeur utilisé, donc a une plateforme. Un programme compilé sur Windows ne fonctionne pas sur Mac.

Java à une approche différente : plutôt que de compiler le langage en binaire, il le compile en un "langage portable" appelé "Java ByteCode" qui n'est donc spécifique à aucune plateforme. Cependant, il nous reste encore à traduire le Java ByteCode en binaire. Java viens donc installé avec une JVM (Java Virtual Machine) qui permettra de faire la convertion en binaire. Quand on lance un programme Java, JVM se lance et charge le Java Bytecode durant l'exécution du programme Java, JVM va convertir chaque instructions en binaire.

On peut donc exécuter un programme Java sur n'importe quelle plateforme ayant une JVM, il existe des JVM pour Windows, Mac etc. Python et C# on prit le même chemin, ils sont donc plateforme-indépendant.

Quand on lance un programme Python en utilisant CPython, ça va compiler notre code Python en PythonBytecode puis il va passer ce Bytecode dans PVM (Python Virtual Machine) qui finira par le convertir en binaire, puis l'exécuter.

# Pourquoi peut-on utiliser du Java dans notre programme Python en utilisant Jython ?

Quand on utilise Jython pour lancer un programme en Python, plutôt que de compiler le code en PythonBytecode comme le ferai CPython, Jython compilera le code en JavaBytecode. Donc on peut utiliser ce JavaBytecode dans une Java Virtual machine. C'est pourquoi on peut importer du code Java dans un programme python en utilisant Jython. Parce que le résultat final est du JavaBytecode qui finira par être exécuter par un JVM.
