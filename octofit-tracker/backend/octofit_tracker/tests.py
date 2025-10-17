from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='TestTeam')
        self.assertEqual(team.name, 'TestTeam')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='testuser', type='run', duration=10)
        self.assertEqual(activity.type, 'run')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team='TestTeam', points=100)
        self.assertEqual(leaderboard.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='TestWorkout', difficulty='Easy')
        self.assertEqual(workout.difficulty, 'Easy')

    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass')
        self.assertEqual(user.email, 'test@example.com')
