class Todo:
    def __init__(self, text):
        self.title = text
        self.completed = False

    def complete(self, is_complete=True):
        self.completed = is_complete

class TodoApp:
    def __init__(self):
        self.todos = []

    def add(self, text):
        todo = Todo(text)
        self.todos.append(todo)

    def complete(self, index):
        try:
            self.todos[index].complete()
        except:
            print(f'No todo found at index {index}')
        
    def show(self):
        if len(self.todos) == 0:
            print("You have nothing to do.")
        else:
            print('======= Pending ======')
            for i, todo in enumerate(self.todos):
                if not todo.completed:
                    print(f"{i}: {todo.title}")
            print('======================')
            print('======= Completed ======')
            for i, todo in enumerate(self.todos):
                if todo.completed:
                    print(f"{i}: {todo.title}")
            print('======================')


    def print_menu(self):
        message = """
    Todo App
==================
0. quit
1. print todos
2. add a todo
3. complete a todo
"""
        print(message)

    def get_choice(self, prompt="Choose one: "):
        is_valid_choice = False
        choice = 0
        while not is_valid_choice:
            try:    
                choice = int(input(prompt))
                is_valid_choice = True
            except ValueError:
                print("Please enter a number.")
        return choice
    
    def main(self):
        is_running = True
        while is_running:
            self.print_menu()
            choice = self.get_choice()
            if choice == 0:
                print("K. Byeeee!")
                is_running = False
            elif choice == 1:
                self.show()
            elif choice == 2:
                new_todo = input("Enter a todo: ")
                self.add(new_todo)
            elif choice == 3:            
                index_to_delete = self.get_choice("Enter the index to complete: ")
                self.complete(index_to_delete)

app = TodoApp()
app.main()
