@echo off
title Reparador de Integridade do Sistema - Windows 11
cls

echo ======================================================
echo    INICIANDO VERIFICACAO DE INTEGRIDADE DO SISTEMA
echo ======================================================
echo.

:: 1. DISM - Verifica e repara a imagem do Windows
echo [1/3] Executando DISM (Reparo de Imagem)...
echo Isso pode demorar alguns minutos dependendo da conexao.
dism /online /cleanup-image /restorehealth
echo.

:: 2. SFC - Verifica arquivos corrompidos
echo [2/3] Executando SFC (System File Checker)...
sfc /scannow
echo.

:: 3. CHKDSK - Verifica erros no SSD
echo [3/3] Verificando integridade do Disco C:...
echo Deseja agendar uma verificacao de disco (CHKDSK) para o proximo reinicio?
echo (Isso e recomendável se o seu PC travou com 100%% de uso)
set /p escolha="Digita 'S' para sim ou 'N' para pular: "

if /i "%escolha%"=="S" (
    chkdsk C: /f
    echo.
    echo [ OK ] Verificacao de disco agendada.
) else (
    echo [ ! ] Verificacao de disco pulada pelo usuario.
)

echo.
echo ======================================================
echo        PROCESSO CONCLUIDO! REVISE OS RESULTADOS.
echo ======================================================
pause