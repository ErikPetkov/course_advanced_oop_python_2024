from project.influencers.base_influencer import BaseInfluencer
from project.campaigns.base_campaign import BaseCampaign


class StandardInfluencer(BaseInfluencer):
    PAYMENT_PERCENTIGE = 0.45

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign):
        payment = float( campaign.budget * self.PAYMENT_PERCENTIGE)
        return payment

    def reached_followers(self, campaign_type: str):
        if campaign_type == "HighBudgetCampaign":
            return int(self.followers * self.engagement_rate * 1.2)
        return int(self.followers * self.engagement_rate * 0.9)
