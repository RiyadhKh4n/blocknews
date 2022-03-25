from . import views
from django.urls import path

urlpatterns = [
    path('', views.get_portfolio_list, name='get_portfolio_list'),
    path('edit/<portfolio_id>', views.edit_portfolio, name='edit_portfolio'),
    path('delete/<portfolio_id>', views.delete_portfolio, name='delete_portfolio'),
    path('create', views.create_portfolio, name='create_portfolio_url'),
    path('view/<portfolio_id>', views.get_asset_list, name='get_asset_list'),
    path('add/<portfolio_id>', views.add_asset, name='add_asset'),
    path('update/<int:pk>/<str:b_or_s>', views.update_asset, name='update_asset'),
    # path('buy/<asset_id>', views.get_asset_to_buy, name='buy_asset'),
]
