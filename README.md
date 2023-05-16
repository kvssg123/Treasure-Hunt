# Treasure-Hunt
The objective of this project is to assess the soft-skills of a player through puzzles and riddles 
## How To Solve
### Level-1 : 
#### Soft-skills assessed : Observation
The initial stage comprises a 15 x 15 grid of emojis depicting hand gestures, with one of them being different from the rest. The odd one out is the only left-handed emoji among the right-handed ones. Once this level is completed, a Wikipedia article is provided as the first clue to assist in solving subsequent levels.

### Level-2: 
#### Soft-skills assessed : Observation, Attention to detail
In this level, you need to identify the national sport of a country without being explicitly provided with the name of the country. The round is designed as an observational challenge where you have to spot a hidden button with a color similar to the background color. Clicking the button will change the background to black and reveal the latitude and longitude of a location. Based on this information, you need to enter the national sport of the country, which in this case is Romania. You can also use the keyboard shortcut "ctrl+A" to select all the text, which will also highlight the hidden text. Once you solve this round, you will be presented with an image of a key and a rainbow as the next clue. The answer is **oian**.

### Level-3:
#### Soft-skills assessed : Involvment , Observation
In this round, you will encounter three questions, the first one being a straightforward riddle. The second question will relate to the article provided in the first round. The third one will be a tricky question that requires a lot of observation and involvement in the previous rounds. Throughout the previous pages, clues have been given with six colors displayed as the background and a rainbow image. You will need to enter the missing 7th color to proceed. Once you clear this task, you will receive an image of rails as the third clue. The answers are **dictionary**,**cryptosystem**,**indigo**.

### Level-4:
#### Soft-skills assessed : Exploring nature,Curiosity
In this round, there are 7 clues given that lead to solving a puzzle related to a Google Doodle. The Google Doodle was released on the 105th birthday of a Lutianian singer named Clara Rockmore, as a token of respect. The doodle contains three lessons taught by an animation of Clara Rockmore, with each lesson represented by a sequence of letters. The task is to provide the sequence of letters for the third lesson in the doodle game. After successfully solving the puzzle, a new clue is revealed in the form of an image showing the number 5.The answer to this round is **gfbed**

### Level-5:
#### Soft-skills assessed : Critical Thinking, Analysing 
This round presents a gibberish text that lacks any apparent meaning. To progress, the player must rely on clues provided in earlier rounds to decipher the correct text and enter it..
##### Clue-1 : An article related to cryptography.
##### Clue-2 : An image of key 
##### Clue-3 : A rail image
##### Clue-4 : Figure showing 5
By putting all these clues at one place. It is some cipher with key=5 and the rails image tells the name of the cipher as **rail cipher**. A small amount of analysis of all clues is sufficient to solve this. The answer is **congratualtionsonclearingthelastroundyoucanseetheresultsinnextpage**

Upon completing all the rounds, the player's information is displayed, including their rank compared to other users, the time taken to finish the game, and the player's personal best time.

### Admin Dashboard - [Admin Dashboard](http://13.49.138.209:8000/admin) 
The admin dashboard mentioned above provides a user-friendly interface to access and manage the database. It allows the admin to track the performance of all the users, including their position relative to others, time taken to solve the questions, and best time. The dashboard also includes various functionalities, such as sorting users based on their best time or IDs. Furthermore, the admin can directly manipulate the data in the database, including manipulating the player data.

### Features Included :
- The project contains clues for solving upcoming rounds and the user cannot navigate to next round till he finishes the current round.
- Admin dashboard is cusomized cointaining necessary features.
- Anyone with email addess can register as player.
- The player's progress is restored.
- All the details like time taken by player, his best time, his position relative to other users etc only at the end of last round.

### Steps to Set-up the project
- Clone the repository or download it as zip file in your local machine.
- Move to the directory where the file **manage.py** is present and open command prompt.
- Install the necessary dependencies from requirements.txt **pip install -r requirements.txt**
- Execute **python manage.py runserver** and the application starts in local host.





