Missing Hubstaff Linux Desktop Client API aka `hsbot`.

This program clicks pre-defined coordinates in Hubstaff Desktop Client,
so that you script your interactionsw with Hubstaff.
It's blind and silly but that might just be enough.

It seems to me Hubstaff folks deliberately did not include ways
to interact with the program programmatically so that the user does not
cheat. Whatever. I need to automatize this and I can't be told not to.

Known limitations:
- I don't have a way yet to test if any project is running, so you can't tell whether you're
  turning project on or off, I plan to just assume "off" at start and store the pseudo-state
  "outside" (this script will be called from other scripts
- I tested the program on a fullscreen mode client on i3 window manager,
  I have no idea if it will work with your fancy WM, let me know
- my screen (1920x1080) fits 20 projects, no scrollbar shenanigans implemented, though technically
  possible
- the script assumes fair amount of care and maybe even intelligence, tha author assumes you will
  read the whole of it before running it.
- there is no and there won't be installation script
- Tested on Ubuntu/i3wm, it won't work on SteveJobsOs nor SteveBalmerOs

Usage:
- ./hsbot.py 10 -j
- ./hsbot.py 4

The program has no Python dependencies, only system ones
