from dotenv import load_dotenv
load_dotenv(override=True)

from src.pipeline.train_pipeline import TrainingPipeline

pipeline = TrainingPipeline()
result = pipeline.run_pipeline()
print("Training complete:", result)