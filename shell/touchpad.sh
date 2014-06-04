#!/bin/sh

# Sometimes system gets overloaded and Synaptics freeze
# in my system a pm-susend and back solves the issue
# but the better solution is to use xinput disable and 
# re enable it back. Tests  in other system works,

TOUCH="SynPS/2 Synaptics TouchPAd"
echo "restarting $TOUCH"
exec xinput disable $TOUCH
exec xinput enable $TOUCH
