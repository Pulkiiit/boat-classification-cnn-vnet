# 🚤 Boat Types Image Classification — CNN & Transfer Learning

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1MrlMMuhv7SXHjloaKwUdtuDxpIDM5ZQ2?usp=sharing)

## 📌 Overview
This project focuses on classifying images of different **boat types** using deep learning.  
We start with a **Convolutional Neural Network (CNN)** from scratch to understand the baseline performance, finding that the network is unable to classify the images that well, then move to **transfer learning** to improve accuracy and generalization.

The dataset is sourced from **Kaggle's [Boat Types Recognition](https://www.kaggle.com/datasets/clorichel/boat-types-recognition)** and contains labeled images of various boat categories.

---

## 📂 Dataset
- **Source:** Kaggle — `clorichel/boat-types-recognition`
- **Structure:** Images organized into class-specific folders.
- **Classes:** Multiple boat types (e.g., cruise ship, ferry, kayak, sailboat, etc.).
- **Total Images:** 1462 (The dataset is skewed as well).

---

## 🛠️ Technologies Used
- **Python**
- **Google Colab**
- **Keras / TensorFlow**
- **NumPy / Pandas / Matplotlib**
- **Kaggle API** for dataset download

---

## 🚀 Project Workflow

### **1. Dataset Preparation**
- Download dataset from Kaggle using `kaggle` API.
- Extract and organize images into training, validation, and testing sets.

### **2. Baseline CNN Model**
- Build a custom **Convolutional Neural Network**.
- Train and evaluate on the dataset.
- Observation: Model accuracy was limited due to dataset complexity and fairly small CNN.

### **3. Transfer Learning**
- Apply **pre-trained models** (MobileNetV2).
- Freeze base layers, fine-tune top layers (added manually).
- Achieve significantly improved performance compared to baseline CNN.

### **4. Evaluation**
- Accuracy and loss curves plotted for training/validation.
- Final model tested on unseen data.

---

## 📊 Results
| Model               | Accuracy | Notes                               |
|---------------------|----------|-------------------------------------|
| Custom CNN          | ~26.37%     | Struggled with complex variations   |
| Transfer Learning   | ~84.47%     | Improved accuracy & generalization  |

---
