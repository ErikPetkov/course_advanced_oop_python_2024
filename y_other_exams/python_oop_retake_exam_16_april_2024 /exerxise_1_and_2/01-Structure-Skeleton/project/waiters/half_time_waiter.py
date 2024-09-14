from project.waiters.base_waiter import BaseWaiter


class HalfTimeWaiter(BaseWaiter):

    def calculate_earnings(self):
        self.total_earnings = 12.0 * self.hours_worked
        return self.total_earnings

    def report_shift(self):
        return f"{self.name} worked a half-time shift of {self.hours_worked} hours."

