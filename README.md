<div align="center">

# 🧠 Alzheimer's MRI Classification using VGG16 Transfer Learning

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg?style=flat&logo=tensorflow)](https://www.tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-Red.svg?style=flat&logo=keras)](https://keras.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

## 📌 Problem Statement & Motivation
Alzheimer's disease is a progressive neurologic disorder that causes the brain to shrink and brain cells to die. Early detection is crucial for better management and treatment. This project leverages Deep Learning, specifically Convolutional Neural Networks (CNNs) via Transfer Learning, to classify Brain MRI scans into four distinct severity stages of Alzheimer's disease. By automating this process, we aim to assist medical professionals in making faster and more accurate diagnoses.

## 📂 Dataset & Structure
The project uses the **Augmented Alzheimer MRI Dataset** from Kaggle.
It contains images classified into 4 classes:
- `NonDemented`
- `VeryMildDemented`
- `MildDemented`
- `ModerateDemented`

The data is split safely into:
- **70%** Training
- **15%** Validation
- **15%** Test

## ⚙️ Model Architecture
The core model is based on **VGG16**, originally trained on the ImageNet dataset.

**Architecture summary:**
- Base Model: `VGG16` (ImageNet weights, include_top=False)
- Custom Head:
  - `GlobalAveragePooling2D`
  - Fully Connected `Dense` layers with Dropout
  - Final Output Dense layer with `softmax` activation (4 classes)

**Two-Phase Training:**
1. **Phase 1 (Feature Extraction):** The base VGG16 model is frozen, and only the newly added custom classification head is trained.
2. **Phase 2 (Fine-Tuning):** The `block5_conv` layers of the VGG16 base model are unfrozen. The model is trained with a lower learning rate to closely fine-tune the deeper features specific to MRI scans.

**Key Features:**
- **Data Augmentation:** Rotation, Zoom, Horizontal Flips applied to training data.
- **Class Weights:** Used to handle class imbalances in the dataset.
- **Callbacks:** `EarlyStopping` for optimal training without overfitting.

## 📊 Results & Performance
| Metric | Score |
| --- | --- |
| **Test Accuracy** | `97.38%` |
| **Test Loss** | `0.4400` |

*(Insert your training accuracy and loss curves screenshot here, standard Markdown approach: `![Training Curves](path/to/image.png)`)*

## 🚀 How to Run in Google Colab
1. Clone this repository or download the `.ipynb` file.
2. Open [Google Colab](https://colab.research.google.com/).
3. Upload the notebook to Colab.
4. Download the dataset from Kaggle and upload it to your Colab environment (or mount your Google Drive).
5. Update the dataset paths in the notebook to point to your uploaded directories.
6. Run all cells (`Runtime > Run All`).
7. The trained model will be saved as `alzheimer_model.h5` and can be downloaded from the Colab file explorer.

## 🖼️ Sample Prediction
The notebook includes a single-image prediction function. Provide the path to a Brain MRI scan, and the model will output the predicted class along with confidence probabilities.

```python
# Pseudo-code representation of the usage
test_image_path = "dataset/test/MildDemented/sample.jpg"
predict_single_image(test_image_path, model)
# Output Example: Predicted Class: MildDemented | Confidence: 92%
```

## 👨‍💻 Author
**Peri Naga Venkata Sai Manoj**
- LinkedIn: [linkedin.com/in/manojperi26](https://www.linkedin.com/in/manojperi26)
- GitHub: [github.com/manojperi26](https://github.com/manojperi26)

---
⭐️ If you find this project helpful, please give it a star on GitHub!
