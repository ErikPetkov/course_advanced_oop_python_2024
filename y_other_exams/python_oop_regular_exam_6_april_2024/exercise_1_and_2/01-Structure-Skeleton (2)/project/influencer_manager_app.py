from typing import List
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.campaigns.base_campaign import BaseCampaign


class InfluencerManagerApp:
    VALID_INFLUENCER_TYPES = {'StandardInfluencer':StandardInfluencer,'PremiumInfluencer':PremiumInfluencer}
    VALID_CAMPAIGN_TYPES = {'HighBudgetCampaign': HighBudgetCampaign ,'LowBudgetCampaign': LowBudgetCampaign}
    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self,influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCER_TYPES.keys():
            return f"{influencer_type} is not an allowed influencer type."
        is_username = [True for i in self.influencers if i.username == username]
        # is_username = is_username[0]
        if is_username:
            return f"{username} is already registered."
        influencer = self.VALID_INFLUENCER_TYPES[influencer_type](username, followers, engagement_rate)
        self.influencers.append(influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self,campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGN_TYPES.keys():
            return f"{campaign_type} is not a valid campaign type."
        is_campaign_id = [True for c  in self.campaigns if c.campaign_id == campaign_id]
        # is_campaign_id = is_campaign_id[0]
        if is_campaign_id:
            return f"Campaign ID {campaign_id} has already been created."
        campaign = self.VALID_CAMPAIGN_TYPES[campaign_type](campaign_id,brand,required_engagement)
        self.campaigns.append(campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self,influencer_username: str, campaign_id: int):

        influencer = [i for i in self.influencers if i.username == influencer_username]

        if len(influencer) == 0:
            return f"Influencer '{influencer_username}' not found."
        influencer = influencer[0]
        campaign = [c for c in self.campaigns if c.campaign_id == campaign_id]

        if len(campaign) == 0:
            return f"Campaign with ID {campaign_id} not found."
        campaign = campaign[0]
        if not campaign.check_eligibility(influencer.engagement_rate):
            return (f"Influencer '{influencer_username}' does not meet the eligibility"
                    f" criteria for the campaign with ID {campaign_id}.")
        if influencer.calculate_payment(campaign) > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget-=influencer.calculate_payment(campaign)
            influencer.campaigns_participated.append(campaign)
            return (f"Influencer '{influencer_username}' has successfully participated in"\
                    f" the campaign with ID {campaign_id}.")

    def calculate_total_reached_followers(self):
        total_reached_follolers_dict = {}
        for c in self.campaigns:
            campaign_type = 'HighBudgetCampaign' if c.BUDGET == 5000 else "LowBudgetCampaign"
            total_reached_follolers_dict[c] = 0
            for i in c.approved_influencers:
                total_reached_follolers_dict[c]+=i.reached_followers(campaign_type)
            if total_reached_follolers_dict[c] == 0:
                del total_reached_follolers_dict[c]
        return total_reached_follolers_dict

    def influencer_campaign_report(self,username: str):
        influencer = [i for i in self.influencers if i.username == username]
        influencer = influencer[0]
        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        dict = self.calculate_total_reached_followers()
        organised_campaigns = sorted(self.campaigns, key= lambda x: (len(x.approved_influencers), -x.budget))

        result = '$$ Campaign Statistics $$\n'
        for c in organised_campaigns:
            result+=f'  * Brand: {c.brand}, Total influencers: {len(c.approved_influencers)}, ' \
                     f'Total budget: ${c.budget}, Total reached followers: {dict[c]} \n'
        return result






