import os

class Config:
    """Configuration settings for loading datasets and fine-tuned models."""
    
    # Directory for datasets
    DATASET_DIR = os.getenv("DATASET_DIR", "datasets/")
    
    # Model configurations
    MODEL_NAME = os.getenv("MODEL_NAME", "default_model")
    MODEL_PATH = os.getenv("MODEL_PATH", "models/")
    
    # Security settings
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    
    # Logging settings
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
    
    # Other configurations can be added as needed