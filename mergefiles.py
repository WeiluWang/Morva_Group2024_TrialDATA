import pandas as pd
import os

# 步骤1：读取并合并“2003_v4”文件夹下的所有CSV文件
folder_path = '2012_v4'
output_file_name = '2012.csv'
csv_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.csv')]
combined_csv = pd.concat([pd.read_csv(file) for file in csv_files])

# 步骤2：读取"tj2003-v4.csv"文件
additional_data_file = 'tj2012-v4.csv'  # 更新为您的tj2003-v4.csv文件路径
additional_data = pd.read_csv(additional_data_file)

# 确保Hiker trail name列在两个DataFrame中都存在
if 'Hiker trail name' not in combined_csv.columns:
    print("Error: 'Hiker trail name' column not found in the combined CSV.")
    exit(1)

# 步骤3：合并Trip Miles和Hiker General Journal Link数据到合并后的DataFrame中
# 使用左连接保证所有原始行都保留下来
updated_combined_csv = pd.merge(combined_csv, additional_data[['Hiker trail name', 'Trip Miles', 'Hiker Journal Link']],
                                 on='Hiker trail name', 
                                 how='left')

# 步骤4：将更新后的数据保存回"2003.csv"文件
updated_combined_csv.to_csv(output_file_name, index=False)

print(f"Update completed and saved to '{output_file_name}'.")
