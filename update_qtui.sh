#!/bin/bash

rm scripts/gui/qtmain.py
rm scripts/gui/qtinfo.py

pyuic6 -x qt/main.ui -o ./scripts/gui/qtmain.py
pyuic6 -x qt/info.ui -o ./scripts/gui/qtinfo.py

echo "main.ui -> qtmain.py"
echo "info.ui -> qtinfo.py"