# misy350-group-assignment
Description: For our project, we will be creating a 2 table database for an intramural basketball team. One of these tables will hold all the player names, height, weight and position. The second table will contain the stats for this player. These stats will include field goal percentage, 3-point percentage, and overall player rating along with the player name that these stats belong to. This will be a one to many relationship. For one player, there are many statistics.


Setup Instructions:

Make sure to use Python version 2.7.x.

Install virtualenv if needed.

If you do not have a virtual environment yet on the project folder, set it up with:

$ virtualenv venv
Then activate the virtual environment

$ source venv/bin/activate
Install packages

$ pip install -r requirements.txt
To initialize the database:

$ python manage.py deploy
To run the development server (use -d to enable debugger and reloader):

$ python manage.py runserver -d


Navigating the webpages:

Home-base.html is where you can navigate between the Home, Players, Statistics, and Members pages.

The members.html page is where you can learn more about the team captains.

The player-add.html page is where you can add a player to the team by entering Name, Height, Weight, and Position

The player-all.html page is where each player is listed on the roster.

The player-delete.html tab is where you can delete a player that no longer plays on the team.

The player-edit.html page is where you can edit a player(say someone gained some weight or height).

The statistic-add.html page is where you can add statistics about a player through Field Goal Percentage, Three Point percentage, and Player Rating.

The statistic-all.html page is where you can see those statistics for all players.

The statistic-delete.html page is where you can delete stats from players through clicking the delete button.

The statistic-edit.html page is where you can edit a players stats after each game.
