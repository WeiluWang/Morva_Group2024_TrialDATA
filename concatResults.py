import pandas as pd


csv_files = [
    '2003.csv',
    '2004.csv',
    '2005.csv',
    '2006.csv',
    '2007.csv',
    '2008.csv',
    '2009.csv',
    '2010.csv',
    '2011.csv',
    '2012.csv'
]

# 读取并合并所有CSV文件
combined_csv = pd.concat([pd.read_csv(file) for file in csv_files])

# 将合并后的DataFrame保存为新的CSV文件
output_file_name = '03-12.csv'
combined_csv.to_csv(output_file_name, index=False)

print(f"All CSV files have been merged and saved to '{output_file_name}'.")
