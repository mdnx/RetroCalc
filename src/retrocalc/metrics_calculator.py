# metrics_calculator.py
def calculate_confusion_matrix(total_positive, total_negative, metrics):
    sensitivity = metrics.get('sensitivity')
    specificity = metrics.get('specificity')
    precision = metrics.get('precision')
    npv = metrics.get('npv')
    f1_score = metrics.get('f1_score')
    lr_pos = metrics.get('lr_pos')
    lr_neg = metrics.get('lr_neg')
    accuracy = metrics.get('accuracy')
    
    TP = TN = FP = FN = None

    try:
        if sensitivity is not None and specificity is not None:
            TP = sensitivity * total_positive
            FN = total_positive - TP
            TN = specificity * total_negative
            FP = total_negative - TN
        elif sensitivity is not None and precision is not None:
            TP = (precision * sensitivity * (total_positive + total_negative)) / (sensitivity + precision - (sensitivity * precision))
            FP = (TP * (1 - precision)) / precision
            FN = TP * (1 - sensitivity) / sensitivity
            TN = total_negative - FP
        elif sensitivity is not None and npv is not None:
            TN = (npv * (1 - sensitivity) * (total_positive + total_negative)) / (sensitivity * (1 - npv) + npv)
            FN = (total_positive + total_negative) / (npv + sensitivity - (npv * sensitivity)) - TN
            TP = total_positive - FN
            FP = total_negative - TN
        elif accuracy is not None and sensitivity is not None:
            TP = sensitivity * total_positive
            FN = total_positive - TP
            TN = accuracy * (total_positive + total_negative) - TP
            FP = total_negative - TN
        else:
            return None, "Not enough information to calculate TP, TN, FP, FN"

        additional_metrics = {
            'sensitivity': TP / (TP + FN) if sensitivity is None else sensitivity,
            'specificity': TN / (TN + FP) if specificity is None else specificity,
            'precision': TP / (TP + FP) if precision is None else precision,
            'npv': TN / (TN + FN) if npv is None else npv,
            'f1_score': 2 * TP / (2 * TP + FP + FN) if f1_score is None else f1_score,
            'lr_pos': (TP / (TP + FN)) / (FP / (FP + TN)) if lr_pos is None else lr_pos,
            'lr_neg': (FN / (TP + FN)) / (TN / (FP + TN)) if lr_neg is None else lr_neg,
            'accuracy': (TP + TN) / (total_positive + total_negative) if accuracy is None else accuracy
        }
        
        return {'TP': TP, 'TN': TN, 'FP': FP, 'FN': FN}, additional_metrics

    except Exception as e:
        return None, f"Error in calculation: {e}"
