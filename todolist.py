from todo import Todo

class TodoList:
    def __init__(self):
        # properties
        # - todos
        self.todos = []

    def display(self):
        for todo in self.todos:
            print(todo)

    def add(self, title):
        # Instantiate a new Todo object
        new_todo = Todo(title)
        self.todos.append(new_todo)

    def add_already_completed(self, title):
        new_todo = Todo(title, True)
        self.todos.append(new_todo)

    def complete(self, index):
        todo = self.todos[index]
        # todo.completed = True
        todo.update_completed(True)

# behaviors
# - print
# - add
# - complete
