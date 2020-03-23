from django.test import TestCase
from .models import *

# Create your tests here.
class ProjectsTestCase(TestCase):
    #set up method
    def setUp(self):
        self.Chi_Gallery=Project(project_name='Chi_Gallery',project_photo='tree.png',description='some description',github_repo='git repo',url='tree.com',uploader='chinchillah')

        #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Chi_Gallery,Project))

        #Testing save method
        def test_save_method(self):
            self.Chi_Gallery.save_project()
            projects = Project.objects.all()
            self.assertTrue(len(projects) > 0)

    def setUp(self,project_name='Chi_Gallery',project_photo='tree.png',description='some description',github_repo='git repo',url='tree.com',uploader='chinchillah'):
        return Projects.objects.create(project_name=project_name, project_photo=project_photo, description=description, github_repo=github_repo, url=url, uploader=uploader)

    def projectSave(self):
        initialization = self.setUp()
        self.assertTrue(save > 0)

