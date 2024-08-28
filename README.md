# Router Backup Automation

## Overview

This project automates the backup of an XML file containing router settings (pfSense). It consists of two Python scripts that are compiled into executable files. These executables are scheduled to run daily to ensure regular backups of the router settings.

## Components

1. mires_app.py - Main application script for handling the backup process.
2. router_password.py - Manages router authentication details.

Both scripts are compiled into .exe files and scheduled to run automatically.

## Installation

1. Compile Python Scripts to Executables
   - Ensure pyinstaller is installed:

```bash
     pip install pyinstaller
```
     
   - Compile the Python scripts:
    
```bash
     pyinstaller --onefile --icon='lightbrown.ico' mires_app.py
     pyinstaller --onefile --icon='iconfinder.ico' router_password.py
``` 
2. Setup Scheduled Task
   - Use Task Scheduler in Windows or an equivalent tool to schedule mires_app.exe to run daily.

## Usage

### Commands

- mires_app.exe
  - Description: This executable handles the backup process of the router settings.
  - Usage: Run this executable to perform the backup of the XML file.

- router_password.exe
  - Description: This executable manages the router authentication details.
  - Usage: Run this executable if you need to update or verify router authentication details.

## Contact

If you encounter any issues or need assistance, please contact me via Telegram: [@Mordsad](https://t.me/mordsad).
