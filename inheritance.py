from setuptools.extern import names
class Publisher:
 def __init__(self,name):
      self.name=name
 def display(self):
    print(self.name)
class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
    def display(self):
        super().display()
        print(self.title)
        print(self.author)
class Python(Book):
    def __init__(self,name,title,author,price,no_pages):
     super().__init__(name,title,author)
     self.price=price
     self.no_pages=no_pages
    def display(self):
        super().display()
        print(self.price)
        print(self.no_pages)
p1=Python("abc","py","jaan",450,100)
p1.display()


