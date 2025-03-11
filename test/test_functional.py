import pytest
import re
from test.TestUtils import TestUtils

@pytest.fixture
def test_obj():
    return TestUtils()

def test_core_implementation(test_obj):
    """Test function definitions, variables, and loop implementations"""
    try:
        with open('data_analysis_system_console.py', 'r') as file:
            content = file.read()
        
        # Check required functions
        required_functions = [
            r'def\s+process_sales_data\s*\(\s*sales_data\s*\)',
            r'def\s+analyze_customer_tiers\s*\(\s*customer_records\s*\)',
            r'def\s+filter_transactions\s*\(\s*sales_data\s*\)',
            r'def\s+validate_customer_data\s*\(\s*customer_records\s*\)'
        ]
        
        # Check required loop patterns
        required_patterns = [
            r'for\s+.*\s+in\s+sales_data',  # FOR loop
            r'while\s+.*\s*<\s*len',  # WHILE loop
            r'continue',  # CONTINUE keyword
            r'pass'  # PASS keyword
        ]
        
        all_patterns_found = True
        missing_patterns = []
        
        for pattern in required_functions + required_patterns:
            if not re.search(pattern, content):
                all_patterns_found = False
                missing_patterns.append(pattern)
        
        test_obj.yakshaAssert("TestCoreImplementation", all_patterns_found, "functional")
        
        if not all_patterns_found:
            pytest.fail(f"Core implementation test failed: Missing patterns: {missing_patterns}")
            
    except Exception as e:
        test_obj.yakshaAssert("TestCoreImplementation", False, "functional")
        pytest.fail(f"Core implementation test failed: {str(e)}")

def test_business_logic(test_obj):
    """Test business logic of all core functions"""
    try:
        import data_analysis_system_console as app
        
        # Test process_sales_data
        sales_test = [
            {"order_id": "T1", "customer_id": "C1", "amount": 100, "status": "completed"},
            {"order_id": "T2", "customer_id": "C1", "amount": 200, "status": "completed"}
        ]
        sales_result = app.process_sales_data(sales_test)
        sales_logic_correct = (sales_result["C1"]["total"] == 300 and sales_result["C1"]["orders"] == 2)
        
        # Test analyze_customer_tiers
        tier_test = {
            "C1": {"name": "Test1", "tier": "bronze", "total_spent": 1200, "active": True},
            "C2": {"name": "Test2", "tier": "bronze", "total_spent": 600, "active": True},
            "C3": {"name": "Test3", "tier": "gold", "total_spent": 300, "active": True}
        }
        tier_result = app.analyze_customer_tiers(tier_test)
        tier_logic_correct = (
            tier_result["C1"]["tier"] == "gold" and 
            tier_result["C2"]["tier"] == "silver" and 
            tier_result["C3"]["tier"] == "bronze"
        )
        
        # Test filter_transactions
        filter_test = [
            {"order_id": "T1", "customer_id": "C1", "amount": 100, "status": "completed"},
            {"order_id": "T2", "customer_id": "C2", "amount": 200, "status": "pending"}
        ]
        filter_result = app.filter_transactions(filter_test)
        filter_logic_correct = (
            len(filter_result) == 1 and 
            filter_result[0]["status"] == "completed"
        )
        
        # Test validate_customer_data
        validate_test = {
            "C1": {"name": "Test1", "tier": "gold", "total_spent": 1000, "active": True},
            "C2": {"name": "Test2", "tier": "silver"}  # Missing fields
        }
        validate_result = app.validate_customer_data(validate_test)
        validate_logic_correct = (
            len(validate_result) == 1 and 
            "C1" in validate_result and 
            "C2" not in validate_result
        )
        
        all_logic_correct = (
            sales_logic_correct and 
            tier_logic_correct and 
            filter_logic_correct and 
            validate_logic_correct
        )
        
        test_obj.yakshaAssert("TestBusinessLogic", all_logic_correct, "functional")
        
        if not all_logic_correct:
            error_message = []
            if not sales_logic_correct:
                error_message.append("Sales calculation logic incorrect")
            if not tier_logic_correct:
                error_message.append("Tier calculation logic incorrect")
            if not filter_logic_correct:
                error_message.append("Transaction filtering logic incorrect")
            if not validate_logic_correct:
                error_message.append("Customer validation logic incorrect")
            pytest.fail(f"Business logic test failed: {', '.join(error_message)}")
            
    except Exception as e:
        test_obj.yakshaAssert("TestBusinessLogic", False, "functional")
        pytest.fail(f"Business logic test failed: {str(e)}")

def test_edge_cases(test_obj):
    """Test handling of edge cases in business logic"""
    try:
        import data_analysis_system_console as app
        
        # Test empty inputs
        assert app.process_sales_data([]) == {}, "Should handle empty sales"
        assert app.filter_transactions([]) == [], "Should handle empty transactions"
        
        # Test boundary values
        tier_edge_test = {
            "C1": {"name": "Low", "tier": "bronze", "total_spent": 499, "active": True},
            "C2": {"name": "Mid", "tier": "bronze", "total_spent": 500, "active": True},
            "C3": {"name": "High", "tier": "bronze", "total_spent": 1000, "active": True}
        }
        edge_result = app.analyze_customer_tiers(tier_edge_test)
        edge_logic_correct = (
            edge_result["C1"]["tier"] == "bronze" and 
            edge_result["C2"]["tier"] == "silver" and 
            edge_result["C3"]["tier"] == "gold"
        )
        
        test_obj.yakshaAssert("TestEdgeCases", edge_logic_correct, "functional")
        
        if not edge_logic_correct:
            pytest.fail("Edge cases test failed: Tier boundaries not handled correctly")
            
    except Exception as e:
        test_obj.yakshaAssert("TestEdgeCases", False, "functional")
        pytest.fail(f"Edge cases test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])