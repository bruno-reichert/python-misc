from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from tracker.models import Transaction, Category

class TransactionResource(resources.ModelResource):
    category = fields.Field(
        column_name='category',
        attribute='category',
        widget=ForeignKeyWidget(Category, field='name') # type: ignore
    )

    class Meta:
        model = Transaction
        fields = ('amount', 'type', 'date', 'category')