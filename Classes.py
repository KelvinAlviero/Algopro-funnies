class food_KA:  
    def __init__(self, name, amount):
        self.__name = name 
        self.__amount = amount

    def get_name_KA(self):
        return self.__name

    def get_amount_KA(self):
        return self.__amount

    def get_priceperpound_KA(self):
        return self.foods.get(self.__name)

    foods = {
        "Dry cured Iderian ham" = 177.80,
        "Wagyu steaks" = 450.00,
        "Mushroom steaks" = 272.00,
        "Kopi luwak coffee" = 306.50,
        "Moose chese" = 487.20,
        "White truffels" = 3600.00,
        "Blue fin tuna" = 3603.00,
        "Le Bonnotte potato" = 270.81
    
    def total_price_KA(self):
        return self.get_priceperpound_KA(self)
        


    


    