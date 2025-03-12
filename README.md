# 🎲 Guess the Number Game

## 📌 Description
Guess the Number is a simple Python game where the computer randomly selects a number within a given range, and the player tries to guess it. The game provides hints and keeps track of the number of attempts.

## 🚀 How to Play
1. Run the Python script.
2. The game will generate a random number between 1 and 10.
3. Enter your guess when prompted.
4. The game will tell you if your guess is too high, too low, or very close.
5. Keep guessing until you find the correct number.
6. Once guessed correctly, the game displays the number of attempts taken.

## 🛠️ Requirements
- Python 3.x

## 📜 Installation & Running the Game
1. Clone this repository or copy the script.
2. Open a terminal and navigate to the script's directory.
3. Run the following command:
   ```bash
   python guess_the_number.py
   ```

## 📝 Code Overview
The game works as follows:
- Uses `random.randint(1, 10)` to generate a random number.
- Takes user input and converts it to an integer.
- Uses a loop to allow multiple guesses.
- Provides hints based on how close the guess is.
- Handles invalid input using `try-except`.

## 🏆 Features
✅ Random number generation
✅ User-friendly hints ("Too high", "Too low", "Very close!")
✅ Tracks the number of attempts
✅ Error handling for invalid inputs

## 📌 Example Run
```
🎲 Welcome to Guess the Number! 🎲
Try to guess a number between 1 & 10.
Enter guess: 5
🔼 Too low!
Enter guess: 7
🔥 Very close!
Enter guess: 8
🎉 Congratulations! You guessed the number 8 in 3 attempts!
```

## 📌 Future Improvements
- Add difficulty levels (Easy, Medium, Hard)
- Allow the player to set a custom range
- Implement a leaderboard to track best scores

## 📜 License
This project is open-source and free to use.

Happy Coding! 🚀

