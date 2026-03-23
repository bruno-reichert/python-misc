from django.db.models import Sum
from tracker.models import Category

def plot_income_expenses_bar_chart(qs):
    import plotly.express as px
    
    x_vals = ['Income', 'Expenditure']
    total_income = qs.filter(type='income').aggregate(total=Sum('amount'))['total'] or 0
    total_expenses = qs.filter(type='expense').aggregate(total=Sum('amount'))['total'] or 0

    fig = px.bar(x=x_vals, y=[total_income, total_expenses])
    return fig

def plot_category_pie_chart(qs):
    import plotly.express as px

    count_per_category = qs.order_by('category').values('category').annotate(total=Sum('amount'))
    category_pks = count_per_category.values_list('category', flat=True).order_by('category')
    categories = Category.objects.filter(pk__in=category_pks).order_by('pk').values_list('name', flat=True)
    total_amounts = count_per_category.order_by('category').values_list('total', flat=True)
    fig = px.pie(values=total_amounts, names=categories)
    fig.update_layout(title_text="Total Amount by Category", title_x=0.5)
    return fig