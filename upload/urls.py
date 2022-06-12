from django.urls import path


urlpatterns = [
    path(
        r"^uploads/$",
        views.SalesOrdersListView.as_view(),
        name="list_sales_orders",
    ),