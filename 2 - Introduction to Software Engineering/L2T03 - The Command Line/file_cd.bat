@echo off
REM Create three new folders
mkdir Folder1
mkdir Folder2
mkdir Folder3

REM Navigate into one of the folders and create three new folders inside it
cd Folder1
mkdir Subfolder_A
mkdir Subfolder_B
mkdir Subfolder_C

REM Remove 2 of the Subfolders created
rmdir /s /q Subfolder_B
rmdir /s /q Subfolder_C

REM Return to the parent directory
cd ..
