# Metaphoria: The Ultimate Story Companion

## Overview

Metaphoria is a web application that serves as the ultimate story companion. It helps users discover stories similar to their favorite ones and uncover new literary gems with ease. Whether you're a writer looking for inspiration or a reader seeking new adventures, Metaphoria can assist you in finding the perfect story.

## Project Structure

The project consists of the following files and directories:

- **app.py**: This is the main Python script that runs the Metaphoria web application. It utilizes Flask, the Metaphor Python library, and BeautifulSoup for web scraping.

- **templates**: This directory contains the HTML template file used by the Flask application to render the user interface.

- **requirements.txt**: This file lists the required Python packages and their versions. You can use it to install the necessary dependencies.

## How to Run

Follow these steps to run the Metaphoria web application:

1. Ensure you have Python installed on your system.

2. Clone this repository to your local machine.

3. Install the required Python packages listed in `requirements.txt` using pip:

```bash
pip install -r requirements.txt
```
4. Run the Flask application by executing `app.py`:

To run the Metaphoria web application, execute the `app.py` script using the following Python command:
```bash
python app.py
```
5. Open a web browser and navigate to `http://127.0.0.1:5000` to access Metaphoria.

## Usage

1. Enter your story or text in the provided textarea on the Metaphoria homepage.

2. Click the "Submit" button to generate story suggestions.

3. Explore the suggested stories listed on the page. Click on a title to view its content in the embedded iframe.

## About

Metaphoria was created as a project to assist users in finding stories that match their preferences. It uses the Metaphor Python library for searching related content and web scraping techniques to display story suggestions.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests on the GitHub repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

