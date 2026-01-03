# coffee-and-wifi
Local web application built with Flask and Bootstrap that dynamically catalogs cafés

**Overview**

A local web application designed for digital nomads and coffee lovers to find and catalog the best cafés for remote work. This project uses Flask to serve a dynamic directory of cafés, featuring details like wifi strength, power socket availability, and coffee quality. The app reads and writes data to a local CSV file, providing a simple yet effective way to manage a database of work-friendly spots.

**Features**
- Shows a comprehensive table of all saved cafés with their location (Google Maps links), opening and closing hours, and ratings.
- The user can add new cafés to the database via a custom-built WTForm with field validation.
- All data is stored locally in a CSV file, ensuring data persistence without the need for a complex SQL database setup.
- Styled with Bootstrap for a clean, modern look.

**Stack**
- Backend: Python / Flask.
- Frontend: HTML5, CSS3, Bootstrap 5.
- Forms: WTForms.
- Data: CSV.
