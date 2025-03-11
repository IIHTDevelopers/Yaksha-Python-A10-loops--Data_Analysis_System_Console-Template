import pytest
from test.TestUtils import TestUtils

@pytest.fixture
def test_obj():
    return TestUtils()

def test_input_validation(test_obj):
    """Test handling of invalid inputs (types, missing fields, values)"""
    try:
        import data_analysis_system_console as app
        
        # Test null inputs
        with pytest.raises(TypeError):
            app.process_sales_data(None)
        
        with pytest.raises(TypeError):
            app.analyze_customer_tiers(None)
        
        # Test invalid data types
        invalid_sales = [
            {"order_id": 123,  # Should be string
             "customer_id": "C1",
             "amount": "100",  # Should be number
             "status": "completed"
            }
        ]
        
        with pytest.raises((TypeError, ValueError)):
            app.process_sales_data(invalid_sales)
        
        # Test missing fields
        incomplete_sales = [
            {"order_id": "A1", "customer_id": "C1"}  # Missing amount and status
        ]
        
        with pytest.raises(KeyError):
            app.process_sales_data(incomplete_sales)
        
        # Test invalid values
        invalid_values = [
            {"order_id": "A1", "customer_id": "C1", "amount": -100, "status": "completed"},  # Negative amount
            {"order_id": "A2", "customer_id": "C1", "amount": 100, "status": "invalid"}  # Invalid status
        ]
        
        with pytest.raises(ValueError):
            app.process_sales_data(invalid_values)
        
        test_obj.yakshaAssert("TestInputValidation", True, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestInputValidation", False, "exception")
        pytest.fail(f"Input validation test failed: {str(e)}")

def test_customer_data_validation(test_obj):
    """Test validation of customer data"""
    try:
        import data_analysis_system_console as app
        
        # Test invalid customer data
        invalid_customers = {
            "C1": {"name": "Test", 
                   "tier": "invalid",  # Invalid tier
                   "total_spent": -1000,  # Negative spent
                   "active": True}
        }
        
        with pytest.raises(ValueError):
            app.analyze_customer_tiers(invalid_customers)
        
        # Test missing fields in customer data
        incomplete_customers = {
            "C1": {"name": "Test"}  # Missing tier, total_spent, active
        }
        
        with pytest.raises(KeyError):
            app.analyze_customer_tiers(incomplete_customers)
        
        # Test validate_customer_data function
        mixed_customers = {
            "C1": {"name": "Test", "tier": "bronze", "total_spent": 100, "active": True},  # Valid
            "C2": {"name": "Test2"}  # Invalid
        }
        
        result = app.validate_customer_data(mixed_customers)
        assert len(result) == 1, "Should only return valid customer records"
        assert "C1" in result, "Should include valid records"
        assert "C2" not in result, "Should exclude invalid records"
        
        test_obj.yakshaAssert("TestCustomerDataValidation", True, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestCustomerDataValidation", False, "exception")
        pytest.fail(f"Customer data validation test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])