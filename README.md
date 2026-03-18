# student-performance-predictor

## 📌 Overview

This project is a **Machine Learning-based web application** that predicts a student's **math score** based on various factors such as:

* Gender
* Parental education
* Lunch type
* Test preparation
* Reading score
* Writing score

The model is trained using **Linear Regression** and deployed as an interactive **Streamlit web app**.

---

## 🚀 Live Demo

👉 *Add your deployed Streamlit URL here*
Example: https://your-app-name.streamlit.app

---

## 🧠 Problem Statement

Educational institutions often want to understand the factors influencing student performance.
This project helps predict **math scores** using data-driven insights.

---

## ⚙️ Tech Stack

* **Programming Language:** Python
* **Libraries:**

  * Pandas
  * NumPy
  * Scikit-learn
  * Matplotlib
  * Joblib
* **Framework:** Streamlit
* **Deployment:** Streamlit Cloud

---

## 📂 Project Structure

```
student-performance-prediction
│
├── data
│   └── StudentsPerformance.csv
│
├── src
│   └── student_model.py
│
├── models
│   └── student_model.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🔍 Machine Learning Workflow

1. **Data Loading**
2. **Data Cleaning & Preprocessing**
3. **Feature Engineering**

   * One-Hot Encoding (`pd.get_dummies`)
4. **Train-Test Split**
5. **Model Training**

   * Linear Regression
6. **Model Evaluation**

   * MAE (Mean Absolute Error)
   * R² Score
7. **Model Saving**

   * Using `joblib`
8. **Deployment**

   * Streamlit Web App

---

## 📊 Model Details

* **Algorithm:** Linear Regression
* **Target Variable:** Math Score
* **Evaluation Metrics:**

  * Mean Absolute Error (MAE)
  * R² Score

---

## 🖥️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/student-performance-predictor.git
cd student-performance-predictor
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run the Streamlit app

```bash
streamlit run app.py
```

---

### 4. Open in browser

```
http://localhost:8501
```

---

## 📈 Features

* Predict student math score in real-time
* Interactive user interface
* Data-driven insights
* Lightweight and fast deployment

---

## 💡 Key Learnings

* End-to-end Machine Learning pipeline
* Data preprocessing & feature encoding
* Model training and evaluation
* Model persistence using `.pkl`
* Building ML-powered web applications
* Deploying apps using Streamlit Cloud

---

## 🔮 Future Improvements

* Add more advanced models (Random Forest, XGBoost)
* Improve UI/UX
* Add feature importance visualization
* Integrate REST API (FastAPI)
* Add real-time data input

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Gowtham S**
 Product Manager

---

⭐ If you found this project useful, please give it a star!
