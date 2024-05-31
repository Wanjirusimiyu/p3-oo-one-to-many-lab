class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []


    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner=owner
        self.all.append(self)
  
       

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def pets(self):
        return self.pets
    
    def add_pets(self,pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet instance")
        pet.owner = self
        self.pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self.pets, key=lambda x: x.name)
        
       
          


      
        