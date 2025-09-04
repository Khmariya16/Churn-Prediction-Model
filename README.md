# Churn-Prediction-Model

# 📊 Telecom Customer Churn Prediction

This project predicts whether a customer will **churn** (leave the telecom service) based on their demographic and service usage patterns.  
It uses **Python (pandas, scikit-learn, matplotlib)** for data analysis and machine learning, and **Streamlit** for deployment as an interactive web app.  

---

## 🚀 Project Workflow

1. **Problem Statement**  
   A telecom company wants to reduce customer churn. The goal is to identify key churn factors and predict which customers are at risk of leaving.  

2. **Dataset**  
   The dataset contains customer details such as:  
   - Demographics (gender, senior citizen, partner, dependents)  
   - Services (Internet, Phone, Streaming, Online Security, etc.)  
   - Contract details (monthly charges, total charges, contract type, payment method, etc.)  
   - Target variable: `Churn` (Yes/No)  

3. **Steps Performed**
   - Data cleaning and preprocessing (`pandas`)  
   - Exploratory Data Analysis (EDA) using `matplotlib`  
   - Train/Validation split  
   - Feature scaling (`StandardScaler`) and categorical encoding (`OneHotEncoder`)  
   - Model training: **Logistic Regression** and **Decision Tree Classifier**  
   - Evaluation using accuracy, precision, recall, ROC-AUC  
   - Deployment with **Streamlit**  

---

## 🔑 Key Insights

- Customers with **month-to-month contracts** and **electronic check payments** are more likely to churn.  
- Higher **monthly charges** correlate with higher churn probability.  
- Senior citizens and customers without **online security/tech support** also show higher churn rates.  

---

## 🛠 Tech Stack

- **Python** (pandas, scikit-learn, matplotlib, joblib)  
- **Machine Learning** (Logistic Regression, Decision Tree)  
- **Streamlit** (for deployment)  

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/telecom-churn-prediction.git
cd telecom-churn-prediction
```

### 2️⃣ Create virtual environment & install dependencies
```python3 -m venv my_env
source my_env/bin/activate   # Mac/Linux
my_env\Scripts\activate      # Windows

pip install -r requirements.txt
```

### 3️⃣ Run Streamlit app
```
streamlit run streamlit_app.py

```
Then open the app in your browser at http://localhost:8501


## 📂 Project Structure
```
Churn/
│── Data.csv                     # Dataset
│── project.ipynb                # Jupyter notebook with EDA & model training
│── streamlit_app.py              # Streamlit web app
│── telco_churn_pipeline.joblib   # Saved ML pipeline
│── requirements.txt              # Dependencies
│── README.md                     # Project documentation

```


## 📸 Demo
<img width="1464" height="877" alt="Screenshot 2025-09-03 at 10 03 44 AM" src="https://github.com/user-attachments/assets/5797270d-2660-4d70-90f9-231ef50ef627" />


## ✅ Results
- Logistic Regression achieved ~80% accuracy.

- Decision Tree provided interpretability with feature importance.

- Streamlit app allows business users to input customer details and instantly get churn probability.


## 📌 Future Improvements
- Try advanced models (Random Forest, XGBoost, Gradient Boosting).

- Hyperparameter tuning for better accuracy.

- Integrate with a real-time telecom CRM system.


---

## ⚡Pro Tip: Add a **`requirements.txt`** file for easy setup:

```txt
streamlit
pandas
scikit-learn
matplotlib
joblib
```


## 👩‍💻 Author
Mariya Khan
B.Tech in Computer Science | Data Analyst & ML Enthusiast

📧 Contact: mariyak9122@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/mariyakhan16/
