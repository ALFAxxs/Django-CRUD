from .models import Book  #Serializer qilish uchun kerakli modellar imort qilinishi kerak
from rest_framework import \
    serializers  #modellarni api ga aylantirish uchun rest_frameworkdan serializer import qilinib olinadi


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"  #modeldagi barcha fieldalarni seraializer qilish uchun "__all__" ni fieldsga yuklashni ozi kifoya
        #fields = ['field1' , 'field2'] #modeldan faqat kerakli bo'lganlarni yuklash uchun field nomlarini ozini korsatish kerak
        #exclude = ['field1', 'field2'] #bu xolatda exclude da korsatilgan nomlardan boshqa hamma nomlar seraializer qilinadi
