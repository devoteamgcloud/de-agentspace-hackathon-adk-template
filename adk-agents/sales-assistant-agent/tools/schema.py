from typing import Optional
from pydantic import BaseModel

class StockCheckRequest(BaseModel):
    """Request body for the /inventory/check-availability endpoint."""
    base_product_name: str
    color: str
    storage: Optional[str] = None

class StockCheckResponse(BaseModel):
    """Response from the /inventory/check-availability endpoint."""
    product_id: Optional[str] = None
    requested_variant: Optional[str] = None
    available_stock: Optional[int] = None
    detail: Optional[str] = None

class OrderCreateRequest(BaseModel):
    """Request body for the POST /orders endpoint."""
    customer_id: str
    product_id: str

class OrderCreateResponse(BaseModel):
    """Response from the POST /orders endpoint."""
    message: Optional[str] = None
    sale_id: Optional[str] = None
    inventory_item_id: Optional[str] = None
    product_id: Optional[str] = None
    detail: Optional[str] = None