from person import Person
from customer import Customer
from product import Product

if __name__ == '__main__':
    person1 = Person("hammiche","kamel",47)
    print(person1.nom, person1.prenom, person1.age)

    client1= Customer("hammiche","kamel",47,)
    print(client1.nom,client1.prenom,client1.age)

    #client1 = Product("")
    #client1 = Customer("hammiche","kamel",47)
    #day2 = Day(20, 2)
    #print (client1)
    # Visits: 10, Contacts: 1
    #print day2
    # Visits: 20, Contacts: 2

    #day3 = day1 + day2
    #print day3
    # Visits: 30, Contacts: 3

    #day4 = sum([day1, day2, day3])
    #print day4
# Visits: 60, Contacts: 6
