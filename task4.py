# Создайте класс ContactList, который должен наследоваться от
# встроенного класса list. В нем должен быть реализован метод
# search_by_name, который должен принимать имя, и возвращать список
# всех совпадений. Замените all_contacts = [ ] на all_contacts =
# ContactList(). Создайте несколько контактов, используйте метод
# search_by_name.
class List():
    def __init__(self):
        self.all_contacts = []
    
    def search_by_name(self,*name):
        for i in name:
            self.all_contacts.append(i.title())
        a = [i for i in self.all_contacts if self.all_contacts.count(i) > 1]
        b = set(a)
        print("Список совпадений: ")
        for x in b:
            print("\t","\t",x) 

class Contactlist(List):
    def __init__(self):
        super().__init__()


my_contacts = Contactlist()
my_contacts.search_by_name("odin","dva","tri","tri","dva","odin")
