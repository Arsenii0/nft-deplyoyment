from brownie import SimpleCollectible, network
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests, json


def main():
    simple_collectible = SimpleCollectible[-1]
    token_count = simple_collectible.tokenCounter()
    for token_id in range(token_count):
        metadata_file_name = (
            f"./metadata/{network.show_active()}/ArsenCat{token_id}.json"
        )

        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"metadata already exist for {token_id}")
        else:
            collectible_metadata["name"] = "ArsenCat"
            collectible_metadata["description"] = "Great cat"
            image_file_path = "./img/ArseniiCat.png"
            image_uri = upload_to_ipfs(image_file_path)
            collectible_metadata["image"] = image_uri
            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            upload_to_ipfs(metadata_file_name)


def upload_to_ipfs(filepath):
    # rb open in binary (because image)
    with Path(filepath).open("rb") as file_path:
        image_binary = file_path.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"

        # 1 param - where to request (server url + endpoint) 2 param - post our file content
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]

        # "./img/ArseniiCat.png" -> "ArseniiCat.png"
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
