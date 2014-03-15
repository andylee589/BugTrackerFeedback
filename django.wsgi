import os
import sys
import django.core.handlers.wsgi
sys.path.append(r'C:/Users/Hachi/Documents/GitHub/BugTrackerFeedback')
os.environ['DJANGO_SETTINGS_MODULE'] = 'BugTrackerFeedback.settings'
application = django.core.handlers.wsgi.WSGIHandler()