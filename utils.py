# importing packages
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Box plots function for features
def box_plots_for(feature, df):
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='left', y=feature, data=df)
    plt.title(f'{feature} vs Turnover')
    plt.show()

# Create a function to ploy distribution
def histplot_employee_kde_by(feature, df, show_turnover=True, show_kde=True):
    plt.figure(figsize=(8, 4))
    if show_turnover:
        sns.histplot(x=feature, hue='left',data=df,  kde=show_kde, bins=15, palette='Set2')
        # sns.histplot(x=feature, hue='left', data=df, bins=15, palette='Set2')
        # sns.histplot(x=feature, hue='left', data=df,  bins=15, palette='Set2')
        plt.legend(title='Employee Status', labels=['Left', 'Stayed'])
    else:
        sns.histplot(x=feature, data=df, kde=show_kde, bins=15)
    plt.title(f'Distribution of Employees based on {feature}')
    # plt.xlabel(f'Number of {feature}')
    plt.ylabel('Count of Employees')
    plt.show() 

def aggregate_reports(reports):
    """Aggregate multiple classification reports into a single report."""
    aggregated_report = {}
    for key in reports[0].keys():
        if isinstance(reports[0][key], dict):
            aggregated_report[key] = {metric: np.mean([r[key][metric] for r in reports]) for metric in reports[0][key].keys()}
        else:
            aggregated_report[key] = np.mean([r[key] for r in reports])
    return aggregated_report

def plot_classification_report(report, title):
    """Plot the classification report as a heatmap."""
    df_report = pd.DataFrame(report).iloc[:-1, :].T
    plt.figure(figsize=(10, 6))
    sns.heatmap(df_report, annot=True, vmax=1, vmin=-1, center=0,cmap='vlag')
    plt.title(title)
    plt.tight_layout()
    plt.show()

def plot_confusion_matrix(y_test, y_pred, model=""):
    # Plot confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap="Blues")
    plt.title(f"{model} Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.tight_layout()
    plt.show()

def percentages_turnover_by(feature, df):
    perc = df.groupby(['left'])[feature].mean().apply(lambda x: '{:,.2f} %'.format(x * 100)).reset_index()
    df.groupby(['number_project'])['left']
    print(f"Employee's turnover % based on {feature}")
    print("-"*50)
    print(perc)    