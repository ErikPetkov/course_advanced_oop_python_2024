from project.player import Player
class Guild:
    def __init__(self,name:str):
        self.name = name
        self.players = []

    def assign_player(self,player: Player):
        if player.guild == "Unaffiliated":
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {player.guild}"
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        return f"Player {player.name} is in another guild."

    def kick_player(self,player_name: str):
        if player_name in self.players:
            self.players.remove(player_name)
            player_name:Player
            player_name.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        res = ""
        res+=f"Guild: {self.name}\n"
        for p in self.players:
            p:Player
            res+=f'{p.player_info()}\n'
        return res

