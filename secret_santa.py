import random

phrase1 = ("N° {} : Pour ce Secret Santa, {} va offrir un cadeau à {}!")
phrase2 = "Nombre de personne dans cette famille : {}"


Santa = ['Pierre', 'Edith', 'Annabelle', 'Edeline', 'Benoit', # Groupe Blangero
          'Sylvie', 'Gilles', 'Vincent', # Groupe Sertorio
          'Martine', 'Nicholas', 'Caroline','Paul',#Groupe Snowden
          'Alain', 'Michèle', 'Didier', 'Chrystèle', #groupe Mathias
          ]

Child = ['Pierre', 'Edith', 'Annabelle', 'Edeline', 'Benoit', # Groupe Blangero
          'Sylvie', 'Gilles', 'Vincent', # Groupe Sertorio
          'Martine', 'Nicholas', 'Caroline','Paul','Nathalie',#Groupe Snowden
          'Alain', 'Didier', 'Chrystèle', #groupe Mathias
          ]

random.shuffle(Santa)
random.shuffle(Child)

print(phrase2.format(len(Santa)+1))

def simple():
    compteur = 0
    while Santa:
        elem1 = Santa.pop()
        elem2 = Child.pop()
        # needs to search for the element throughout the list!
  #      if elem1!=elem2:
        compteur += 1
#        Santa.remove(elem1)
 #       Child.remove(elem2)
        print(phrase1.format(compteur,elem1,elem2))
#        else:
 #           pass

simple()

