#!/usr/bin/env python3
"""
Missing Hubstaff Linux Desktop Client API aka `hsbot`.

This program clicks pre-defined coordinates in Hubstaff Desktop Client,
so that you script your interactions with Hubstaff.
It's blind and silly but that might just be enough.

It seems to me Hubstaff folks deliberately did not include ways
to interact with the program programmatically so that the user does not
cheat. Whatever. I need to automatize this and I can't be told not to.

Known limitations:
- I don't have a way yet to test if any project is running, so you can't tell whether you're
  turning project on or off, I plan to just assume "off" at start and store the pseudo-state
  "outside" (this script will be called from other scripts)
- I tested the program on a fullscreen mode client on i3 window manager,
  I have no idea if it will work with your fancy WM, let me know
- my screen (1920x1080) fits 20 projects, no scrollbar shenanigans implemented, though technically
  possible
- the script assumes fair amount of care and maybe even intelligence, the author assumes you will
  read the whole of it before running it.
- there is no and there won't be installation script
- Tested on Ubuntu/i3wm, it won't work on SteveJobsOs nor SteveBalmerOs

Usage:
./hsbot.py 10 -j
./hsbot.py 4

The program has no Python dependencies, only system ones.
"""
import argparse
import sys
import subprocess
import shutil


assert sys.version_info >= (3, 5), 'Python 3.5 required'

assert shutil.which('wmctrl'), 'apt install wmctrl'
assert shutil.which('xdotool'), 'apt install xdotool'

# found via
# cnee --record --mouse | awk  '/7,4,0,0,1/ { system("xdotool getmouselocation") }'
# I hope you don't need to modify this but if you do, that's easy, fire
# the above command and click each project start
# remember to delete those times in the hubstaff web app
x = 30
ys = (
    184, 229, 268, 310, 354,
    396, 438, 480, 524, 563,
    605, 648, 691, 735, 775,
    816, 859, 899, 941, 987,
)
#
my_titlebar_height = 20

# xdotool can raise windows but I can't make this work, that'd be one dependency less
raise_windows_via_xdotool = 'xdotool search --name Hubstaff windowactivate'
raise_windows = 'wmctrl -Fa Hubstaff'
just_move = 'xdotool mousemove {x} {y}'
click_and_back = 'xdotool mousemove {x} {y} click 1 mousemove restore'


def call(action_string, **kwargs):
    subprocess.run(action_string.format(**kwargs).split())


parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('position', help='which project to click? 0-indexed', type=int)
parser.add_argument(
    '-j','--just-move', help="don't click, just move, I want to test", action='store_true')
parser.add_argument(
    '-t','--titlebar-height',
    help='the height of the titlebar in your window manager',
    default=my_titlebar_height
)
args = parser.parse_args()


y = ys[args.position] + args.titlebar_height

call(raise_windows)
if args.just_move:
    call(just_move, x=x, y=y)
else:
    call(click_and_back, x=x, y=y)

# that's it folks, send money to bartekbrak1@gmail.com
