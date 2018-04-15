import random
import names

races = ['Birb', 'Doggo', 'Kitteh']
plumages = ['blanc', 'noir', 'jaune', 'gris', 'beige', 'vert']
pelages = ['blanc', 'noir', 'brun', 'gris', 'roux']
binaryChoice = [0, 1]
genders = 'mf'
cities = ['Montreal', 'Quebec', 'Rouyn-Noranda', 'Levis', 'St-Hyacinthe', 'Riviere-Du-Loup', 'London',
          'Mongolie Orientale']
descriptions = ['reeeeeeeeeeeee', 'aaaaaaaaaaa', 'Hello there', 'Boop', 'l ll ll l_', 's+e', 'o+e', 'Hello doug',
                'No this is patrick', 'Shreck is love, Shreck is life', 'boop boop', 'bork bork', 'plz boop me', 'floof', 'zoooop']


def insertAnimal(cursor, number):
    for j in range(0, number + 1):
        sexe = random.choice(genders)
        prenom = names.get_first_name(sexe)
        age = random.randint(0, 15)
        location = random.choice(cities)
        race = random.choice(races)

        if race == 'Birb':
            poids = random.randint(0, 4)
        elif race == 'Cat'
            poids = random.randint(0, 30)
        else:
            poids = random.randint(0, 50)
        description = random.choice(descriptions)

        sql = "INSERT INTO animal(id, nom, sexe, age, poids, location, race, description) VALUES ({}, '{}', '{}', {}, {}, '{}', '{}', '{}')"
        cursor.execute(sql.format(j, prenom, sexe, age, poids, location, race, description))

        # insert in the good animal isa database
        if race == 'Birb':
            plumage = random.choice(plumages)
            sql = "INSERT INTO bird(id, plumage) VALUES ({},'{}')"
            cursor.execute(sql.format(j, plumage))
        elif race == 'Doggo':
            pelage = random.choice(pelages)
            castre = random.choice(binaryChoice)
            degriffe = random.choice(binaryChoice)
            sql = "INSERT INTO dog(id, pelage, castre, degriffe) VALUES({}, '{}', {}, {})"
            cursor.execute(sql.format(j, pelage, castre, degriffe))
        else:
            pelage = random.choice(pelages)
            castre = random.choice(binaryChoice)
            degriffe = random.choice(binaryChoice)
            sql = "INSERT INTO cat(id, pelage, castre, degriffe) VALUES({}, '{}', {}, {})"
            cursor.execute(sql.format(j, pelage, castre, degriffe))
