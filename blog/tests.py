from django.test import TestCase
from django.urls import reverse
from.models import Post, Author
# Create your tests here.
class BlogTest(TestCase):
  
  def setUp(self):
    
    self.author = Author.objects.create(
      name = "Author"
      )
    
    self.post = Post.objects.create(
      title = "Blog Title",
      author = self.author,
      content = "This is the content"
    )
    
  def test_post_model(self):
    post_title = f"{self.post.title}"
    post_content = f"{self.post.content}"
    
    self.assertEqual(post_title, "Blog Title")
    self.assertEqual(self.author.name, "Author")
    self.assertEqual(post_content, self.post.content)
    
  def test_post_model_str(self):
    self.assertEqual(str(self.post), self.post.title)
    
  def test_get_absolute_url(self):
    self.assertEqual (self.post.get_absolute_url(), "/post/1/")
    
  def test_list_view(self):
    response = self.client.get(reverse("home"))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Blog Title")
    self.assertTemplateUsed(response, "home.html")
    
  def test_detail_view(self):
    response = self.client.get("/post/1/")
    no_response = self.client.get("/post/1000/")
    self.assertEqual(response.status_code, 200)
    self.assertEqual(no_response.status_code, 404)
    self.assertContains(response, "Blog Title")
    self.assertTemplateUsed(response, "post.html")
    
  def test_create_view(self):
    response = self.client.post(reverse("new"), {
      "title" : "The title",
      "author" : self.author,
      "content" : "the content"
    })
    
  def test_update_view(self):
    response = self.client.post(reverse("update", args=[str(1)]), {
      "title" : "the title",
      "content" : "the content"
    }
    )
    
    self.assertEqual(response.status_code, 302)
     

    
  def test_delete_view(self):
    response = self.client.get(reverse("delete", args=[1]) )
    self.assertEqual(response.status_code, 200)
    
    
class AuthorModelTest(TestCase):
  
  def setUp(self):
    self.author = Author.objects.create(
      name = "Author"
      )
      
  def test_author_model(self):
    self.assertEqual(self.author.name, "Author")
  
  def test_author_str(self):
    self.assertEqual(str(self.author), "Author")
    
