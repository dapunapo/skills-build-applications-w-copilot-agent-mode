from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from pymongo import MongoClient
from django.conf import settings
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connessione diretta a MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Elimina le collezioni esistenti
        for collection in ['users', 'teams', 'activity', 'leaderboard', 'workouts']:
            db[collection].drop()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', age=25),
            User(email='metalgeek@mhigh.edu', name='Tony', age=30),
            User(email='zerocool@mhigh.edu', name='Steve', age=28),
            User(email='crashoverride@mhigh.edu', name='Natasha', age=27),
            User(email='sleeptoken@mhigh.edu', name='Bruce', age=35),
        ]
        # Save users individually
        for user in users:
            user.save()

        # Create teams
        teams = [
            Team(name='Blue Team', members=[user.id for user in users[:3]]),
            Team(name='Gold Team', members=[user.id for user in users[3:]]),
        ]
        # Save teams individually
        for team in teams:
            team.save()

        # Create activities
        activities = [
            Activity(user=users[0], type='Cycling', duration=60),
            Activity(user=users[1], type='Crossfit', duration=120),
            Activity(user=users[2], type='Running', duration=90),
            Activity(user=users[3], type='Strength', duration=30),
            Activity(user=users[4], type='Swimming', duration=75),
        ]
        # Save activities individually
        for activity in activities:
            activity.save()

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=teams[0], points=100),
            Leaderboard(team=teams[1], points=90),
        ]
        # Save leaderboard entries individually
        for entry in leaderboard_entries:
            entry.save()

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        # Save workouts individually
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))