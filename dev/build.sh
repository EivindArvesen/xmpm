#!/usr/bin/env bash

rm -rf build/ dist/
#rm *.log # *.spec

# python pyinstaller/Makespec.py --onefile --windowed application.py # -i <FILE.icns>, --icon=<FILE.icns>
# python pyinstaller/Build.py application.spec

pyinstaller main.spec #--debug

# file="dist/Raskolnikov.app/Contents/Info.plist"
# beginning=$(head -n $(echo $(($(wc -l $file | awk {'print $1'})-1))) $file)
# new="<key>LSUIElement</key>\n<string>1</string>"
# end=$(tail -n 2 $file)

# printf "$beginning\n$new\n$end" > $file

# touch "dist/Raskolnikov.app"
