import requests
import os

def download_tiktok_video(link, output_filename="output.mp4"):
    # URL and headers for the API
    url = "https://tiktok-scraper7.p.rapidapi.com/"
    headers = {
        "x-rapidapi-key": "2e4d95fa54mshd6782f6267c683cp119d20jsn6e6bdb07019e",
        "x-rapidapi-host": "tiktok-scraper7.p.rapidapi.com"
    }

    querystring = {"url": link, "hd": "1"}
    filename = output_filename  # Name for the downloaded file

    # Get the path to the current directory
    current_dir = os.getcwd()
    full_file_path = os.path.join(current_dir, filename)

    # Fetch the data from the API
    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        data_index = data.get('data')
        play_index = data_index.get('hdplay')
        print(play_index)
        
        if play_index is not None:
            # Stream the video content
            response1 = requests.get(play_index, stream=True)
            
            if response1.status_code == 200:
                # Open the file in write-binary mode
                with open(full_file_path, 'wb') as f:
                    # Write the content to the file in chunks
                    for chunk in response1.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                
                print(f"Video saved as {full_file_path}")
            else:
                print("Failed to download the video.")
        else:
            print("No 'hdplay' key found in the data.")
    else:
        print("Failed to fetch the data.")

if __name__ == "__main__":
    link = input("Link to video: ")
    download_tiktok_video(link)
