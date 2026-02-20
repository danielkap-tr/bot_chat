import pandas as pd
import numpy as np

# Create a sample DataFrame
df = pd.DataFrame({
    'id': range(1, 101),
    'name': [f'Item {i}' for i in range(1, 101)],
    'value': np.random.randn(100),
    'category': np.random.choice(['A', 'B', 'C'], 100),
    'date': pd.date_range(start='2023-01-01', periods=100)
})

# Save to Parquet
output_file = 'sample.parquet'
try:
    df.to_parquet(output_file)
    print(f"Successfully created {output_file}")
except Exception as e:
    print(f"Error creating parquet file: {e}")
