# project_tracker/models.py
from pymongo import MongoClient
from django.conf import settings
from datetime import timedelta

# Connect to MongoDB
client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]
period_tracker_collection = db["period_tracker"]

class PeriodTracker:
    @staticmethod
    def create_or_update(user_name, last_period_date, cycle_length, phone_number, sms_enabled):
        """Create or update a period tracker entry for the user."""
        period_tracker_collection.update_one(
            {"user_name": user_name},
            {
                "$set": {
                    "last_period_date": last_period_date,
                    "cycle_length": cycle_length,
                    "phone_number": phone_number,
                    "sms_enabled": sms_enabled
                }
            },
            upsert=True
        )

    @staticmethod
    def get_tracker(user_name):
        """Fetch the period tracker entry for the user."""
        return period_tracker_collection.find_one({"user_name": user_name})

    @staticmethod
    def get_all_trackers_with_sms():
        """Fetch all trackers with SMS enabled."""
        return period_tracker_collection.find({"sms_enabled": True, "phone_number": {"$ne": None}})

    @staticmethod
    def calculate_next_period(last_period_date, cycle_length):
        """Calculate the next period date."""
        from datetime import datetime
        last_date = datetime.strptime(last_period_date, "%Y-%m-%d")
        return (last_date + timedelta(days=cycle_length)).strftime("%Y-%m-%d")



