from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .models import Post, Comment, Contact



class NoteViewTests(TestCase):

	def test_note_index_page(self):
		response = self.client.get(reverse('note:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Check resources for python, django, and more ')
		u = User.objects.create_user('john', 'lennone@thebeatels.com', 'johnpassword')
		python1 = Post.objects.create(author=u, title="test lion", content="test", postcategory="python")
		python1.publish()
		response2 = self.client.get(reverse('note:python_list'))
		self.assertEqual(response2.status_code, 200)
		self.assertContains(response2, 'test lion')



