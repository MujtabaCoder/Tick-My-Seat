

# Tick My Seat

## Project Overview

**Tick My Seat** is a web application designed to provide a convenient platform for users to reserve cinema seats. This application allows users to view available movies, select seats, and make reservations. The project is built using Python, Django, MySQL, HTML, CSS, and Ninja.js.

## Features

- **User Authentication**: Secure user registration and login system.
- **Seat Selection**: Interactive seat map to select available seats for a chosen show.
- **Reservation Management**: Users can view and manage their reservations.


## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```
   git clone https://github.com/MujtabaCoder/Tick-My-Seat/.git
   cd tick-my-seat
   ```

2. **Create and activate a virtual environment:**
   ```sh
   # Install virtualenv if you don't have it
   pip install virtualenv

   # Create a virtual environment
   virtualenv venv

   # Activate the virtual environment
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   - Ensure you have MySQL installed and running.
   - Create a database for the project.
   - Configure the database settings in `settings.py` under the `DATABASES` section.

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_database_user',
           'PASSWORD': 'your_database_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. **Apply migrations and create a superuser:**
   ```
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```
   python manage.py runserver
   ```

7. **Access the application:**
   - Open your browser and go to `http://localhost:8000`.

## Usage

- **User Interface**: Users can browse available movies, select showtimes, and choose seats.

## Technologies Used

- **Backend**: Python, Django, MySQL
- **Frontend**: HTML, CSS, Ninja.js
- **Authentication**: Django's built-in authentication system

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/) for providing the web framework.
- [MySQL](https://www.mysql.com/) for database management.
- [Ninja.js](https://ninja.js.org/) for frontend interactivity.

---

Feel free to adjust the details, such as the project URL, feature descriptions, and any other specific information about your project.
