from django.urls import path

from .views import *

app_name = 'store'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<int:id>', StoreMetaProductView.as_view(), name='store_meta_product'),
    path('category/<int:id>/', CategoryView.as_view(), name='category'),
    path('category/<int:c_id>/subcategory/<int:sc_id>', SubcategoryView.as_view(), name='subcategory'),
    path('category/<int:c_id>/subcategory/<int:sc_id>/meta_product/<int:mp_id>', MetaProductView.as_view(), name='meta_product'),

    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('update_item/', update_item, name="update_item"),
]
