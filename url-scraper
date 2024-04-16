import requests
from bs4 import BeautifulSoup
import os

# URL of the directory containing files to download
base_url = 'www.xyz'
 
def get_file_links(url, file_types=('.json', '.html', '.pdf', '.arrow', '.bin', '.md', '.MD', '.txt', '.safetensors', '.config', '.xml', '.csv', '.jpg', '.PNG', '.png', 'jpeg')):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    file_links = []
    directory_links = []

    for a in soup.find_all('a', href=True):
        href = a['href']
        if any(href.endswith(ft) for ft in file_types):
            full_url = requests.compat.urljoin(url, href)
            file_links.append(full_url)
        elif href.endswith('/'):
            full_url = requests.compat.urljoin(url, href)
            directory_links.append(full_url)

    return file_links, directory_links

def download_files(links, download_dir='./downloads'):
    os.makedirs(download_dir, exist_ok=True)
    for link in links:
        filename = os.path.join(download_dir, link.split('/')[-1])
        response = requests.get(link)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f'Downloaded: {filename}')
        else:
            print(f'Failed to download: {link} with status code {response.status_code}')

def traverse_directories(url, download_dir, file_types):
    print(f'Checking {url}')
    files, directories = get_file_links(url, file_types)
    print(f'Found {len(files)} files and {len(directories)} directories in {url}')
    download_files(files, download_dir)
    for directory in directories:
        new_download_dir = os.path.join(download_dir, directory.split('/')[-2])
        traverse_directories(directory, new_download_dir, file_types)

if __name__ == '__main__':
    traverse_directories(base_url, './downloads', ('.json', '.html', '.pdf', '.arrow', '.bin', '.md', '.MD', '.txt', '.safetensors', '.config', '.xml', '.csv', '.jpg', '.PNG', '.png', 'jpeg'))
