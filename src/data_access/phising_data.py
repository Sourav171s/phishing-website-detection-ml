import sys
import os
from typing import Optional, List

from pymongo import MongoClient 
import numpy as np
import pandas as pd
from src.constant import *
# Correctly import your existing MongoDBClient
from src.configuration.mongo_db_connection import MongoDBClient
from src.exception import CustomException

class PhisingData:
    "This class help to export entire mongo db record as pandas dataframe"

    def __init__(self, database_name: str):
        try:
            self.database_name = database_name
            self.mongo_url = os.getenv("MONGO_DB_URL")
            if not self.mongo_url:
                raise CustomException("MONGO_DB_URL environment variable not set.", sys)

            # Initialize your MongoDBClient here once for potential re-use
            self.mongo_client_instance = MongoDBClient(database_name=self.database_name)

        except Exception as e:
            raise CustomException(e, sys)

    def get_collection_names(self) -> List:
        """
        Gets a list of all collection names in the current MongoDB database.
        """
        try:
            # Use the established MongoDBClient instance
            collection_names = self.mongo_client_instance.database.list_collection_names()
            return collection_names
        except Exception as e:
            raise CustomException(f"Error getting collection names: {str(e)}", sys)

    def get_collection_data(self, collection_name: str, query: dict = {}) -> pd.DataFrame:
        """
        To find data in a MongoDB collection and return a dataframe of the searched data.
        PARAMS:
        query: dict, default : {} which will be fetching all data from the collection query to find the data in mongo database
        -- example of query -- {"name":"sourav"}
        """
        try:
            # Access the specific collection using your MongoDBClient instance
            collection = self.mongo_client_instance.database[collection_name]

            # Fetch all documents matching the query as a list of dictionaries
            data_list = list(collection.find(query))

            # Convert the list of dictionaries to a Pandas DataFrame
            df = pd.DataFrame(data_list)

            # Drop the "_id" column if it exists, as it's typically not needed for ML
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"])

            # Replace "na" strings with numpy.nan for consistent missing value handling
            df = df.replace({"na": np.nan})
            return df
        except Exception as e:
            raise CustomException(f"Error getting collection data for {collection_name}: {e}", sys)

    def export_collections_as_dataframe(self):
        try:
            """
            Export entire collection as dataframe:
            Yields collection_name and its corresponding Pandas DataFrame.
            """
            collections = self.get_collection_names()

            for collection_name in collections:
                df = self.get_collection_data(collection_name=collection_name)
                yield collection_name, df

        except Exception as e:
            raise CustomException(e, sys)