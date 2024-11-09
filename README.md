
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


## Installation
No specific requirements.


# Usage


```
# clone the retrocalc into your own enviroment
!git clone https://github.com/mdnx/RetroCalc.git


%cd RetroCalc
!pip install .

# input the required metrics, remember not to use percentage (e.g. 45% incorrect, .45 correct)

from retrocalc.retrocalc import get_user_inputs


get_user_inputs()

```


# Contributing

please contact mdnrz1379@gmail.com 

# License

RetroCalc is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgments
I highly appreciate the expertise comments from proffessor Zeileis.

