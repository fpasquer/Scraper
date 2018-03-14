#!/bin/sh
Xvfb :00 &
export DISPLAY=:00
python3 scraper/main.py
