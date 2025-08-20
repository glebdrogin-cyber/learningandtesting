#!/bin/zsh

if [ ${1,,} = glebdrogin ]; then
	echo "Oh, you are the boss here, welcome!"
elif [ ${1,,} = help]; then 
	echo "Just enter your username, dude!"
else
	echo "I do not know who you are. But you are not the boss of me!"
fi

