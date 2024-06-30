# Quora-Duplication-Question-Google-Gemini-API-KEY

This project is a web application that helps identify if two given questions are duplicates using a machine learning model. Additionally, it integrates with Google Gemini API to generate responses for duplicate questions.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Training](#model-training)
- [API Integration](#api-integration)
- [Technologies Used](#technologies-used)
- [License](#license)

## Features

- Identify duplicate questions using machine learning
- Generate responses for duplicate questions using Google Gemini API
- Web-based user interface

## Installation

### Prerequisites

- Python 3.10+
- pip (Python package installer)

### Clone the Repository

```sh
git clone https://github.com/yourusername/quora-duplication-question-finder.git
cd quora-duplication-question-finder


python3 -m venv venv
source venv/bin/activate
 # On Windows use `venv\Scripts\activate`


pip install -r requirements.txt
GEMINI_API_KEY=your_google_gemini_api_key
