from django.core.management.base import BaseCommand
from course_recommendation_app.models import Course

class Command(BaseCommand):
    help = 'Populate the courses database'

    def handle(self, *args, **kwargs):
        # Define course names and their respective keywords
        courses_data = [
            {"name": "Introduction to Python", "keywords": ["python", "programming", "beginner"]},
            {"name": "Advanced Java", "keywords": ["java", "programming", "intermediate"]},
            {"name": "Programming 101", "keywords": ["programming", "beginner", "coding"]},
            {"name": "World War 2 History", "keywords": ["history", "world war 2", "military"]},
            {"name": "Political Science Fundamentals", "keywords": ["politics", "government", "political theory"]},
            {"name": "Calculus Basics", "keywords": ["mathematics", "calculus", "algebra"]},
            {"name": "Introduction to Sociology", "keywords": ["sociology", "social sciences", "society"]},
            {"name": "Data Structures and Algorithms", "keywords": ["data structures", "algorithms", "computer science"]},
            {"name": "Artificial Intelligence", "keywords": ["artificial intelligence", "machine learning", "neural networks"]},
            {"name": "European History", "keywords": ["history", "europe", "culture"]},
            {"name": "International Relations", "keywords": ["politics", "international relations", "diplomacy"]},
            {"name": "Linear Algebra", "keywords": ["mathematics", "linear algebra", "vectors"]},
            {"name": "Cultural Anthropology", "keywords": ["anthropology", "culture", "society"]},
            {"name": "Web Development Fundamentals", "keywords": ["web development", "html", "css"]},
            {"name": "Psychology 101", "keywords": ["psychology", "behavior", "mind"]},
            {"name": "Mobile App Development", "keywords": ["mobile app development", "android", "ios"]},
            {"name": "American History", "keywords": ["history", "united states", "american culture"]},
            {"name": "Game Theory", "keywords": ["mathematics", "game theory", "strategies"]},
            {"name": "Environmental Science", "keywords": ["environment", "science", "sustainability"]},
            {"name": "Digital Marketing Essentials", "keywords": ["digital marketing", "marketing", "online advertising"]},
        ]

        # Iterate through courses data and create Course objects
        for course_data in courses_data:
            course_name = course_data["name"]
            keywords = course_data["keywords"]
            course = Course.objects.create(course_name=course_name, keywords=keywords)
            course.save()

        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))
