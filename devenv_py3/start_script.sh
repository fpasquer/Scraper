#!/bin/sh
Xvfb :00 &
export DISPLAY=:00
bash
