from brownie import AdvancedCollectible, accounts, config
from scripts.helpful_scripts import get_breed
import time

STATIC_SEED = 123
def main():
    dev = accounts.add(config['wallets']['from_key'])
    advenced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    transaction = advenced_collectible.createCollectible(STATIC_SEED, "None", { 'from': dev })
    transaction.wait(2)
    requestId = transaction.events['requestedCollectible']['requestId']
    token_id = advenced_collectible.requestIdToToKenId(requestId)
    time.sleep(55)
    breed = get_breed(advenced_collectible.tokenIdToBreed(token_id))
    print('Dog breed of tokenId {} is {}'.format(token_id, breed))
