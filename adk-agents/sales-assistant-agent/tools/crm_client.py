import requests
import logging
from ..config import settings
from .schema import (
    StockCheckRequest, StockCheckResponse,
    OrderCreateRequest, OrderCreateResponse
)

logger = logging.getLogger(__name__)

class CrmApiClient:
    """A client for interacting with the CRM backend API."""
    def __init__(self, base_url: str = settings.API_BASE_URL):
        self.base_url = base_url

    def check_availability(self, request_data: StockCheckRequest) -> StockCheckResponse:
        """Calls the stock availability check endpoint."""
        api_url = f"{self.base_url}/inventory/check-availability"
        try:
            response = requests.post(api_url, json=request_data.model_dump())
            response.raise_for_status()
            return StockCheckResponse.model_validate(response.json())
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed for stock check: {e}")
            return StockCheckResponse(detail=f"API request failed: {e}")
        except Exception as e:
            logger.error(f"An unexpected error occurred during stock check: {e}")
            return StockCheckResponse(detail=f"An unexpected error occurred: {e}")

    def create_order(self, request_data: OrderCreateRequest) -> OrderCreateResponse:
        """Calls the order creation endpoint."""
        api_url = f"{self.base_url}/orders"
        try:
            response = requests.post(api_url, json=request_data.model_dump())
            response.raise_for_status()
            return OrderCreateResponse.model_validate(response.json())
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed for order creation: {e}")
            return OrderCreateResponse(detail=f"API request failed: {e}")
        except Exception as e:
            logger.error(f"An unexpected error occurred during order creation: {e}")
            return OrderCreateResponse(detail=f"An unexpected error occurred: {e}")