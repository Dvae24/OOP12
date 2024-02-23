class Dog:
    def __init__(self, size, color, breed):
        self.size = size
        self.color = color
        self.breed = breed

    def Chuahua(self):
        return ('size:{}\n'
                ' color:{}\n'
                ' breed:{}').format(self.size, self.color, self.breed)

    def Harold(self):
        return ('size:{}\n'
                ' color:{}\n'
                ' breed:{}').format(self.size, self.color, self.breed)

    def Throx(self):
        return ('size:{}\n'
                ' color:{}\n'
                ' breed:{}').format(self.size, self.color, self.breed)

Dog3_Attributes = Dog(25, "Violet", "Chuahua")
Dog2_Attributes = Dog(20, "Pink", "Rottweiler")
Dog_Attributes = Dog(12, "Red", "Husky")

print("Dog1:\n",Dog_Attributes.Chuahua())
print()
print("Dog2:\n",Dog2_Attributes.Harold())
print()
print("Dog3:\n",Dog3_Attributes.Throx())
print()
print("Dog4:\n")


# Dog_Attributes2 = Dog(12, "Red", "Chuahua").color
# Dog_Attributes3 = Dog(12, "Red", "Chuahua").breed
# print(f"Size:{Dog_Attributes}\n"
#       f"Color:{Dog_Attributes2}\n"
#       f"Breed:{Dog_Attributes3}")

# def greet(name="Jhoon Doe"):
#     print("Hello, " + name)
#
# greet()


