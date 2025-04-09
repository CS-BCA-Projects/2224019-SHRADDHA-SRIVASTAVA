from pymongo import MongoClient
from django.conf import settings
from datetime import timedelta, datetime

# Connect to MongoDB
client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]
period_tracker_collection = db["period_tracker"]

class PeriodTracker:
    @staticmethod
    def create_or_update(user_name, last_period_date, cycle_length, phone_number, sms_enabled, mood=None, water_intake=None, cravings=None):
        """
        Create or update a period tracker entry for the user, including optional wellness data.
        """
        period_tracker_collection.update_one(
            {"user_name": user_name},
            {
                "$set": {
                    "last_period_date": last_period_date,
                    "cycle_length": cycle_length,
                    "phone_number": phone_number,
                    "sms_enabled": sms_enabled,
                    "mood": mood,
                    "water_intake": water_intake,
                    "cravings": cravings
                }
            },
            upsert=True
        )

    @staticmethod
    def get_tracker(user_name):
        """
        Fetch the period tracker entry for the user.
        """
        return period_tracker_collection.find_one({"user_name": user_name})

    @staticmethod
    def get_all_trackers_with_sms():
        """
        Fetch all trackers with SMS enabled and valid phone numbers.
        """
        return period_tracker_collection.find({
            "sms_enabled": True,
            "phone_number": {"$ne": None}
        })

    @staticmethod
    def calculate_next_period(last_period_date, cycle_length):
        """
        Calculate the next period date based on the last period and cycle length.
        """
        last_date = datetime.strptime(last_period_date, "%Y-%m-%d")
        next_date = last_date + timedelta(days=cycle_length)
        return next_date.strftime("%Y-%m-%d")
