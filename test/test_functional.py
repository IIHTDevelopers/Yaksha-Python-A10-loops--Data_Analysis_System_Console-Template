import unittest
from skeleton import *
from test.TestUtils import TestUtils


class TestExpectedValuesYaksha(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_obj = TestUtils()

        cls.sales_data = [
            {"order_id": "A1", "customer_id": "C1", "amount": 100, "status": "completed"},
            {"order_id": "A2", "customer_id": "C2", "amount": 200, "status": "pending"},
            {"order_id": "A3", "customer_id": "C1", "amount": 300, "status": "cancelled"},
            {"order_id": "A4", "customer_id": "C3", "amount": 150, "status": "completed"},
            {"order_id": "A5", "customer_id": "C2", "amount": 250, "status": "completed"}
        ]

        cls.customer_records = {
            "C1": {"name": "John", "tier": "gold", "total_spent": 1500, "active": True},
            "C2": {"name": "Alice", "tier": "silver", "total_spent": 800, "active": False},
            "C3": {"name": "Bob", "tier": "bronze", "total_spent": 300, "active": True}
        }

    def test_process_sales_data_expected(self):
        try:
            result = process_sales_data(self.sales_data)
            expected = {
                "C1": {"total": 400, "orders": 2},  # completed + cancelled included
                "C2": {"total": 450, "orders": 2},  # pending + completed
                "C3": {"total": 150, "orders": 1}
            }
            result_match = (
                result.get("C1") == {"total": 400, "orders": 2} and
                result.get("C2") == {"total": 450, "orders": 2} and
                result.get("C3") == {"total": 150, "orders": 1}
            )
            self.test_obj.yakshaAssert("TestProcessSalesDataExpected", result_match, "functional")
            print("TestProcessSalesDataExpected =", "Passed" if result_match else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestProcessSalesDataExpected", False, "functional")
            print("TestProcessSalesDataExpected = Failed | Exception:", e)

    def test_analyze_customer_tiers_expected(self):
        try:
            updated = analyze_customer_tiers(self.customer_records.copy())
            expected = {
                "C1": "gold",   # 1500
                "C2": "silver", # 800
                "C3": "bronze"  # 300
            }
            result = (
                updated["C1"]["tier"] == expected["C1"] and
                updated["C2"]["tier"] == expected["C2"] and
                updated["C3"]["tier"] == expected["C3"]
            )
            self.test_obj.yakshaAssert("TestAnalyzeCustomerTiersExpected", result, "functional")
            print("TestAnalyzeCustomerTiersExpected =", "Passed" if result else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestAnalyzeCustomerTiersExpected", False, "functional")
            print("TestAnalyzeCustomerTiersExpected = Failed | Exception:", e)

    def test_filter_transactions_expected(self):
        try:
            result = filter_transactions(self.sales_data)
            expected_orders = ["A1", "A4", "A5"]
            result_ids = [item['order_id'] for item in result]
            result_match = result_ids == expected_orders
            self.test_obj.yakshaAssert("TestFilterTransactionsExpected", result_match, "functional")
            print("TestFilterTransactionsExpected =", "Passed" if result_match else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestFilterTransactionsExpected", False, "functional")
            print("TestFilterTransactionsExpected = Failed | Exception:", e)

    def test_validate_customer_data_expected(self):
        try:
            result = validate_customer_data(self.customer_records)
            expected_keys = {"C1", "C2", "C3"}
            result_match = set(result.keys()) == expected_keys
            self.test_obj.yakshaAssert("TestValidateCustomerDataExpected", result_match, "functional")
            print("TestValidateCustomerDataExpected =", "Passed" if result_match else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestValidateCustomerDataExpected", False, "functional")
            print("TestValidateCustomerDataExpected = Failed | Exception:", e)
