@echo off

:start
echo Rebooting bot
python %cd%\Bot.py

TIMEOUT /t 6000
echo Period Elapsed
goto start