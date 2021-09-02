from brownie import AdvancedCollectible
from scripts.helpful_scripts import fund_advanced_collectible

def main():
    advenced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    fund_advanced_collectible(advenced_collectible)
