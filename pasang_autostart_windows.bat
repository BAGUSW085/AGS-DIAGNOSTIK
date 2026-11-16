@echo off
setlocal
set "STARTUP_DIR=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
copy /Y "%~dp0run_agos_autostart_silent.vbs" "%STARTUP_DIR%\AGOS_Smart_Diagnostik_AutoStart.vbs" >nul
echo [SUKSES] Auto-Start AGOS SMART DIAGNOSTIK berhasil dipasang di Windows Startup!
echo Server http://localhost:8000/ akan otomatis menyala setiap kali laptop dihidupkan.
pause
