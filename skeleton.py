# DO NOT MODIFY THE SECTIONS MARKED AS "DO NOT MODIFY"
# Sample data structures - DO NOT MODIFY
sales_data = [
    {"order_id": "A1", "customer_id": "C1", "amount": 100, "status": "completed"},
    {"order_id": "A2", "customer_id": "C2", "amount": 200, "status": "pending"},
    {"order_id": "A3", "customer_id": "C1", "amount": 300, "status": "cancelled"},
    {"order_id": "A4", "customer_id": "C3", "amount": 150, "status": "completed"},
    {"order_id": "A5", "customer_id": "C2", "amount": 250, "status": "completed"}
]

customer_records = {
    "C1": {"name": "John", "tier": "gold", "total_spent": 1500, "active": True},
    "C2": {"name": "Alice", "tier": "silver", "total_spent": 800, "active": False},
    "C3": {"name": "Bob", "tier": "bronze", "total_spent": 300, "active": True}
}

product_inventory = [
    {"id": "P1", "name": "Laptop", "stock": 5, "defective": 1},
    {"id": "P2", "name": "Phone", "stock": 0, "defective": 0},
    {"id": "P3", "name": "Tablet", "stock": 3, "defective": 2}
]

def process_sales_data(sales_data):
    """
    Process sales transactions using FOR loop
    Return: Dictionary with customer sales data
    Example: {"C1": {"total": 1500, "orders": 3}}
    """
    # Validation - DO NOT MODIFY
    if not sales_data:
        return {}
    if not all(isinstance(sale, dict) for sale in sales_data):
        raise TypeError("All records must be dictionaries")
    
    # TODO: Implement the following using a FOR loop
    # 1. Create an empty dictionary for customer sales
    # 2. Loop through sales_data
    # 3. For each sale, extract customer_id, amount, and status
    # 4. Validate the data (amount >= 0, valid status)
    # 5. Add the sale to the customer's total and increment order count
    # 6. Return dictionary of customer sales
    pass

def find_top_customers(customer_records):
    """
    Analyze customer tiers using WHILE loop
    Updates customer tiers based on total spent
    """
    # Validation - DO NOT MODIFY
    if not customer_records:
        return {}
    
    # TODO: Implement the following using a WHILE loop
    # 1. Convert customer_records to a list of items
    # 2. Initialize a counter
    # 3. Process records while counter < length of customers list
    # 4. For each customer, validate their data
    # 5. Update tier based on total_spent (gold: >=1000, silver: >=500, bronze: <500)
    # 6. Increment counter
    # 7. Return updated customer records
    pass

def process_active_transactions(sales_data):
    """
    Filter transactions using CONTINUE
    Skip processing of pending/cancelled orders
    """
    # Validation - DO NOT MODIFY
    if not sales_data:
        return []
    
    # TODO: Implement the following with CONTINUE
    # 1. Create empty list for completed sales
    # 2. Loop through sales_data
    # 3. Use continue to skip non-completed transactions
    # 4. Add completed transactions to list
    # 5. Return list of completed transactions
    pass

def validate_inventory(product_inventory):
    """
    Validate inventory data using PASS
    Handle incomplete data fields
    """
    # Validation - DO NOT MODIFY
    if not product_inventory:
        return {}
    
    # TODO: Implement the following with PASS
    # 1. Create dictionary for valid inventory items
    # 2. Loop through inventory
    # 3. Use try/except block to handle potential errors
    # 4. Use pass for invalid/incomplete records
    # 5. Add valid records to the dictionary
    # 6. Return dictionary of valid inventory items
    pass

def display_report(processed_data):
    """Display formatted report data"""
    # Validation - DO NOT MODIFY
    if processed_data is None:
        print("No data to display")
        return
    
    # TODO: Implement the following
    # 1. Print report header
    # 2. Check if processed_data is a dictionary
    # 3. If it is, print column headers
    # 4. Loop through the data and print each row
    # 5. If it's not a dictionary, print appropriate message
    pass

def main():
    """Main program execution"""
    # TODO: Implement the following:
    # 1. Create a menu loop that continues until user chooses to exit
    # 2. Display menu options
    # 3. Get user choice with error handling
    # 4. Based on choice, call appropriate function and display results
    # 5. Exit when user selects the exit option
    pass

if __name__ == "__main__":
    main()