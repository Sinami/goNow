from django.db import models

class UserProfile(models.model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return (self.user_id + " " + self.first_name + " | " + self.last_name + " | " + self.age + " | " + self.city + ", " + self.state)


class Trip(models.model):
    trip_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    trip_location = models.CharField(max_length=200)
    trip_start_date = models.CharField(max_length=50)
    trip_end_date = models.CharField(max_length=50)

    def __str__(self):
        return (self.trip_id + " " + self.user_id + " | " + self.trip_location + " | " + self.trip_start_date + " | " + self.trip_end_date)