# 🩺 Diabetes Risk Analysis

## 📌 Overview
This project explores the relationship between key health indicators and diabetes risk using a clinical dataset. The goal is to identify which factors are most strongly associated with a diabetes diagnosis and demonstrate how exploratory data analysis can generate meaningful healthcare insights.

---

## 🎯 Objective
To analyse how variables such as glucose level, BMI, age, and blood pressure relate to diabetes outcomes, and to identify the most influential risk factors.

---

## 📊 Dataset
The analysis uses the **Pima Indians Diabetes Dataset**, which includes the following variables:

- Glucose level  
- Body Mass Index (BMI)  
- Blood pressure  
- Age  
- Insulin levels  
- Diabetes outcome (0 = No, 1 = Yes)

---

## 🛠️ Methodology
The analysis followed a structured workflow:

1. **Data Inspection**
   - Checked dataset structure, size, and summary statistics  
   - Identified missing or inconsistent values  

2. **Data Cleaning**
   - Verified data integrity  
   - Handled missing values and ensured correct data types  

3. **Exploratory Data Analysis (EDA)**
   - Analysed distributions of key variables  
   - Grouped data by diabetes outcome  

4. **Correlation Analysis**
   - Calculated correlations between features and diabetes outcome  
   - Identified the strongest predictors  

5. **Visualisation**
   - Created bar charts and plots to communicate findings clearly  

---

## 📈 Key Findings

- **Glucose level** showed the strongest positive correlation with diabetes outcome  
- **BMI and age** also demonstrated moderate positive relationships  
- Individuals with diabetes had **significantly higher average glucose levels**  


---

## 💡 Key Insight
The analysis suggests that glucose level is the most significant indicator of diabetes risk within this dataset, highlighting its importance in early detection and screening.

---

## ⚙️ Tools & Technologies

- Python  
- pandas  
- matplotlib  

---

## 🚀 How to Run

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run analysis
python diabetes_analysis.py
