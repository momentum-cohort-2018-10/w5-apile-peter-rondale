from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from mimesis import Person, Text, Internet, Datetime

person = Person('en')
text = Text('en')
internet = Internet()

class Command(BaseCommand):
    help = "Load testing data."

    def add_arguments(self, parser):
        #parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        from apile_app.models import Post
        from django.contrib.auth.models import User
        from mimesis import Text, Datetime

        print("Deleting users...")
        User.objects.filter(is_superuser=False).delete()

        users = []
        for x in range(40):
            user = User.objects.create_user(person.username(), person.email(), 
                                            "password")
            users.append(user)
        print("Test users created") 



        Post.objects.all().delete()
        print("Posts Wiped Out!")



        posts = []
        for y in range(40):
            post = Post(
                author=users[y],
                title=text.title(),
                description=text.sentence(),
                slug=text.word(),
            )
            post.save()
            posts.append(post)
        print("Posts loaded!")