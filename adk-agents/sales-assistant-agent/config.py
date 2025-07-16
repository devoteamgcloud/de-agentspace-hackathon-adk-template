import os
import vertexai
from pydantic import BaseModel, Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

class AgentSettings(BaseModel):
    """Defines the agent's name and the large language model it uses."""
    name: str = Field(default="sales_assistant_agent_v2")
    model: str = Field(default="gemini-2.5-flash")

class Config(BaseSettings):
    """
    Main configuration class loading settings from a .env file.
    It uses aliases to map environment variables (e.g., GOOGLE_CLOUD_PROJECT)
    to the class attributes (e.g., CLOUD_PROJECT).
    """
    model_config = SettingsConfigDict(
        # Correctly navigate up one level to find the .env file
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env"),
        case_sensitive=False,
        extra='ignore'
    )

    agent_settings: AgentSettings = Field(default_factory=AgentSettings)

    # Google Cloud settings, loaded from the .env file using aliases.
    # Pydantic will look for the 'alias' name in the environment variables.
    CLOUD_PROJECT: str = Field(alias="GOOGLE_CLOUD_PROJECT")
    CLOUD_LOCATION: str = Field(alias="GOOGLE_CLOUD_LOCATION")

    # Backend API URL, loaded from the .env file using an alias.
    API_BASE_URL: str = Field(alias="GOOGLE_API_BASE_URL")

    @computed_field
    @property
    def STAGING_BUCKET(self) -> str:
        """Computes the staging bucket URL from the project ID after it's loaded."""
        return f"gs://{self.CLOUD_PROJECT}-adk-staging"


# Instantiate config to be used across the application
# This will raise an error if the required environment variables are not found.
settings = Config()

def initialize_vertexai():
    """Initializes the Vertex AI client with settings from config."""
    vertexai.init(
        project=settings.CLOUD_PROJECT,
        location=settings.CLOUD_LOCATION,
        staging_bucket=settings.STAGING_BUCKET
    )