from django.db import models

class Advertisement(models.Model):

    title = models.CharField("заголовок",max_length=128)
    description = models.TextField("описание")
    price = models.DecimalField("цена",max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text="Если торг уместен, то True (1), если не уместен то False (0)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ap = models.DateTimeField(auto_now=True)

    def str(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"



class Meta:
    db_table = "advertisements"