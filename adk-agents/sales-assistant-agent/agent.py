from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from .config import settings
from .instructions import GLOBAL_INSTRUCTION, INSTRUCTION
from .tools.crm_tools import check_product_availability, create_order


#TODO: Following snippet of code will help you to enable the tools that can be used by your Agent
# check_product_availability_tool=FunctionTool(func=check_product_availability),
# create_order_tool=FunctionTool(func=create_order)


# This is the main agent object that brings everything together.
# It is imported by main.py for execution or deployment.
root_agent = Agent(
    name=settings.agent_settings.name,
    model=settings.agent_settings.model,
    global_instruction=GLOBAL_INSTRUCTION,
    instruction=INSTRUCTION,
    tools=[
        #TODO: Add your functional tools here for checking availability of products and create orders. 
    ]
)
