import pandas as pd

restaurant_tables = [
    [0, 'T1(2)', 'T2(4)', 'T3(2)', 'T4(6)', 'T5(4)', 'T6(2)'],  # First row has table IDs
    [1, 'o', 'o', 'o', 'o', 'o', 'o'],  # Row 1-6: All tables are free 
    [2, 'o', 'o', 'o', 'o', 'o', 'o'],  
    [3, 'o', 'o', 'o', 'o', 'o', 'o'],  
    [4, 'o', 'o', 'o', 'o', 'o', 'o'],  
    [5, 'o', 'o', 'o', 'o', 'o', 'o'],  
    [6, 'o', 'o', 'o', 'o', 'o', 'o']   
]
df = pd.DataFrame(restaurant_tables)

def get_free_tables():
    # Check where the table is free ('o') by using vectorized operations
    free_tables = df.iloc[1:].apply(lambda x: x == 'o').any(axis=0)
    
    # Get the table IDs where the status is free ('o')
    free_table_ids = df.iloc[0, free_tables].tolist()
    
    return free_table_ids

free_tables = get_free_tables()
print(free_tables)  # Prints the table IDs that are free
