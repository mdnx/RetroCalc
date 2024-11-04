# input_handler.py
def get_user_inputs():
    try:
        total_positive = float(input("Enter the positive cohort size (TP + FN): "))
        total_negative = float(input("Enter the negative cohort size (TN + FP): "))
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

    return total_positive, total_negative, inputs
