from datetime import datetime

# Sample data structures as per requirements
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
    if sales_data is None:
        raise TypeError("sales_data cannot be None")
    else:
        if not isinstance(sales_data, list):
            raise TypeError("sales_data must be a list")
    customer_sales = {}
    
    for sale in sales_data:
        # Check for missing required fields
        if 'order_id' not in sale or 'customer_id' not in sale or 'amount' not in sale or 'status' not in sale:
            raise KeyError("Missing required fields in sales data")
        # Validate data types
        if not isinstance(sale.get('order_id'), str):
            raise TypeError("order_id must be a string")
        if not isinstance(sale.get('customer_id'), str):
            raise TypeError("customer_id must be a string")
        if not isinstance(sale.get('amount'), (int, float)):
            raise TypeError("amount must be a number")
            
        customer_id = sale['customer_id']
        amount = sale['amount']
        status = sale['status']
        
        # Validate values
        if amount < 0:
            raise ValueError("amount cannot be negative")
        if status not in ["completed", "pending", "cancelled"]:
            raise ValueError("Invalid status value")
            
        if customer_id not in customer_sales:
            customer_sales[customer_id] = {"total": 0, "orders": 0}
            
        customer_sales[customer_id]["total"] += amount
        customer_sales[customer_id]["orders"] += 1
            
    return customer_sales

def analyze_customer_tiers(customer_records):
    """
    Analyze customer tiers using WHILE loop
    Updates customer tiers based on total spent
    """
    if customer_records is None:
        raise TypeError("customer_records cannot be None")
        
    customers = list(customer_records.items())
    i = 0
    
    while i < len(customers):
        customer_id, data = customers[i]
        
        # Check for missing required fields
        if 'name' not in data or 'tier' not in data or 'total_spent' not in data or 'active' not in data:
            raise KeyError("Missing required fields in customer data")
            
        # Validate data types
        if not isinstance(data['total_spent'], (int, float)):
            raise TypeError("total_spent must be a number")
            
        # Validate values
        if data['total_spent'] < 0:
            raise ValueError("total_spent cannot be negative")
        if data['tier'] not in ['bronze', 'silver', 'gold']:
            raise ValueError("Invalid tier value")
            
        if data['total_spent'] >= 1000:
            customer_records[customer_id]['tier'] = 'gold'
        elif data['total_spent'] >= 500:
            customer_records[customer_id]['tier'] = 'silver'
        else:
            customer_records[customer_id]['tier'] = 'bronze'
        i += 1
    
    return customer_records

def filter_transactions(sales_data):
    """
    Filter transactions using CONTINUE
    Skip processing of pending/cancelled orders
    """
    if sales_data is None:
        raise TypeError("sales_data cannot be None")
        
    completed_sales = []
    
    for transaction in sales_data:
        if transaction['status'] != 'completed':
            continue
        completed_sales.append(transaction)
    
    return completed_sales

def validate_customer_data(customer_records):
    """
    Validate customer data using PASS
    Handle incomplete data fields
    """
    if customer_records is None:
        raise TypeError("customer_records cannot be None")
        
    valid_records = {}
    
    for cust_id, data in customer_records.items():
        try:
            if not all(key in data for key in ['name', 'tier', 'total_spent', 'active']):
                pass
            else:
                valid_records[cust_id] = data
        except Exception:
            pass
            
    return valid_records

def generate_reports(processed_data):
    """Display formatted report data"""
    print("\nData Analysis System")
    print("Report Type: Sales Analysis")
    print("-" * 50)
    
    if isinstance(processed_data, dict):
        print(f"{'Customer ID':<15}{'Orders':^10}{'Total Amount':>15}")
        print("-" * 50)
        for cust_id, data in processed_data.items():
            if isinstance(data, dict):
                print(f"{cust_id:<15}{data['orders']:^10}${data['total']:>14.2f}")
            else:
                print(f"{cust_id:<15}N/A{data:>24.2f}")
    else:
        print("No data to display")

def main():
    """Main program execution"""
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