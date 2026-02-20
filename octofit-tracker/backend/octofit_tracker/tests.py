from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create_user(username="testuser", email="test@example.com", password="pass", team=team)
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.team.name, "Test Team")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Team A")
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create_user(username="testuser2", email="test2@example.com", password="pass")
        activity = Activity.objects.create(user=user, type="run", duration=30, distance=5.0)
        self.assertEqual(activity.type, "run")
        self.assertEqual(activity.duration, 30)
        self.assertEqual(activity.distance, 5.0)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create_user(username="testuser3", email="test3@example.com", password="pass")
        workout = Workout.objects.create(name="Pushups", description="Do 20 pushups", suggested_by=user)
        self.assertEqual(workout.name, "Pushups")
        self.assertEqual(workout.suggested_by.username, "testuser3")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create_user(username="testuser4", email="test4@example.com", password="pass")
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)
        self.assertEqual(leaderboard.user.username, "testuser4")
