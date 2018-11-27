from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import csv
from apile_app.models import Post

class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        #parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        print("Deleting posts...")
        Post.objects.all().delete()
        with open(os.path.join(settings.BASE_DIR, 'apile_app/data', 
                                'articles.csv')) as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                
                post = Post(
                    author=row['author'],
                    title=row['title'],
                    description=row['description'],
                    slug=row['slug'],
                )
                post.save()
        print("Posts loaded successfully!")