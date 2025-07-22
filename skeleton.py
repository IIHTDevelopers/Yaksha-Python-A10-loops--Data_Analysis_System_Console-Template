# DO NOT MODIFY: Sample Data Structures
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
    Process sales transactions using FOR loop.
    Return: Dictionary with customer sales data.
    Example: {"C1": {"total": 1500, "orders": 3}}
    """
    # TODO: Implement processing logic using for loop
    pass

def analyze_customer_tiers(customer_records):
    """
    Analyze and update customer tiers using WHILE loop.
    Tier logic: 
      - Gold: >= 1000
      - Silver: >= 500
      - Bronze: < 500
    """
    # TODO: Implement while loop to update tier in customer_records
    pass

def filter_transactions(sales_data):
    """
    Filter out only completed transactions using CONTINUE.
    Return: List of completed sales transactions.
    """
    # TODO: Use continue to skip non-completed sales
    pass

def validate_customer_data(customer_records):
    """
    Validate and return complete customer records using PASS.
    Handle invalid or incomplete records gracefully.
    """
    # TODO: Use try-except and pass to skip bad records
    pass

def generate_reports(processed_data):
    """
    Display formatted report from processed dictionary data.
    """
    # TODO: Format the output using dictionary printing
    pass

def main():
    """
    Menu-driven console program.
    """
    while True:
        print("\nData Analysis System")
        print("1. Process Sales Data")
        print("2. Analyze Customer Tiers")
        print("3. Filter Transactions")
        print("4. Validate Customer Data")
        print("5. Exit")
        
        try:
            choice = int(input("\nEnter your choice (1-5): "))

            if choice == 1:
                result = process_sales_data(sales_data)
                generate_reports(result)
            elif choice == 2:
                result = analyze_customer_tiers(customer_records.copy())
                print("\nCustomer Tiers Updated")
            elif choice == 3:
                result = filter_transactions(sales_data)
                print(f"\nCompleted Transactions: {len(result)}")
            elif choice == 4:
                result = validate_customer_data(customer_records)
                print(f"\nValid Customer Records: {len(result)}")
            elif choice == 5:
                print("Thank you for using the Data Analysis System!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
