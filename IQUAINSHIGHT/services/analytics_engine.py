import pandas as pd
import numpy as np

class AnalyticsEngine:
    WHO_LIMITS = {
        'pH': {'limit': '6.5 – 8.5', 'min': 6.5, 'max': 8.5, 'unit': ''},
        'Turbidity': {'limit': '< 5.0', 'min': 0, 'max': 5.0, 'unit': 'NTU'},
        'Hardness': {'limit': '< 200', 'min': 0, 'max': 200, 'unit': 'mg/L'},
        'Solids': {'limit': '< 500', 'min': 0, 'max': 500, 'unit': 'ppm'},
        'Chloramines': {'limit': '< 4.0', 'min': 0, 'max': 4.0, 'unit': 'mg/L'},
        'Sulfate': {'limit': '< 250', 'min': 0, 'max': 250, 'unit': 'mg/L'},
        'Conductivity': {'limit': '< 400', 'min': 0, 'max': 400, 'unit': 'µS/cm'},
        'Organic_Carbon': {'limit': '< 10.0', 'min': 0, 'max': 10.0, 'unit': 'ppm'},
        'Trihalomethanes': {'limit': '< 80.0', 'min': 0, 'max': 80.0, 'unit': 'µg/L'},
    }

    def compute_summary_statistics(self, df: pd.DataFrame) -> pd.DataFrame:
        """Compute statistical summary for numeric columns."""
        if df is None:
            return pd.DataFrame()
        num_df = df.select_dtypes(include=[np.number])
        summary = num_df.describe().T
        summary['median'] = num_df.median()
        summary['variance'] = num_df.var()
        summary['range'] = summary['max'] - summary['min']
        return summary[['mean', 'median', 'std', 'variance', 'min', 'max', 'range']]

    def compute_correlations(self, df: pd.DataFrame) -> pd.DataFrame:
        """Compute Pearson correlation matrix."""
        if df is None:
            return pd.DataFrame()
        num_df = df.select_dtypes(include=[np.number])
        return num_df.corr().round(2)

    def detect_outliers(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
        """Get outlier rows for a specific column."""
        if df is None or column not in df.columns:
            return pd.DataFrame()
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        return df[(df[column] < lower) | (df[column] > upper)]

    def get_who_compliance(self, df: pd.DataFrame) -> list[dict]:
        """Check compliance against WHO drinking water guidelines."""
        results = []
        if df is None:
            return results
        for param, specs in self.WHO_LIMITS.items():
            col_name = [c for c in df.columns if param.lower() in c.lower()]
            if col_name:
                avg_val = round(float(df[col_name[0]].mean()), 2)
                is_compliant = specs['min'] <= avg_val <= specs['max']
                results.append({
                    'parameter': param,
                    'unit': specs['unit'],
                    'who_limit': specs['limit'],
                    'your_avg': avg_val,
                    'status': 'Compliant' if is_compliant else 'Exceeded',
                    'is_compliant': is_compliant
                })
        return results

    def get_parameter_analysis(self, df: pd.DataFrame, parameter: str) -> dict:
        """Detailed analysis breakdown for a single parameter."""
        if df is None or parameter not in df.columns:
            return {}
        series = df[parameter].dropna()
        specs = self.WHO_LIMITS.get(parameter, {'limit': 'N/A', 'min': 0, 'max': 100, 'unit': ''})
        avg_val = float(series.mean())
        status = 'Normal' if specs['min'] <= avg_val <= specs['max'] else ('High' if avg_val > specs['max'] else 'Low')
        
        return {
            'parameter': parameter,
            'current_avg': round(avg_val, 2),
            'status': status,
            'unit': specs['unit'],
            'who_range': specs['limit'],
            'min': round(float(series.min()), 2),
            'max': round(float(series.max()), 2),
            'std': round(float(series.std()), 2),
            'median': round(float(series.median()), 2),
            'health_impact': f"{parameter} levels outside recommended guidelines can impact water aesthetics, pipe corrosion, or health.",
            'recommendation': "Parameter levels are within safe operational thresholds. Continue standard monitoring." if status == 'Normal' else "Adjust treatment dosing to restore parameter within standard WHO guidelines."
        }
