class Animals: 

    def __init__(self, id, name, species, locationId, customerId, status):
        self.id = id
        self.name = name 
        self.species = species
        self.location = locationId
        self.customer = customerId
        self.status = status

        # a1 = Animals("Snickers", "Dog", 1, 4, "Admitted")
        # a2 = Animals("Gypsy", "Dog", 1, 2, "Admitted")
        # a3 = Animals("Blue", "Cat", 2, 1, "admitted")