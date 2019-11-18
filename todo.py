class Todo:
    # instructions for how to construct
    # a new Todo object
    # Use the __init__() to create instances
    # of the Todo class
    # This method is also known as the "constructor"
    # "dunder init" - "double underscore init"
    def __init__(self, title, completed=False):
        # Assume that a new todo
        # is not already completed.
        # So we set the default argument
        # value to False
        self.title = title
        self.completed = completed

    # behaviors


    # Examples of "Encapsulation"
    # This means you hide the details of how
    # your code works.
    # You manage that yourself.
    # You present an interface to anybody using
    # your code, but you don't require
    # them to know those details.
    def update_title(self, new_title):
        if self.title != new_title:
            self.updated_on = '2019-11-18' # whatever the current date really is
        self.title = new_title
        
    
    def update_completed(self, new_completed):
        self.completed = new_completed
        if self.completed:
            self.completed_on = '2019-11-18' # no really, calculate the current date
        

    def display(self):
        # You must use the keyword
        # "self" as the first argument
        # so that an object can
        # call the function.
        # It links the function
        # to the object.
        print(self.title)

    def __str__(self):
        return f"{self.title} ({self.completed})"