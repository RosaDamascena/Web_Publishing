from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# 유저 생성을 위한  form이 이미 있는데 바꿔 써야 하는 이유
# 기본 제공 UsercreationForm은 model을 auth.User을 쓰고 있음
# 우리는 accounts.User를 쓸거임

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    # Meta class는 왜 상속받아서 쓰나요?
    # Meta class에서 model, field, exclude 외 다양함
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ('username', 'password')