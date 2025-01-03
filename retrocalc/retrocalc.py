import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Function to calculate TP, TN, FP, FN from given metrics and cohort sizes
def calculate_confusion_matrix(pos_cohort, neg_cohort, metrics):
    # Extract values from the dictionary
    sensitivity = metrics.get('sensitivity')
    specificity = metrics.get('specificity')
    precision = metrics.get('precision')
    npv = metrics.get('npv')
    f1_score = metrics.get('f1_score')
    lr_pos = metrics.get('lr_pos')
    lr_neg = metrics.get('lr_neg')
    accuracy = metrics.get('accuracy')

    # Initialize variables for TP, TN, FP, FN
    TP = TN = FP = FN = None

    try:
        # Pair 1: Sensitivity and Specificity
        if sensitivity is not None and specificity is not None:
            TP = sensitivity * pos_cohort
            FN = pos_cohort - TP
            TN = specificity * neg_cohort
            FP = neg_cohort - TN

        # Pair 2: Sensitivity and Precision (PPV)
        elif sensitivity is not None and precision is not None:
            TP = sensitivity * pos_cohort
            FN = pos_cohort - TP
            FP = (TP * (1 - precision)) / precision
            TN = neg_cohort - FP

        # Pair 3: Sensitivity and NPV
        elif sensitivity is not None and npv is not None:
            TN = npv * FN / (1- npv)
            FP = neg_cohort - TN
            TP = sensitivity * pos_cohort
            FN = pos_cohort - TP

        # Pair 4: Sensitivity and F1 Score
        elif sensitivity is not None and f1_score is not None:
            precision = (f1_score * sensitivity) / (2 * sensitivity - f1_score)
            TP = sensitivity * pos_cohort
            FN = pos_cohort - TP
            FP = (TP * (1 - precision)) / precision
            TN = neg_cohort - FP
        # Pair 5: Specificity and Precision (PPV)
        elif specificity is not None and precision is not None:
            TN = specificity * neg_cohort
            FP = neg_cohort - TN
            TP = precision* (FP) / (1 - precision)
            FN = pos_cohort - TP


        # Pair 6: Accuracy and Sensitivity
        elif accuracy is not None and sensitivity is not None:
            TP = sensitivity * pos_cohort
            FN = pos_cohort - TP
            TN = (accuracy) * (pos_cohort + neg_cohort) - TP
            FP = neg_cohort - TN

        # Pair 7: Accuracy and Specificity
        elif accuracy is not None and specificity is not None:
            TN = specificity * neg_cohort
            FP = neg_cohort - TN
            TP = (accuracy * (pos_cohort + neg_cohort)) - TN
            FN = pos_cohort - TP

         # Pair 8: Specificity and NPV
        elif specificity is not None and npv is not None:
            TN = specificity * neg_cohort
            FP = neg_cohort - TN
            FN = (TN * (1 - npv)) / npv
            TP = pos_cohort - FN


        # Pair 9: Sensitivity and LRP
        elif sensitivity is not None and lr_pos is not None:
            specificity = 1 - (sensitivity / lr_pos)
            TP = sensitivity * pos_cohort
            FN = pos_cohort - TP
            TN = specificity * neg_cohort
            FP = neg_cohort - TN

        # Pair 10: specificity and LRP
        elif specificity is not None and lr_pos is not None:
            sensitivity = lr_pos * (1 - specificity)
            TP = sensitivity * pos_cohort
            FN = pos_cohort - TP
            TN = specificity * neg_cohort
            FP = neg_cohort - TN


        # Pair 11: Specificity and LRN
        elif specificity is not None and lr_neg is not None:
            sensitivity = 1 - (lr_neg * specificity)
            TP = sensitivity * pos_cohort
            FN = pos_cohort - TP
            TN = specificity * neg_cohort
            FP = neg_cohort - TN

        # Pair 12: Sensitivity and LRN
        elif sensitivity is not None and lr_neg is not None:
            TP = sensitivity * pos_cohort
            FN = pos_cohort - TP
            TN = ((1 - sensitivity)/ lr_neg) * neg_cohort
            FP = neg_cohort - TN

        # Check if TP, TN, FP, and FN were calculated successfully
        if TP is not None and TN is not None and FP is not None and FN is not None:
            # Round values to integers
            TP, TN, FP, FN = round(TP), round(TN), round(FP), round(FN)

            # Calculate metrics again based on rounded values
            calculated_metrics = {
                'sensitivity': round(TP / pos_cohort, 2),
                'specificity': round(TN / neg_cohort, 2),
                'precision': round(TP / (TP + FP), 2) if (TP + FP) > 0 else None,
                'npv': round(TN / (TN + FN), 2) if (TN + FN) > 0 else None,
                'f1_score': round(2 * TP / (2 * TP + FP + FN), 2) if (2 * TP + FP + FN) > 0 else None,
                'lr_pos': round((TP / (TP + FN)) / (FP / (FP + TN)), 2) if (TP + FN) > 0 and (FP + TN) > 0 else None,
                'lr_neg': round((FN / (TP + FN)) / (TN / (FP + TN)), 2) if (TP + FN) > 0 and (FP + TN) > 0 else None,
                'accuracy': round((TP + TN) / (TP + TN + FP + FN), 2) if (TP + TN + FP + FN) > 0 else None

            }
            return {'TP': TP, 'TN': TN, 'FP': FP, 'FN': FN}, calculated_metrics
        else:
            return None, "Not enough information to calculate TP, TN, FP, FN"

    except (ZeroDivisionError, TypeError) as e:
        return None, f"Error in calculation: {e}"

    pass




# Function to plot confusion matrix
def plot_confusion_matrix(confusion_values):
    TP, TN, FP, FN = confusion_values['TP'], confusion_values['TN'], confusion_values['FP'], confusion_values['FN']
    matrix = np.array([[TP, FN], [FP, TN]])

    plt.figure(figsize=(6, 5))
    sns.heatmap(matrix, annot=True, fmt=".1f", cmap="Blues", xticklabels=["Predicted Positive", "Predicted Negative"], yticklabels=["Actual Positive", "Actual Negative"])
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    pass





# Prompt user for inputs
def get_user_inputs():
    try:
        pos_cohort = float(input("Enter the positive cohort size (TP + FN): "))
        neg_cohort = float(input("Enter the negative cohort size (TN + FP): "))
    except ValueError:
        print("Invalid input for cohort sizes.")
        return None, None, None

    inputs = {}
    for metric in ['sensitivity', 'specificity', 'precision', 'npv', 'f1_score', 'lr_pos', 'lr_neg', 'accuracy']:
        try:
            value = input(f"Enter {metric.replace('_', ' ').title()}, or NA if not available: ")
            inputs[metric] = float(value) if value.strip().upper() != "NA" else None
        except ValueError:
            inputs[metric] = None

    return pos_cohort, neg_cohort, inputs

# Run the calculation
pos_cohort, neg_cohort, user_inputs = get_user_inputs()
if pos_cohort is not None and neg_cohort is not None:
    results, additional_metrics = calculate_confusion_matrix(pos_cohort, neg_cohort, user_inputs)

    if results:
        print("\nCalculated Confusion Matrix Values:")
        print("TP (True Positives):", results['TP'])
        print("TN (True Negatives):", results['TN'])
        print("FP (False Positives):", results['FP'])
        print("FN (False Negatives):", results['FN'])
        print("\nAdditional Calculated Metrics:")
        for metric, value in additional_metrics.items():
            print(f"{metric.replace('_', ' ').title()}: {value}")

        # Plot the confusion matrix
        plot_confusion_matrix(results)
    else:
        print(additional_metrics)
else:
    print("Calculation could not be completed due to insufficient inputs.")
    pass
