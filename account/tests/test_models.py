import pytest
from django.contrib.auth import get_user_model


@pytest.mark.backend
@pytest.mark.django_db(serialized_rollback=True)
class TestAccount:

	@pytest.fixture()
	def setup(self):
		user_model = get_user_model()
		u1 = user_model.objects.create_user(
			email="test@recipe-remix.tech",
			username="test",
			password="n&M0jU3@S*"
		)
		u1.is_admin = False
		u1.is_active = True
		u1.is_staff = False
		u1.save()
		return u1

	def test_create_user(self, setup):
		user_email = get_user_model().objects.get(email="test@recipe-remix.tech").email
		assert user_email == "test@recipe-remix.tech"
