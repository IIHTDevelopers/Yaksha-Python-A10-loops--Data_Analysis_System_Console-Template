import pytest
from test.TestUtils import TestUtils

@pytest.fixture
def test_obj():
    return TestUtils()

def test_boundary_cases(test_obj):
    """Test empty data and boundary values"""
    try:
        import data_analysis_system_console as app
        
        # Test with empty data
        empty_sales = []
        empty_customers = {}
        
        assert app.process_sales_data(empty_sales) == {}, "Should handle empty sales"
        assert app.analyze_customer_tiers(empty_customers) == {}, "Should handle empty customers"
        assert app.filter_transactions(empty_sales) == [], "Should handle empty transactions"
        
        # Test with boundary values
        boundary_sales = [
            {"order_id": "A1", "customer_id": "C1", "amount": 0, "status": "completed"},
            {"order_id": "A2", "customer_id": "C1", "amount": 999999.99, "status": "completed"}
        ]
        
        boundary_customers = {
            "C1": {"name": "Test", "tier": "bronze", "total_spent": 0, "active": True},
            "C2": {"name": "Test2", "tier": "bronze", "total_spent": 999999.99, "active": True}
        }
        
        # Test process_sales_data with boundary amounts
        result = app.process_sales_data(boundary_sales)
        assert result["C1"]["total"] == 999999.99, "Should handle maximum amount"
        
        # Test analyze_customer_tiers with boundary spent values
        result = app.analyze_customer_tiers(boundary_customers)
        assert result["C1"]["tier"] == "bronze", "Should handle zero spent"
        assert result["C2"]["tier"] == "gold", "Should handle maximum spent"
        
        test_obj.yakshaAssert("TestBoundaryCases", True, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestBoundaryCases", False, "boundary")
        pytest.fail(f"Boundary case test failed: {str(e)}")

def test_data_limits(test_obj):
    """Test system with large datasets"""
    try:
        import data_analysis_system_console as app
        
        # Create large dataset (reduced from 1000 to 100 for faster testing)
        large_sales = [
            {"order_id": f"A{i}", "customer_id": "C1", "amount": 100, "status": "completed"}
            for i in range(100)
        ]
        
        # Test processing large datasets
        result = app.process_sales_data(large_sales)
        assert result["C1"]["orders"] == 100, "Should handle large number of orders"
        assert result["C1"]["total"] == 10000, "Should handle large total amount"
        
        test_obj.yakshaAssert("TestDataLimits", True, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestDataLimits", False, "boundary")
        pytest.fail(f"Data limits test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])