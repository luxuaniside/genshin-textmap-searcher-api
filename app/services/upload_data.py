from typing import Any, Dict, List
from tqdm import tqdm
from sqlalchemy.orm import Session
# Use postgresql or sqlite dialect insert depending on your database engine
from sqlalchemy.dialects.postgresql import insert

from database.db import engine
from database.models.text_entry import TextEntry

BATCH_SIZE = 1000

def upload_data(data: List[Dict[str, Any]], version: str) -> None:
    """
    Uploads text entries to the database in batches with a progress bar,
    skipping rows that cause an 'id' primary key conflict.
    """
    total_records = len(data)
    
    with Session(engine) as session:
        with tqdm(total=total_records, desc="Uploading Data", unit="record") as pbar:
            for i in range(0, total_records, BATCH_SIZE):
                chunk = data[i : i + BATCH_SIZE]
                
                # Prepare bulk dictionary objects
                mappings = [
                    {
                        "id": text["id"],
                        "en": text["en"],
                        "chs": text["chs"],
                        "version": version,
                        "text_source": text["text_source"],
                    }
                    for text in chunk
                ]
                
                # Create the INSERT statement and specify DO NOTHING on id conflict
                stmt = insert(TextEntry).values(mappings)
                stmt = stmt.on_conflict_do_nothing(index_elements=["id"])
                
                session.execute(stmt)
                session.commit()
                
                pbar.update(len(chunk))

    print("\nUpload complete!")