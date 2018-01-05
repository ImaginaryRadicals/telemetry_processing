@ECHO OFF
ECHO.
ECHO View connected devices
ECHO.
adb devices -l
ECHO.
ECHO From /data/data/com.qualcomm.ftcrobotcontroller/files/
ECHO copy telemetry.csv to /sdcard/
ECHO.
adb shell "run-as com.qualcomm.ftcrobotcontroller cp /data/data/com.qualcomm.ftcrobotcontroller/files/telemetry.csv /sdcard/.;"
ECHO.
ECHO copy constants.csv to /sdcard/
ECHO.
adb shell "run-as com.qualcomm.ftcrobotcontroller cp /data/data/com.qualcomm.ftcrobotcontroller/files/constants.csv /sdcard/.;"
ECHO.
ECHO copy controls.csv to /sdcard/
ECHO.
adb shell "run-as com.qualcomm.ftcrobotcontroller cp /data/data/com.qualcomm.ftcrobotcontroller/files/controls.csv /sdcard/.;"
ECHO.

ECHO Pull telemetry.csv from /sdcard/ to local folder
CHDIR
adb pull /sdcard/telemetry.csv .
ECHO Pull constants.csv from /sdcard/ to local folder
CHDIR
adb pull /sdcard/constants.csv .
ECHO Pull controls.csv from /sdcard/ to local folder
CHDIR
adb pull /sdcard/controls.csv .

ECHO.
ECHO Script Complete
ECHO.
PAUSE
CLS
EXIT