# UMass STEM Discord Bot

Bot designed for the UMass STEM Discord server for memes and other functionality.

**Bot Prefix**: Start a command with $ to use the bot

## Add to your server

[Invite bot to server](https://discordapp.com/api/oauth2/authorize?client_id=552254598279069708&permissions=1342179392&scope=bot)

## Commands
### Roles
- get [role]
  - The bot gives the specified role to the user
- remove [role]
  - The bot removes the specified role from the user (if they have it)
- getlist
  - Prints out an organized list of roles available with the get command
  
 ### Memes
- mdraw [image/image link/text]
    - The bot responds with an image of marius drawing whatever image or text is passed into the argument
- bdraw [image/image link/text]
    - The bot responds with an image of barrington drawing whatever image or text is passed into the argument
- erase
    - Deletes the most recent m/bdraw generated by the bot
  
**Example of the $bdraw [text] generator**

[![bdraw example](https://i.gyazo.com/c598fe1f391e75f0207dc392332cd622.gif)](https://gyazo.com/c598fe1f391e75f0207dc392332cd622)

## Other functionality
- remove missing housing and major role
    - bot removes the missing housing and major role if someone has set both a housing and major role

### Commands to add
- marius
    - The bot responds with a random marius meme
- barr
    - The bot responds with a random barrington meme
- tim
    - The bot responds with a random tim meme
- meme [text]
    - The bot responds with the inputed image with the specifed text on it in typical meme format
- barrify [url/image]
    - The bot uses computer vision through the OpenCV library to put the barr emote on peoples faces in the inputed image



