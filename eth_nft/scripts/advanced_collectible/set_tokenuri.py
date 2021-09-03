from brownie import AdvancedCollectible, accounts, network, config
from meta_data import sample_metadata
from scripts.helpful_scripts import get_breed, OPENSEA_FORMAT 

def main():
    print('Working on ' + network.show_active())
    
    advenced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    number_of_advanced_collectibles = advenced_collectible.tokenCounter()
    print('The number of tokens you\'ve deployed is ' 
            + str(number_of_advanced_collectibles))

    for token_id in range(number_of_advanced_collectibles):
        # breed = get_breed(advenced_collectible.tokenIdToBreed(token_id))
        if not advenced_collectible.tokenURI(token_id).startswith('https://'):
            setTokenURI(token_id, advenced_collectible, "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json")
        else:
            print('Skipping')


def setTokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config['wallets']['from_key'])
    nft_contract.setTokenURI(token_id, tokenURI, { 'from': dev })
    print('You can see your nft at {}'.format(OPENSEA_FORMAT.format(nft_contract.address, token_id)))
