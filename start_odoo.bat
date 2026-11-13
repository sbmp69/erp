@echo off
setlocal

set "ERP_DIR=%~dp0"
set "PGSQL_BIN=%ERP_DIR%pgsql\bin"
set "PGSQL_DATA=%ERP_DIR%pgsql\data"
set "PYTHON_EXE=%ERP_DIR%venv\Scripts\python.exe"
set "ODOO_BIN=%ERP_DIR%odoo\odoo-bin"
set "ODOO_CONF=%ERP_DIR%odoo.conf"

echo ============================================================
echo Starting CloudERP SaaS Local Environment
echo ============================================================

echo [1/2] Checking PostgreSQL...
"%PGSQL_BIN%\pg_isready.exe" -U odoo -h 127.0.0.1 -p 5432 >nul 2>&1
if %ERRORLEVEL% equ 0 (
    echo PostgreSQL is already running.
) else (
    echo Starting PostgreSQL server...
    start "PostgreSQL Server" /b "%PGSQL_BIN%\postgres.exe" -D "%PGSQL_DATA%"
    timeout /t 3 >nul
)

echo [2/2] Starting Odoo Server...
echo CloudERP is launching at http://localhost:8069
echo Press Ctrl+C to stop the Odoo server.
echo ============================================================

"%PYTHON_EXE%" "%ODOO_BIN%" -c "%ODOO_CONF%"

endlocal

