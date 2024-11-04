# retrocalc.py
from utils.metrics_calculator import calculate_confusion_matrix
from utils.input_handler import get_user_inputs

def main():
    # Collect inputs
    total_positive, total_negative, metrics = get_user_inputs()
    
    # Calculate confusion matrix and other metrics
    results, additional_metrics = calculate_confusion_matrix(total_positive, total_negative, metrics)

    # Display results
    if results:
        print("\nCalculated Confusion Matrix Values:")
        print("TP (True Positives):", results['TP'])
        print("TN (True Negatives):", results['TN'])
        print("FP (False Positives):", results['FP'])
        print("FN (False Negatives):", results['FN'])
        print("\nAdditional Calculated Metrics:")
        for metric, value in additional_metrics.items():
            print(f"{metric.replace('_', ' ').title()}: {value}")
    else:
        print(additional_metrics)

if __name__ == "__main__":
    main()
