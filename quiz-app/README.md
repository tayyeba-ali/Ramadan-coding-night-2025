# 📝 Quiz Application

This is a simple **Quiz Application** built using **Streamlit** in Python. The application presents a random question from a predefined set of questions and allows users to select an answer. It then provides feedback on whether the answer is correct or incorrect.

## ⭐ Features
- 🎲 Randomized questions from a predefined set
- ✅ Multiple-choice format
- ⚡ Instant feedback on the selected answer
- 🎈 Celebration animation for correct answers
- 🔄 Automatic question refresh after answering

## 📥 Installation
To run this application, you need to have **Python** installed. Follow the steps below to set it up:

### 1️⃣ Clone the Repository
```sh
$ git clone https://github.com/yourusername/quiz-app.git
$ cd quiz-app
```

### 2️⃣ Install Dependencies
Install the required dependencies using:
```sh
$ pip install streamlit
```

### 3️⃣ Run the Application
Execute the following command to start the application:
```sh
$ streamlit run quiz.py
```

## 🛠 Code Overview
The application consists of the following key components:
- 🎲 **Randomized Question Selection**: Each time the user submits an answer, a new random question is displayed.
- 🎯 **User Interaction**: Users select an answer using radio buttons and submit their choice.
- ✅ **Instant Feedback**: The application indicates whether the selected answer is correct or incorrect.
- 🎈 **Balloon Animation**: If the user selects the correct answer, balloons appear as a celebration effect.
- 🔄 **Automatic Refresh**: The next question appears automatically after a short delay.

## 📝 Example Question Format
```python
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Islamabad", "Karachi", "Lahore", "Quetta"],
        "answer": "Islamabad"
    }
]
```

## 🤝 Contributing
Feel free to fork this repository and submit pull requests with improvements! 🚀

## 📜 License
This project is licensed under the **MIT License**.

