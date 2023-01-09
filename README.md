# AP-Farm
Attempt at farming account level(AP) in valorant by AFK botting
#
My intent here was to be able to start this bot, and leave my PC automatically queue into a DM, prevent being afk, and receieve AP. However, something is missing and VALORANT knows you are botting. My guess is that you need to be able to hit a target, mouse_event (move the camera around in-game), or get a kill, all of which would require dipping into HWID ban territory IMO.

inGameCheck() checks for the color cyan in the center of your screen (my cross hair color) to determine if you are in-game. To get the program to work correctly change the matchrgb() statement, or the color of your crosshair, or you know, code something different.

You're gonna wanna already have deathmatch queue selected, then just start the program, click on the desktop or any program running on the monitor you want valorant to open on, and the program will do everything else

Had fun making this, but I hit a roadblock on the whole idea of having to risk HWID ban to get the thing to start getting AP, so I'm persoanlly shelving this project until further notice.

#added a beizer curve to the mouse movement

credit to https://github.com/SineshX/NO-AFK for the start of which I built all this code from, but I kinda redid pretty much everything it's not even morally correct to call this new monsotorsity a "fork"
