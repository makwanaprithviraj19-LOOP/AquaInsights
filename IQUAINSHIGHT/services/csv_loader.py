import pandas as pd
import os
import streamlit as st
from datetime import datetime

class CSVLoader:
    DEFAULT_DATASET_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'datasets', 'water_quality_2024.csv')

    def load_file(self, uploaded_file) -> pd.DataFrame | None:
        """Load a CSV or Excel file into a pandas DataFrame."""
        if uploaded_file is None:
            return self.get_default_dataset()
        try:
            filename = uploaded_file.name
            if filename.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif filename.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(uploaded_file)
            else:
                return None
            
            st.session_state['dataset'] = df
            st.session_state['dataset_name'] = filename
            st.session_state['dataset_uploaded_at'] = datetime.now().strftime("%Y-%m-%d %H:%M")
            return df
        except Exception as e:
            st.error(f"Error loading file: {e}")
            return None

    def get_default_dataset(self) -> pd.DataFrame:
        """Get or load default water quality dataset."""
        if 'dataset' in st.session_state and st.session_state['dataset'] is not None:
            return st.session_state['dataset']
        
        if os.path.exists(self.DEFAULT_DATASET_PATH):
            df = pd.read_csv(self.DEFAULT_DATASET_PATH)
            st.session_state['dataset'] = df
            st.session_state['dataset_name'] = 'water_quality_2024.csv'
            st.session_state['dataset_uploaded_at'] = '2 hours ago'
            return df
        else:
            # Fallback mock dataframe
            df = pd.DataFrame({
                'pH': [7.18, 6.95, 7.25, 6.90, 7.45],
                'Hardness': [195.0, 204.8, 129.8, 224.9, 188.8],
                'Solids': [315.0, 20791.0, 18630.0, 19909.0, 28710.0],
                'Chloramines': [2.2, 7.33, 5.20, 7.33, 7.33],
                'Sulfate': [333.0, 312.1, 348.8, 333.4, 393.3],
                'Conductivity': [512.0, 520.5, 520.5, 611.2, 502.5],
                'Organic_Carbon': [10.2, 14.2, 12.1, 15.6, 11.4],
                'Trihalomethanes': [66.4, 73.8, 60.1, 82.3, 54.9],
                'Turbidity': [2.1, 4.2, 3.8, 4.1, 3.5],
                'Potability': [1, 1, 1, 1, 0]
            })
            st.session_state['dataset'] = df
            st.session_state['dataset_name'] = 'water_quality_2024.csv'
            st.session_state['dataset_uploaded_at'] = 'Just now'
            return df

    def validate_file(self, uploaded_file) -> tuple[bool, str]:
        """Validate the uploaded file format and size."""
        if uploaded_file is None:
            return False, "No file provided"
        if not uploaded_file.name.endswith(('.csv', '.xls', '.xlsx')):
            return False, "Unsupported file format. Please upload CSV or Excel files."
        if uploaded_file.size > 50 * 1024 * 1024:
            return False, "File size exceeds 50MB limit."
        return True, "Valid file"

    def get_file_info(self, df: pd.DataFrame) -> dict:
        """Get detailed statistics and info about loaded dataset."""
        if df is None:
            return {}
        return {
            'file_name': st.session_state.get('dataset_name', 'water_quality_2024.csv'),
            'rows': len(df),
            'cols': len(df.columns),
            'missing_percent': round(df.isna().sum().sum() / (df.shape[0] * df.shape[1]) * 100, 2),
            'duplicate_rows': int(df.duplicated().sum()),
            'memory_mb': round(df.memory_usage(deep=True).sum() / (1024 * 1024), 2),
            'uploaded_at': st.session_state.get('dataset_uploaded_at', '2 hours ago')
        }
