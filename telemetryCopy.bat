@ECHO OFF
ECHO.
ECHO View connected devices
ECHO.
adb devices -l
ECHO.
ECHO Copy telemetry.csv to /sdcard/ from 
ECHO /data/data/com.qualcomm.ftcrobotcontroller/files/
ECHO.
adb shell "run-as com.qualcomm.ftcrobotcontroller cp /data/data/com.qualcomm.ftcrobotcontroller/files/telemetry.csv /sdcard/.;"
ECHO.
ECHO Pull telemetry.csv from /sdcard/ to local folder
CHDIR
adb pull /sdcard/telemetry.csv .
ECHO.
ECHO Script Complete
ECHO.
PAUSE
CLS
EXIT