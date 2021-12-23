from . import quest_core


class Quest:
    def __init__(self, rpc_address, logger):
        self.rpc_address = rpc_address
        self.logger = logger

    def start_quest(self, quest_address, hero_ids, attempts, private_key, nonce, gas_price_gwei, tx_timeout_seconds):
        return quest_core.start_quest(quest_address, hero_ids, attempts, private_key, nonce, gas_price_gwei, tx_timeout_seconds, self.rpc_address, self.logger)

    def complete_quest(self, hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds):
        return quest_core.complete_quest(hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, self.rpc_address, self.logger)

    def parse_complete_quest_receipt(self, tx_receipt):
        return quest_core.parse_complete_quest_receipt(tx_receipt, self.rpc_address)

    def cancel_quest(self, hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds):
        return quest_core.cancel_quest(hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, self.rpc_address, self.logger)
    
    def hero_to_quest_id(self, hero_id):
        return quest_core.hero_to_quest_id(hero_id, self.rpc_address)

    def get_active_quest(self, address):
        return quest_core.get_active_quest(address, self.rpc_address)

    def get_hero_quest(self, hero_id):
        return quest_core.get_hero_quest(hero_id, self.rpc_address)

    def get_quest(self, quest_id):
        return quest_core.get_quest(quest_id, self.rpc_address)

    def quest_address_to_type(self, quest_address):
        return quest_core.quest_address_to_type(quest_address, self.rpc_address)
    
    def get_current_stamina(self, hero_id):
        return quest_core.get_current_stamina(hero_id, self.rpc_address)
