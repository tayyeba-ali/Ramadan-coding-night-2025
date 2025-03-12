# Todo List Manager using Python & UV

## 📌 Overview
This is a simple command-line Todo List Manager built using Python and the Click library. It allows users to add, list, complete, and remove tasks efficiently. The project is managed using [UV](https://github.com/astral-sh/uv), a modern Python package manager.

## 🚀 Features
- Add new tasks to your todo list
- View all tasks with completion status
- Mark tasks as completed
- Remove tasks from the list
- Uses JSON for persistent storage

## 🛠️ Installation

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/todo-cli.git
cd todo-cli
```

### 2. Install UV and Set Up Virtual Environment
If you haven't installed UV, do so with:
```sh
pip install uv
```
Then create and activate a virtual environment:
```sh
uv venv
uv
```

### 3. Install Dependencies
```sh
uv pip install click
```

## 📌 Usage

### Adding a Task
```sh
uv run python todo.py add "Buy groceries"
```

### Listing Tasks
```sh
uv run python todo.py list
```

### Marking a Task as Completed
```sh
uv run python todo.py complete 1
```

### Removing a Task
```sh
uv run python todo.py remove 1
```

## 📄 File Structure
```
📂 todo-cli
 ├── todo.py  # Main script
 ├── todo.json  # Task storage (auto-generated)
 ├── README.md  # Documentation
```

## 🛠️ Built With
- Python
- Click (Command Line Interface library)
- UV (Python package manager)

## 🎯 Future Improvements
- Add due dates and priorities
- Implement a GUI version
- Sync tasks across multiple devices

## 📜 License
This project is licensed under the MIT License.


