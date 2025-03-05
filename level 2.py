restaurant_tables = [
    [0, 'T1(2)', 'T2(4)', 'T3(2)', 'T4(6)', 'T5(4)', 'T6(2)'],  # Table names with capacities
    [1, 'o', 'o', 'o', 'o', 'o', 'o'],  # 'O' means open
    [2, 'o', 'o', 'o', 'o', 'o', 'o'],  
    [3, 'o', 'o', 'o', 'o', 'o', 'o'],  
    [4, 'o', 'o', 'o', 'o', 'o', 'o'],  
    [5, 'o', 'o', 'o', 'o', 'o', 'o'],  
    [6, 'o', 'o', 'o', 'o', 'o', 'o']   
]

def find_one_table_for_size(tables, party_size):
    for i in range(1, len(tables[0])):  # Start from index 1, skip first column
        table_info = tables[0][i]  # Get table name like 'T1(2)'
        size_str = table_info.split('(')[1]  # Get '2)' from 'T1(2)'
        table_size = int(size_str[:-1])  # Remove ')' to get 2

        if tables[1][i] == 'o' and table_size >= party_size:  # Check if table is free and big enough
            return table_info  # Return table names'

    return None  # Return None if no table is found


print(find_one_table_for_size(restaurant_tables, 2))  

