@echo off
title Push ke GitHub - AGOS Smart Diagnostik
cd /d "c:\project bengkel masa depan ai antigravity"
echo ============================================================================
echo   MENGUNGGAH SOURCE CODE AGOS SMART DIAGNOSTIK KE GITHUB
echo   Target: https://github.com/BAGUSW085/AGS-DIAGNOSTIK.git
echo ============================================================================
echo.
echo Sedang mengunggah ke branch main dan apk-offline...
echo (Jika jendela login browser GitHub muncul, silakan klik 'Sign in with browser')
echo.
git push -u origin main
git push -u origin apk-offline
echo.
if %errorlevel% equ 0 (
    echo ============================================================================
    echo [SUKSES] Source code berhasil diunggah ke GitHub AGS-DIAGNOSTIK!
    echo ============================================================================
) else (
    echo ============================================================================
    echo [GAGAL] Upload belum berhasil. Pastikan izin login GitHub telah diberikan.
    echo ============================================================================
)
echo.
pause
