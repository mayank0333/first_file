class Lunch:
    def __init__(self,menu):
        self.menu=menu

    def menu_price(self):
        if self.menu=="menu1":
            print("Your choice",self.menu,"Price 12.00")
        elif self.menu=="menu2":
            print("Your choice",self.menu,"print 13.40")
        else:
            print("error in menu")

Paul=Lunch("menu1")
Paul.menu_price()


