from django.test import TestCase
from django.utils import timezone
from blogengine.models import Post

class PostTest(TestCase):
	def test_create_post(self):
		#create a Post
		post = Post()

		#set the attributes
		post.title = 'My first post'
		post.text = 'This is my first blog post'
		post.pub_date = timezone.now()

		#Save import
		post.save()

		#Check we can find it 
		all_posts = Post.objects.all()
		self.assertEqual(len(all_posts), 1)
		only_post = all_posts[0]
		self.assertEquals(only_post, post)

		#Check attributes
		self.assertEquals(only_post.title, 'My first post')
		self.assertEquals(only_post.text, 'This is my first blog post')
		self.assertEquals(only_post.pub_date.day, post.pub_date.day)
		self.assertEquals(only_post.pub_date.month, post.pub_date.month)
		self.assertEquals(only_post.pub_date.hour, post.pub_date.hour)
		self.assertEquals(only_post.pub_date.minute, post.pub_date.minute)
		self.assertEquals(only_post.pub_date.second, post.pub_date.second)
