# Console Todo Application

A simple in-memory console-based todo application built with Python.

## Features

- Add todo tasks with title and description
- View all tasks with status indicators
- Update task details
- Delete tasks by ID
- Mark tasks as complete/incomplete

## Requirements

- Python 3.13+

## Installation

No external dependencies required. Just run the application directly with Python.

## Usage

Run the application:

```bash
python src/main.py
```

Follow the on-screen menu to interact with your todo list.

## Architecture

This application follows clean architecture principles:

- **Domain Layer**: Contains the Todo entity and business rules
- **Application Layer**: Contains use case services
- **Interface Layer**: CLI interface for user interaction
- **Infrastructure Layer**: In-memory repository for storage