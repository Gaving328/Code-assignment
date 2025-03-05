# def a function to check if the table is available
# make is check the firt row since thats where if it is taken or not
# 





restaurant_tables = [
    [0, 'T1(2)', 'T2(4)', 'T3(2)', 'T4(6)', 'T5(4)', 'T6(2)'],  # First row has table IDs
    [1, 'o', 'o', 'o', 'o', 'o', 'o'],  # Row 1-6: All tables are free 
    [2, 'o', 'o', 'o', 'o', 'o', 'o'],  
    [3, 'o', 'o', 'o', 'o', 'o', 'o'],  
    [4, 'o', 'o', 'o', 'o', 'o', 'o'],  
    [5, 'o', 'o', 'o', 'o', 'o', 'o'],  
    [6, 'o', 'o', 'o', 'o', 'o', 'o']   
]

def get_free_tables(tables):
    free_tables = []
    for i in range(1, len(tables[1])):  # Starts from the first row
        if tables[1][i] == 'o':  # Check if the table is free
            free_tables.append(tables[0][i])  # Add the table ID from the first row
    return free_tables


free_tables = get_free_tables(restaurant_tables) 
print(free_tables) # Prints the tables with the letter 'o'