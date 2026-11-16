' Auto-Start Silent Launcher untuk AGOS SMART DIAGNOSTIK by Agos Corporation
' Menjalankan server FastAPI di belakang layar (tanpa jendela CMD hitam) saat Windows menyala.
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "c:\project bengkel masa depan ai antigravity\start_server_background.bat" & chr(34), 0, False
Set WshShell = Nothing
