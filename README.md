# Study-Planner

## Overview

Study-Planner is a Python-based study management application designed to help students organize their study tasks, create study plans, revise topics using spaced repetition, and have effective and focused study sessions with help of pomodoro timer.

## Features

- Add, view, complete, and delete study tasks
- Create and view study plans
- Add topics to a spaced repetition schedule
- Track revision progress
- Complete and delete revision topics
- Pomodoro study timer
- Alarm notification when a Pomodoro session ends
- JSON-based data storage
- Input validation and error handling

## Technologies Used

- Python
- JSON
- Pytest
- Git
- GitHub
- Visual Studio Code

## Project Structure

Study-Planner/
├── data/
│   └── study_data.json
├── planner/
│   ├── __init__.py
│   ├── pomodoro.py
│   ├── spaced_repetition.py
│   ├── storage.py
│   ├── study_plan.py
│   └── task_manager.py
├── tests/
│   ├── test_planner.py
│   ├── test_pomodoro.py
│   └── test_spaced_repetition.py
├── main.py
├── requirements.txt
├── README.md
└── statement.md