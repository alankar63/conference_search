from django.core.management.base import BaseCommand, CommandError
from vstream.models import Videoinfo as Poll
from vstream import video_search

class Command(BaseCommand):
    help = 'test command'

    def handle(self,*args,**options):
        video_search.input_video_link()

