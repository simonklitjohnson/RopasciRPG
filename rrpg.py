#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

#import start
import sys
import os
import random
import pathlib
import pickle
import glob
import json
#import end
exec(open("helpers.py").read())

exec(open("classes.py").read())

exec(open("declarations.py").read())

exec(open("functions.py").read())


#entities

exec(open("entities/enemies.py").read())

exec(open("entities/items.py").read())

exec(open("entities/weapons.py").read())

exec(open("entities/itemeffects.py").read())

#entities end

#gameloops start
exec(open("loops/fighting.py").read())

exec(open("loops/initiate.py").read())

exec(open("loops/main.py").read())

exec(open("loops/newgame.py").read())

exec(open("loops/stores.py").read())

exec(open("menu/instructions.py").read())

exec(open("menu/modinfo.py").read())

exec(open("menu/about.py").read())

exec(open("menu/saveload.py").read())

exec(open("menu/exit.py").read())
#gameloops end

#mods start
exec(open("tools/modload.py").read())
#mods end

exec(open("tools/compile.py").read())

#run it all
try:
	if __name__ == '__main__':
		initiate()
except KeyboardInterrupt:
	handleinterrupt()
