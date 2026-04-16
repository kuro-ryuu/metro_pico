@echo off
start "mpremote.webserver" python -m http.server
@rem Extract comport name where pico is connected
for /f "tokens=1 delims= " %%a in ('mpremote connect list ^| findstr /R /C:"COM[0-9]"') do set comport=%%a
if "%comport%"=="" (
  echo ERROR: could not detect a Pico serial port from mpremote connect list.
  echo Run "mpremote connect list" manually and update this script if needed.
  goto :end
)
echo Device: %comport%
timeout /t 2 /nobreak
@rem Run mpremote
mpremote connect %comport% mip install --target / http://localhost:8000/
:end
@rem The following line terminates all processes with mpremote.webserver as the window title.
taskkill /fi "WINDOWTITLE eq mpremote.webserver"
