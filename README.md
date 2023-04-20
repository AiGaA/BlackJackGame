# Black Jack Game

BlackJack is a Python terminal game, which runs in the Code Institutes mock terminal on Heroku.

Users simply can try to beat the computer by choosing which turn to take - 'HIT' or 'STAND'.

## How to play

## Features

### Future Features

## Data Model

## Testing

The project has been manually tested by doing following:
- Testing in local and the deployed Heroku terminal.
- Giving wrong inputs, apart from exactly 'HIT' or 'STAND'.
- Passed code through PEP8 linter and confirmed there are no problems.



## Bugs

### Solved Bugs

### Remaining Bugs

## Validator Testing

## Deployment
### Heroku

## Credits

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!