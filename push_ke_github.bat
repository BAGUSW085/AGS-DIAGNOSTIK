@echo off
title Push ke GitHub - AGOS Smart Diagnostik
cd /d "c:\project bengkel masa depan ai antigravity"
echo ============================================================================
echo   MENGUNGGAH SOURCE CODE AGOS SMART DIAGNOSTIK KE GITHUB
echo   Target: https://github.com/BAGUSW085/agos-smart-diagnostik.git
echo ============================================================================
echo.
echo Sedang mengunggah ke branch main...
echo (Jika jendela login browser GitHub muncul, silakan klik 'Sign in with browser')
echo.
git push -u origin main
echo.
if %errorlevel% equ 0 (
    echo ============================================================================
    echo [SUKSES] Source code berhasil diunggah ke GitHub!
    echo Sekarang Anda siap melanjutkan deploy di Render.com.
    echo ============================================================================
) else (
    echo ============================================================================
    echo [GAGAL] Upload belum berhasil. Pastikan izin login GitHub telah diberikan.
    echo ============================================================================
)
echo.
pause
