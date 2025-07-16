
import argparse
import logging
import warnings
import os

from vertexai.preview import reasoning_engines
from vertexai import agent_engines

# Import the agent definition and configuration from other modules within the package
from .agent import root_agent
from .config import initialize_vertexai, settings

# --- Initial Setup ---
warnings.filterwarnings("ignore", category=UserWarning, module=".*pydantic.*")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def read_requirements(path="requirements.txt") -> list[str]:
    """Reads requirements from a file."""
    if not os.path.exists(path):
        logger.error(f"'{path}' not found. Please ensure it exists in the project root.")
        return []
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

def main():
    """Handles script execution for local testing or cloud deployment."""
    parser = argparse.ArgumentParser(
        description="Run the Sales Assistant Agent locally or deploy it to Agent Engine."
    )
    parser.add_argument(
        "--deploy",
        action="store_true",
        help="Deploy the agent to Google Cloud Agent Engine instead of running locally.",
    )
    args = parser.parse_args()

    # Initialize Vertex AI for both local run and deployment
    initialize_vertexai()

    if args.deploy:
        logger.info("🚀 Starting deployment to Agent Engine...")
        
        # Define deployment configuration
        requirements = read_requirements()
        if not requirements:
            logger.error("Deployment cancelled due to missing requirements file.")
            return

        # Correctly package the entire 'sales-assistant-agent' directory
        extra_packages = ["sales-assistant-agent"]

        logger.info(f"Packaging the following local directories: {extra_packages}")

        remote_app = agent_engines.create(
            agent_engine=root_agent,
            requirements=requirements,
            extra_packages=extra_packages,
            display_name="Sales Assistant Agent",
            description="An agent for checking inventory and creating orders."
        )
        logger.info("✅ Deployment successful!")
        logger.info(f"Agent Resource Name: {remote_app.resource_name}")
    else:
        logger.info("🗣️  Starting agent in local interactive mode... (Press Ctrl+C to exit)")
        # This code runs the agent locally for interactive testing
        app = reasoning_engines.AdkApp(
            agent=root_agent,
            enable_tracing=True
        )
        # Note: The AdkApp will start a local server. You will interact with it
        # via API calls, not directly in the console where you run this script.

if __name__ == "__main__":
    main()
