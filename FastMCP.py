from mcp.server.fastmcp import FastMCP
import pandas as pd

# יצירת שרת MCP בשם "DataAnalyzer"
mcp = FastMCP("DataAnalyzer")

@mcp.tool()
def inspect_parquet_schema(file_path: str) -> str:
    """קורא קובץ Parquet ומחזיר את רשימת העמודות וסוגי הנתונים"""
    try:
        df = pd.read_parquet(file_path)
        schema_info = df.dtypes.to_string()
        return f"The schema for {file_path} is:\n{schema_info}"
    except Exception as e:
        return f"Error reading file: {str(e)}"

if __name__ == "__main__":
    mcp.run()