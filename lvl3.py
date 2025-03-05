restaurant_tables = [
    [0, 'T1(2)', 'T2(4)', 'T3(2)', 'T4(6)', 'T5(4)', 'T6(2)'],  # Table names with capacities
    [1, 'o', 'o', 'o', 'o', 'o', 'o'],  # Row indicating which tables are free ('o' means open)
    [2, 'o', 'o', 'o', 'o', 'o', 'o'],  
    [3, 'o', 'o', 'o', 'o', 'o', 'o'],  
    [4, 'o', 'o', 'o', 'o', 'o', 'o'],  
    [5, 'o', 'o', 'o', 'o', 'o', 'o'],  
    [6, 'o', 'o', 'o', 'o', 'o', 'o']   
]

def find_all_tables_for_size(tables, party_size):
    """
    Level 3
    Returns a list of all table IDs that can seat 'party_size' and are free.
    """
    suitable_tables = []  # List to store suitable tables
    for i in range(1, len(tables[0])):  # Loop through each table (skip first element)
        table_info = tables[0][i]  # Get the table name (e.g., 'T1(2)')
        size_str = table_info.split('(')[1]  # Get the part in the parentheses (e.g., '2)')
        table_size = int(size_str[:-1])  # Convert the number into an integer

        if tables[1][i] == 'o' and table_size >= party_size:  # If table is free and can fit the party
            suitable_tables.append(table_info)  # Add table name to list

    return suitable_tables  # Return the list of suitable tables

# Example usage
print(find_all_tables_for_size(restaurant_tables, 4))  # Find tables that can seat at least 4 people
