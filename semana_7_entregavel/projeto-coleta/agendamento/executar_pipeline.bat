@echo off

REM Para criar uma tarefa diaria as 07:00, execute no CMD:
REM schtasks /Create /SC DAILY /ST 07:00 /TN "ColetaMuralTech" /TR "\"C:\Users\pedro\OneDrive\Área de Trabalho\coffee and code\semana_7_entregavel\projeto-coleta\agendamento\executar_pipeline.bat\""
REM
REM Para consultar a tarefa:
REM schtasks /Query /TN "ColetaMuralTech"
REM
REM Para executar imediatamente:
REM schtasks /Run /TN "ColetaMuralTech"
REM
REM Para excluir a tarefa:
REM schtasks /Delete /TN "ColetaMuralTech" /F

for %%I in ("%~dp0..") do set "PROJETO=%%~fI"
set "SCRIPTS=%PROJETO%\scripts"

if not exist "%PROJETO%\logs" mkdir "%PROJETO%\logs"

cd /d "%SCRIPTS%"

"%SCRIPTS%\.venv\Scripts\python.exe" -m coleta.executar >> "%PROJETO%\logs\agendador.log" 2>&1

exit /b %ERRORLEVEL%
