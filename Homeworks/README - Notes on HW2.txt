This one ate away my life a bit

A LOT could potentially be done but unfortunately I sort of ran out of time
As you'll notice, there are 3 different files on HW2
1-) HW2_Fancy.py -> This was the first solution I started with.
I was looking at the libraries python has and I saw that one of them is sqlite so I was planning on using tables for my user database
but then I decided to go with a simpler solution then try to implement that if I have time. Apparently that was the right call.
The reason why it's "fancy" was because I was planning on creating a UI and some fancy regex username-password checks as well but again, time wasn't available.
I left it there cause I already sort of figured out the flow and I didn't want to lose the progress.
2-) HW2_FullApp.py -> This is the second solution, and the first one I finished completely. It's about 400 lines and does a bit more than what the app does with extra steps
I opted out of using a database but I knew I wanted to at least store the information on the disk so it'd be at least a bit more realistic than just pushing it to the memory.
This one is using json format to store the user information between sessions. It also has deleting, updating and listing user information. Creating users and login also has some
extra scenarios in that one. It's pretty large so might be difficult to test + might have some bugs (although I don't think there'd be)

The username information is stored in "userdb.json" file

This one doesn't have regex and stuff like that, just does a basic username - password check with whatever's available in string library.
However, I was at least hoping to switch from json to db but alas. If you have the time and curious, I'd recommend using this one. It has some memes and secrets.
(I have a general theme of an evil corporation going on between all the projects. This one is the most detailed one.)
3-) HW2_Simplified.py -> Just in case you might not want to see any other code anymore, I created this one. It's simple: doesn't do any file I/O or the extra steps.
It literally just gets user info, stores it in a hashmap then checks that info on login. Has some memes but not cool enough, however should be easier to test.
But HW2_FullApp has way more cool stuff

GENERAL NOTES:
1. I have a lot of the information listed on top of the HW2_FullApp.py file and the code is in general well documented and commented
2. One thing to note is that when using the List menu option of HW2_FullApp, you need to enter special admin credentials
username = admin
password = admin
3. HW2_FullApp Also has some javadoc style comments on each function
4. Util.py file is used for general printing purposes and some utility functions
5. There are A LOT of print statements in the HW2_FullApp.py. I tried to separate some of them into the util.py file but moving some just didn't seem like it'd worth it
6. If you decide to use HW2_FullApp, the saving to file only happens on quitting. Doing that in-between each action would be an overkill so I just went with saving to the file at the end approach

 