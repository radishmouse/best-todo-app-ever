
def print_todos(todos):
    if len(todos) == 0:
        print("You have nothing to do.")
    else:
        print('======= Pending ======')
        for i, todo in enumerate(todos):
            if not todo['completed']:
                print(f"{i}: {todo['title']}")
        print('======================')
        print('======= Completed ======')
        for i, todo in enumerate(todos):
            if todo['completed']:
                print(f"{i}: {todo['title']}")
        print('======================')

def add_todo(todos, item_text):
    new_todo = {
        'title': item_text,
        'completed': False
    }
    todos.append(new_todo)

def set_completed(todos, index):
    try:
        todo = todos[index]
        todo['completed'] = True
    except IndexError:
        print("That todo does not exist.")

def print_menu():
    message = """
    Todo App
==================
0. quit
1. print todos
2. add a todo
3. complete a todo
"""
    print(message)

def get_choice(prompt="Choose one: "):
    is_valid_choice = False
    choice = 0
    while not is_valid_choice:
        try:    
            choice = int(input(prompt))
            is_valid_choice = True
        except ValueError:
            print("Please enter a number.")
    return choice
    
def main():
    todo_list = []

    
    is_running = True
    while is_running:
        print_menu()
        choice = get_choice()
        if choice == 0:
            print("K. Byeeee!")
            is_running = False
        elif choice == 1:
            print_todos(todo_list)
        elif choice == 2:
            new_todo = input("Enter a todo: ")
            add_todo(todo_list, new_todo)
        elif choice == 3:            
            index_to_delete = get_choice("Enter the index to complete: ")
            set_completed(todo_list, index_to_delete)
        

main()
