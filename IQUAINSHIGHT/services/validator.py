import pandas as pd
import numpy as np

class DataValidator:
    def validate_schema(self, df: pd.DataFrame) -> tuple[bool, list[str]]:
        """Validate if dataset contains standard water quality columns."""
        expected = ['pH', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_Carbon', 'Trihalomethanes', 'Turbidity']
        cols = [c.strip() for c in df.columns]
        missing = [c for c in expected if c not in cols]
        is_valid = len(missing) == 0
        return is_valid, missing

    def check_missing_values(self, df: pd.DataFrame) -> dict:
        """Calculate missing value counts and percentages per column."""
        if df is None:
            return {}
        total_rows = len(df)
        missing_info = {}
        for col in df.columns:
            cnt = int(df[col].isna().sum())
            pct = round((cnt / total_rows) * 100, 2) if total_rows > 0 else 0
            missing_info[col] = {'count': cnt, 'percentage': pct}
        return missing_info

    def check_duplicates(self, df: pd.DataFrame) -> int:
        """Count duplicate rows in dataframe."""
        if df is None:
            return 0
        return int(df.duplicated().sum())

    def detect_outliers_summary(self, df: pd.DataFrame) -> dict:
        """Detect outliers using IQR for numerical columns."""
        outliers = {}
        if df is None:
            return outliers
        num_cols = df.select_dtypes(include=[np.number]).columns
        for col in num_cols:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr
            count = int(((df[col] < lower) | (df[col] > upper)).sum())
            outliers[col] = count
        return outliers

    def get_data_quality_score(self, df: pd.DataFrame) -> float:
        """Compute dataset health quality score (0 - 100)."""
        if df is None or len(df) == 0:
            return 0.0
        
        # Missing factor (weight 40%)
        total_cells = df.shape[0] * df.shape[1]
        missing_cells = df.isna().sum().sum()
        missing_score = max(0, 100 - (missing_cells / total_cells * 100 * 5))
        
        # Duplicates factor (weight 30%)
        dup_cnt = df.duplicated().sum()
        dup_score = max(0, 100 - (dup_cnt / len(df) * 100 * 10))
        
        # Schema completeness (weight 30%)
        valid, missing = self.validate_schema(df)
        schema_score = 100 if valid else max(0, 100 - len(missing) * 10)
        
        overall = round(missing_score * 0.4 + dup_score * 0.3 + schema_score * 0.3, 1)
        return min(100.0, max(0.0, overall))
