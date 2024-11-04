
# RetroCalc
![Build Status](https://img.shields.io/github/workflow/status/mdnx/RetroCalc/CI)
![License](https://img.shields.io/github/license/mdnx/RetroCalc)

## Description
RetroCalc is a diagnostic metrics recalculation tool designed to allow researchers to retroactively calculate confusion matrix values (TP, TN, FP, FN) and related metrics from minimal diagnostic performance data. Leveraging methodologies from the Cochrane Handbook for diagnostic tests, RetroCalc supports consistent reporting for meta-analysis and clinical research applications.

## Features
- Recalculate TP, TN, FP, FN from minimal input metrics
- Supports multiple metric pair combinations, including sensitivity and specificity, likelihood ratios, and more
- Easy integration into other Python projects or as a standalone tool
- Designed for clinical and meta-analysis applications

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Documentation](#documentation)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Installation
RetroCalc requires Python 3.6 or higher. We recommend using a virtual environment.

```bash
# Clone the repository
git clone https://github.com/mdnx/RetroCalc.git
cd RetroCalc

# Install dependencies
pip install -r requirements.txt
```
# Usage



To use RetroCalc, you can run the main script or integrate it into your own project.
```

from retrocalc.calculator import calculate_confusion_matrix
```
# Example usage
```
total_positive = 100  # TP + FN
total_negative = 120  # TN + FP
metrics = {
    'sensitivity': 0.78,
    'specificity': 0.87,
    'precision': None,
    'npv': None,
    'f1_score': None,
    'lr_pos': None,
    'lr_neg': None,
    'accuracy': None
}

results, additional_metrics = calculate_confusion_matrix(total_positive, total_negative, metrics)
print("Confusion Matrix:", results)
print("Additional Metrics:", additional_metrics)
```
# Examples

Example 1: Sensitivity and Specificity Calculation

Input:

Sensitivity: 0.85

Specificity: 0.90


Output:

Confusion Matrix: TP, TN, FP, FN

Additional Calculated Metrics: Precision, NPV, etc.

please note that at least two metrics (see manuscript for more information) along with number of participants are required. 

# Documentation

Detailed documentation for each function and module is available in the docs folder.

Testing

To run tests, make sure you have pytest installed:

pip install pytest
pytest tests/

# Contributing

please contact mdnrz1379@gmail.com 

# License

RetroCalc is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgments



