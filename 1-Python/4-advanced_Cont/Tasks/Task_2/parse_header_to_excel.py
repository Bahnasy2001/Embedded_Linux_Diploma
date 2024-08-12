import re
import pandas as pd

def parse_header_file(file_path):
    # Regualar expression to match function prototypes
    prototype_pattern = re.compile(r'\b[A-Za-z_][A-Za-z0-9_]*\s+[A-Za-z_][A-Za-z0-9_]*\s*\([^)]*\)\s*(?:;|{)')
    
    with open(file_path, 'r') as file:
        content = file.read()
        
    # Find all function prototypes
    prototypes = prototype_pattern.findall(content)
    
    return prototypes

def write_to_excel(prototypes,output_path):
    # Create a Data Frame
    df = pd.DataFrame({
        'ID':[f'IDX{i}' for i in range(len(prototypes))],
        'Function Prototype': prototypes
    })
    
    # write Data Frame to excel
    df.to_excel(output_path,index=False,engine='openpyxl')
    
def main():
    # Prompt user for input and output file paths
    header_file_path = input("Enter the path to the header file: ")
    output_excel_path = input("Enter the path for the output Excel file: ")
    
    # Parse the header file
    prototypes = parse_header_file(header_file_path)
    
    # Write prototypes to Excel
    write_to_excel(prototypes, output_excel_path)
    
    print(f'Function prototypes have been written to {output_excel_path}')
    
    
if __name__ == "__main__":
    main()