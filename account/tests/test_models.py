from django.contrib.auth import get_user_model
from django.test import TestCase


class AccountTestCase(TestCase):
	def setUp(self):
		user_model = get_user_model()
		self.u1 = user_model.objects.create_user(
			email="test@recipe-remix.tech",
			username="test",
			password="n&M0jU3@S*"
		)
		self.u1.is_admin = False
		self.u1.is_active = True
		self.u1.is_staff = False
		self.u1.save()

	def testAccountExists(self):
		user_email = get_user_model().objects.get(email="test@recipe-remix.tech").email
		self.assertEqual(user_email, "test@recipe-remix.tec")

	def tearDown(self):
		self.u1.delete()
