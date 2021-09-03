from brownie import AdvancedCollectible, network
from meta_data import sample_metadata
from scripts.helpful_scripts import get_breed
from pathlib import Path
import os
import requests
import json

def main():
    advenced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    number_of_tokens = advenced_collectible.tokenCounter()
    print('The number of tokens you\'ve deploy is {}'.format(number_of_tokens))
    write_metadata(number_of_tokens, advenced_collectible, number_of_tokens)

def write_metadata(token_ids, nft_contract, number_of_tokens):
    for token_id in range(number_of_tokens):
        collectible_metadata = sample_metadata.metadata_template
        breed = get_breed(nft_contract.tokenIdToBreed(token_id)) 
        metadata_file_name = (
            './meta_data/{}/'.format(network.show_active()) + str(token_id)
            + '-' + breed + '.json'
        )
        #meta_data/rinkeby/0-SHIBA-INU.json
        if Path(metadata_file_name).exists():
            print('{} already found!'.format(metadata_file_name))
        else:
            print('Create meata file {}'.format(metadata_file_name))
            collectible_metadata['name'] = get_breed(nft_contract.tokenIdToBreed(token_id))
            collectible_metadata['description'] = 'An adorable {} pup!'.format(collectible_metadata['name'])
            print(collectible_metadata)
            image_to_upload = None

            if os.getenv('UPLOAD_ipfs') == 'true':
                print('hello!')
                image_path = './../../img/test.jpeg'
                image_to_upload = upload_to_ipfs(image_path)
            collectible_metadata['image'] = image_to_upload
            with open(metadata_file_name, 'w') as file:
                json.dump(collectible_metadata, file)
            if os.getenv('UPLOAD_IPFS') == 'true':
                upload_to_ipfs(metadata_file_name)

def upload_to_ipfs(filepath): 
    with Path(filepath).open('rb') as fp:
        image_binary = fp.read()
        ipfs_url = 'abc.123'
        response = requests.post(ipfs_url + '/api/v0/add', files={'file': image_binary})

        print(response.json)

        ipfs_hash = response.json()['Hash']
        filename = filepath.split('/')[-1:][0]
        print(filename)
        image_uri = 'https://ipfs.io/ipfs/{}?filename{}'.format(ipfs_hash, filename)
        print(image_uri)
        return image_uri 
    return None

     

