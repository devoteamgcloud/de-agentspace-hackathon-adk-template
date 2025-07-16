from typing import Optional
from .schema import StockCheckRequest, OrderCreateRequest
from .crm_client import CrmApiClient

# Instantiate the client once to be reused by tools
api_client = CrmApiClient()

def check_product_availability(
    base_product_name: str, color: str, storage: Optional[str] = None
) -> str:
    """
    Checks the availability of a specific product variant.

    Returns:
        A JSON string of the StockCheckResponse model.
    """
    request_data = StockCheckRequest(
        base_product_name=base_product_name, color=color, storage=storage
    )
    response_data = api_client.check_availability(request_data)
    return response_data.model_dump_json()

def create_order(customer_id: str, product_id: str) -> str:
    """
    Creates a new customer order.

    Returns:
        A JSON string of the OrderCreateResponse model.
    """
    request_data = OrderCreateRequest(customer_id=customer_id, product_id=product_id)
    response_data = api_client.create_order(request_data)
    return response_data.model_dump_json()