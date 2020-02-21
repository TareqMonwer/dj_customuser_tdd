from django.test import TestCase
from django.contrib.auth import get_user_model


class usersMangerTest(TestCase):

  def test_create_user(self):
    User = get_user_model()
    user = User.objects.create_user(email='test@mail.com', password='testpass')
    self.assertEqual(user.email, 'test@mail.com')
    self.assertTrue(user.is_active)
    self.assertFalse(user.is_staff)
    self.assertFalse(user.is_superuser)
    try:
      # username is none (non-existance) in abstractuser
      self.assertIsNone(user.username)
    except AttributeError:
      pass
    with self.assertRaises(TypeError):
      User.objects.create_user()
    with self.assertRaises(TypeError):
      User.objects.create_user(email='')
    with self.assertRaises(ValueError):
      User.objects.create_user(email='', password='testpass')
  

  def test_create_superuser(self):
    User = get_user_model()
    admin = User.objects.create_superuser('super@admin.com', 'testsuper')
    self.assertEqual(admin.email, 'super@admin.com')
    self.assertTrue(admin.is_active)
    self.assertTrue(admin.is_staff)
    self.assertTrue(admin.is_superuser)
    try:
      # superuser username non for abstractuser
      self.assertIsNone(admin.username)
    except AttributeError:
      pass
    with self.assertRaises(ValueError):
      User.objects.create_superuser(
        email='super@admin.com', password='testsuper', is_superuser=False
      )
