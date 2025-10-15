# Import python dependencies
from .variables.variables import Variables
from io import StringIO
import pandas as pd

class BlobStorage:
    """
    A class to handle uploading pandas DataFrames to Azure Blob Storage.
    """

    def upload_dataframe(self, df: pd.DataFrame, file_name: str) -> None:
        """
        Upload a pandas DataFrame to blob storage as a CSV.

        Args:
            df (pd.DataFrame): The dataframe to upload.
            blob_path (str): The path within the container (e.g. 'data/fpl.csv').
        """
        vars = Variables()

        # Get a reference to the container
        blob_client = vars.blob_service_client.get_blob_client(container=vars.container_name, blob=file_name)

        # Convert DataFrame to CSV
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)

        # Upload the CSV to Blob Storage
        blob_client.upload_blob(csv_buffer.getvalue(), overwrite=True)

    def read_csv_from_blob(self, file_name: str) -> pd.DataFrame:
        """
        Read a CSV file from Azure Blob Storage into a pandas DataFrame.

        Args:
            file_name (str): The path and name of the blob (e.g. 'data/fpl.csv').

        Returns:
            pd.DataFrame: The DataFrame read from the blob.
        """
        vars = Variables()

        # Get a reference to the blob
        blob_client = vars.blob_service_client \
            .get_blob_client(container=vars.container_name, blob=file_name)

        # Download blob content as text
        try:
            download_stream = blob_client.download_blob()
            csv_data = download_stream.readall().decode('utf-8')
            df = pd.read_csv(StringIO(csv_data))
            return df

        except Exception as e:
            raise RuntimeError(f"Error reading CSV from blob '{file_name}': {e}")
