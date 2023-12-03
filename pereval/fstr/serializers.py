from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .models import Users, Coords, Level, Pereval, Images


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('email', 'first_name', 'last_name', 'surname', 'phone')
        verbose_name = 'Турист'

    def save(self, **kwargs):
        self.is_valid()
        user = Users.objects.filter(email=self.validated_data.get('email'))
        if user.exists():
            return user.first()
        else:
            new_user = Users.objects.create(
                email=self.validated_data.get('email'),
                phone=self.validated_data.get('phone'),
                first_name=self.validated_data.get('first_name'),
                last_name=self.validated_data.get('last_name'),
                surname=self.validated_data.get('surname'),
            )
        return new_user


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height')
        verbose_name = 'Координаты'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('winter', 'summer', 'autumn', 'spring')
        verbose_name = 'Уровень сложности'


class ImagesSerializer(serializers.ModelSerializer):
    data = serializers.URLField()

    class Meta:
        model = Images
        fields = ('data', 'title')
        verbose_name = 'Фото'


class PerevalSerializer(WritableNestedModelSerializer):
    user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImagesSerializer(many=True)

    def validate(self, data):
        if self.instance is not None:
            instance_user = self.instance.user
            data_user = data.get('user')
            user_fields_for_validation = [
                instance_user.email != data_user['email'],
                instance_user.phone != data_user['phone'],
                instance_user.first_name != data_user['first_name'],
                instance_user.last_name != data_user['last_name'],
                instance_user.surname != data_user['surname'],
            ]
            if data_user is not None and any(user_fields_for_validation):
                raise serializers.ValidationError(
                    {
                        'Ошибка': 'Данные пользователя заменить нельзя',
                    }
                )
        return data

    class Meta:
        model = Pereval
        fields = '__all__'
        read_only_fields = ['user', ]
