import pandas as pd

# Example data loading function
def load_data(detections_data, ground_truth_data):
    # Mock-up format; adjust based on actual data format
    detections = pd.DataFrame(detections_data, columns=['Type', 'Count'])
    ground_truth = pd.DataFrame(ground_truth_data, columns=['Type', 'TP', 'Total'])
    return detections, ground_truth

# Calculate metrics
def calculate_metrics(detections, ground_truth):
    results = {}
    for index, row in detections.iterrows():
        anomaly_type = row['Type']
        detected_count = row['Count']
        ground_data = ground_truth[ground_truth['Type'] == anomaly_type].iloc[0]
        tp = ground_data['TP']
        total = ground_data['Total']
        fp = detected_count - tp
        fn = total - tp
        
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / total if total > 0 else 0
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        
        results[anomaly_type] = {
            'Precision': precision,
            'Recall': recall,
            'F1-Score': f1_score
        }
    return results

# Example usage
detections_data = [{'Type': 'SHD', 'Count': 2}, {'Type': 'RXD', 'Count': 5}, {'Type': 'RYD', 'Count': 1}, {'Type': 'COR', 'Count': 2}, {'Type': 'GEN', 'Count': 16}]
ground_truth_data = [{'Type': 'SHD', 'TP': 2, 'Total': 2}, {'Type': 'RXD', 'TP': 3, 'Total': 6}, {'Type': 'RYD', 'TP': 1, 'Total': 2}, {'Type': 'COR', 'TP': 1, 'Total': 3}, {'Type': 'GEN', 'TP': 14, 'Total': 18}]

detections, ground_truth = load_data(detections_data, ground_truth_data)
results = calculate_metrics(detections, ground_truth)
print(results)
