@echo off
REM Check if the folder "new_folder" exists
if exist "new_folder" (
    REM If "new_folder" exists, create "if_folder"
    mkdir if_folder
) else (
    REM If "new_folder" does not exist, create "new-projects"
    mkdir new-projects
)

REM Check and see if "if_folder" exists and then create "hyperionDev" or "new-projects" accordingly
if exist "if_folder" (
    mkdir hyperionDev
) else (
    mkdir new-projects
)
