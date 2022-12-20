# What are public,private and protected access modifiers?
# Public: Done in class attr and inst attr file
# Protected: Writting code below
class Article:
    def __init__(self,title,page_count):
        # Initialize protected attributes
        self._title = title
        self._page_count = page_count

    def _show(self):
        print(f'The title of the book is {self._title} and page count of book is {self._page_count}')

class Author(Article):
    def __init__(self, name, title, page_count):
        # Fetch the details of title and page count from parent class.
        super().__init__(title, page_count)
        self.name = name
    
    def display(self):
        print("Author name: {}".format(self.name))
        # Access article's protected method _show().
        self._show()
        print("***********************************")

auth_obj = Author("Sanika","OOPS Concepts In Python",3000)
auth_obj.display()
# Access protected data
print(auth_obj._title)

# Private Access Modifier
class Language:
    # Initialize the private attribute
    __country = "India"
    def __init__(self,name):
        self.__name = name

    # Private method
    def __show(self):
        # Accessing the private attributes
        print(f"The name of the country is: {Language.__country}")
        print(f"The name of the language is: {self.__name}")

    def display(self):
        # Access private method within the class
        self.__show()

lang_obj = Language("Hindi")
lang_obj.display()
# Access private attribute of class Language
print(lang_obj._Language__country)
lang_obj._Language__show()