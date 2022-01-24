import enum


class Baker:
    shelf = []

    def __init__(self, product, ingredients):
        self.product = product
        self.ingredients = ingredients

        self.storage = dict()


    def __has_ingredients(self):
        req = self.__requirements()

        for ingredient in self.ingredients:
            if not ingredient in self.storage:
                return False

            if self.storage[ingredient] < req[ingredient]:
                return False
        
        return True

    def __requirements(self):
        res = dict()

        for ingredient in self.ingredients:
            if not ingredient in res:
                res[ingredient] = 0

            res[ingredient] += 1 

        return res


    def purchase(self, parts):
        for item in parts:
            if item not in self.storage:
                self.storage[item] = 0

            self.storage[item] += 1

    def bake(self):
        if not self.__has_ingredients():
            raise Exception("Not enough ingredients in storage for %s" % self.product)

        for ingredient in self.ingredients:
            self.storage[ingredient] -= 1
        
        Baker.shelf.append(self.product)
        return True

    def __str__(self):
        st = "Bakes %s - " % self.product

        for key, value in self.__requirements().items():
            st += "%d %s " % key, value
        
        return st[:-1]

if __name__ == "__main__":
    dan = Baker("nuts_delight",["nuts","maple","sugar","cider","almonds","nuts"])
    dan.purchase(["maple", "sugar", "nuts", "maple", "cider"])

    try:
        dan.bake()
        assert False
    except:
        assert True

    dan.purchase(["nuts", "almonds"])

    gal = Baker("healthy_bounty", ["maple", "tahini", "coconut", "coconut oil","dark chocolate"])
    gal.purchase(["maple", "tahini", "tahini", "coconut", "coconut oil", "dark chocolate"])
    

    dan.bake()
    assert Baker.shelf == ["nuts_delight"]
    
    try:
        gal.bake()
        assert True
    except:
        assert False

    assert Baker.shelf == ["nuts_delight", "healthy_bounty"]
    
    # assert str(dan) == "Bakes nuts_delight - 2 nuts 1 maple 1 sugar 1 cider 1 almonds"
    # assert str(gal) == "Bakes healthy_bounty - 1 maple 1 tahini 1 coconut 1 coconut oil 1 dark chocolate"
