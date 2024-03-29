from brownie import AdvancedCollectible, accounts, network, config
from scripts.helpful_scripts import fund_advanced_collectible

def main():
    dev = accounts.add(config['wallets']['from_key'])
    print(config['wallets']['from_key'])
    print(network.show_active())
    publish_source = False
    
    advenced_collectible = AdvancedCollectible.deploy(
        config['networks'][network.show_active()]['vrf_coordinator'],
        config['networks'][network.show_active()]['link_token'],
        config['networks'][network.show_active()]['keyhash'],
        { "from": dev },
        publish_source=publish_source
    )
    fund_advanced_collectible(advenced_collectible)
    return advenced_collectible

