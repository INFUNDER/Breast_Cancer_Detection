# Disease Prediction Project

This repository contains a set of machine learning models for predicting various diseases, including breast cancer, COVID-19, and diabetes. The models have been trained and evaluated using datasets specific to each disease, with Jupyter notebooks provided for each model's development process.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Models](#models)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The goal of this project is to create predictive models for different diseases using machine learning techniques. The current version of the project includes models for:
- Breast Cancer Prediction
- COVID-19 Prediction
- Diabetes Prediction

Each model is developed and trained using relevant datasets and stored in `.pkl` format for easy deployment and inference.

## Installation

To run this project locally, you need to have Python installed. Follow the steps below:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/INFUNDER/Disease_Prediction.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd Disease_Prediction-main
   ```
3. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

You can run the Jupyter notebooks to train the models or make predictions using the pre-trained models. The steps are as follows:

1. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```
2. **Open any of the following notebooks:**
   - `Breast_Cancer_Predection_Model_7-J.ipynb`
   - `covid_model.ipynb`
   - `diabetes.ipynb`

3. **Run the cells to train models or use the pre-trained models for predictions.**

## Project Structure

- **`Breast_Cancer_Predection_Model_7-J.ipynb`:** Notebook for breast cancer prediction.
- **`covid_model.ipynb`:** Notebook for COVID-19 prediction.
- **`diabetes.ipynb`:** Notebook for diabetes prediction.
- **`COVID-19.csv`:** Dataset for COVID-19 prediction.
- **`diabetes.csv`:** Dataset for diabetes prediction.
- **`covid_model.pkl`:** Pre-trained model for COVID-19.
- **`deb_model.pkl`:** Pre-trained model, possibly for diabetes.
- **`model.pkl`:** Generic model file, possibly for breast cancer or another disease.
- **`env`:** Virtual environment or related files.

## Models

The models included in this project are:

- **Breast Cancer Prediction Model:** A model developed to predict the likelihood of breast cancer based on medical data.
- **COVID-19 Prediction Model:** A model that predicts COVID-19 infection based on specific input features.
- **Diabetes Prediction Model:** A model for predicting the likelihood of diabetes based on relevant health data.

## Contributing

If you wish to contribute to this project, please fork the repository, create a new branch, make your changes, and submit a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

