from .data_downloader import update_repository
from .data_parser import combine_textmap, remove_duplicates
from services.upload_data import upload_data

def main():
    # Gets newest repo version
    update_repository()
    
    # Combines the textmap
    data = combine_textmap()
    
    # Cleans the data
    cleaned_data = remove_duplicates(data)
    # Uploads the data 
    upload_data(cleaned_data, "7.1")

if __name__ == "__main__":
    main()