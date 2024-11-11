# Gym Tracker WhatsApp Bot (Django Version)

This project is a Django-based web application that enables users to log and retrieve gym exercises through WhatsApp, using Selenium for WhatsApp Web interactions. Additionally, it includes a web interface to display all logged exercises in a table and provides a search functionality to easily find specific exercises.

## Features

- **Track Exercises**: Log your completed gym exercises, including weight and reps, through Django web app.
- **Retrieve Past Data**: Access your previously logged exercises, organized by type, weight, and reps.
- **Web Interface**: View all your logged exercises in a searchable table on a web page.
- **Search Functionality**: Quickly find exercises by name using the search bar.
- **Local Storage**: All data is stored in a PostgreSQL database for easy retrieval and display.

## How It Works

1. **SQL tables**: Initially I set up the tables required for the database called **gym**. The Django app already has code to connect to DB.

2. **Web Interface**: A Django web application displays the stored exercises in a table format, with a search bar to filter exercises by type, weight, date, or any other attribute.

## Installation and Setup

### Requirements

- **Python 3.x**
- **Django 3.x or later**
- **PostgreSQL**: For storing exercise data.
- **Web browser**: For accessing django app.

## .env file
Ensure you have the following parameters set up in your .env file
- **SECRET_KEY**
- **DB_NAME**
- **DB_USER**
- **DB_PASSWORD**
- **DB_HOST**
- **DB_PORT**

For the original project which this was adapted from, check out [this project](https://github.com/Dani-r-36/gym).

**Note** This project was designed for my own use and hasn't been updated for others to use, but are welcome to use :)
