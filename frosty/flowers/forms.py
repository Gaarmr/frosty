from django import forms
from .models import Lot, User


class FeedbackForm(forms.Form):
    seller = forms.IntegerField(required=False)
    lot = forms.IntegerField(required=False)
    text = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        seller = cleaned_data.get('seller')
        lot = cleaned_data.get('lot')
        if not seller and not lot:
            raise forms.ValidationError(
                'Поля "Продавец" и "Лот" не могут быть оба пустыми. Заполните хотя бы одно из двух'
            )
        if seller and lot:
            raise forms.ValidationError(
                'Поля "Продавец" и "Лот" не могут быть оба заполнены. Оставить отзыв можно только на одного из двух'
            )
        return cleaned_data

    def clean_seller(self):
        seller = self.cleaned_data.get('seller')
        if not seller:
            return None
        user = User.objects.filter(id=seller, role='SL').first()
        if not user:
            raise forms.ValidationError('Нет такого продовца')
        return user

    def clean_lot(self):
        lot = self.cleaned_data.get('lot')
        if not lot:
            return None
        lot = Lot.objects.filter(id=lot).first()
        if not lot:
            raise forms.ValidationError('Нет такого лота')
        return lot
