@echo off
setlocal

set "ERP_DIR=%~dp0"
set "PGSQL_BIN=%ERP_DIR%pgsql\bin"
set "PGSQL_DATA=%ERP_DIR%pgsql\data"

echo ============================================================
echo Stopping ConneuralERP SaaS Platform
echo ============================================================

echo Stopping ConneuralERP server...
taskkill /f /im python.exe /fi "WINDOWTITLE eq Odoo*" >nul 2>&1

echo Stopping PostgreSQL cluster...
"%PGSQL_BIN%\pg_ctl.exe" -D "%PGSQL_DATA%" stop -m fast >nul 2>&1

echo ConneuralERP services stopped cleanly.
echo ============================================================

endlocal
