# Student Performance Indicator  

This project aims to predict student performance (test scores) by analyzing various factors such as gender, ethnicity, parental level of education, lunch type, and test preparation courses. It follows the lifecycle of a typical machine learning project.

---

## Project Structure  

1. **Understanding the Problem Statement**  
   Analyze how students' test performance is influenced by various independent variables like demographic and educational factors.  
   
2. **Data Collection**  
   - Dataset: [Student Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)  
   - Dataset contains **8 columns** and **1000 rows**.  

3. **Steps in the Machine Learning Pipeline**  
   - **Data Checks:** Verify data completeness and consistency.  
   - **Exploratory Data Analysis (EDA):** Perform statistical and visual analysis to understand the data.  
   - **Data Pre-Processing:** Handle missing values, encode categorical variables, and normalize data.  
   - **Model Training:** Train different models using training data.  
   - **Choose Best Model:** Evaluate and select the best model based on performance metrics.

---

## Tools & Technologies Used  

### **Core Concepts and Utilities**  
- **Logging**: Track execution steps and debug efficiently.  
- **Pipeline**: Automate data preprocessing, transformation, and model training in a sequential manner.  
- **`setup.py`**: Package and distribute the project as a Python module.  
- **Flask**: Build a web application to serve the trained machine learning model.  

### **Scripts**  
- **`eda.py`**: Script for exploratory data analysis (EDA), including visualizations and feature understanding.  
- **`utils.py`**: Contains helper functions for data processing and common utility methods.  
- **`exception.py`**: Handles custom exceptions for better debugging and error tracking.  
- **`data_ingestion.py`**: Automates data loading and validation from source files.  
- **`data_transformation.py`**: Script for preprocessing, such as encoding, scaling, and splitting data into training and testing sets.  
- **`model_trainer.py`**: Contains logic for training machine learning models and evaluating their performance.

### **Model Deployment**  
- **Pickle**: Serialize and save the trained model for deployment or later use.

---

## Usage Instructions  

### **Setup Environment**  
1. Clone the repository:  
   ```bash
   git clone <https://github.com/1rishu0/Student-Performance-Indicator>
   cd student-performance-indicator
