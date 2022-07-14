from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import OrdersView, OrderView, ServicesView, \
    NewOrderView, ClientsView, ClientView, LogoutView, StatisticView, Calendar_redirectView, \
    CalendarView, DeleteOrderView, DeleteClientView, NewClientView, BabysView, BabyView, DeleteBabyView

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user_info/', LogoutView.as_view(), name='user_info'),
    path('calendar/', Calendar_redirectView.as_view(), name='calendar'),
    path('calendar/<int:year>/<str:month>', CalendarView.as_view()),
    path('clients/', ClientsView.as_view(), name='clients'),
    path('clients/new_client', NewClientView.as_view()),
    path('clients/<int:pk>', ClientView.as_view(), name='client_detail'),
    path('clients/<int:pk>/delete', DeleteClientView.as_view(), name='client_delete'),
    path('babys/', BabysView.as_view(), name='babys'),
    path('babys/<int:pk>', BabyView.as_view(), name='baby_detail'),
    path('babys/<int:pk>/delete', DeleteBabyView.as_view(), name='baby_delete'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('orders/new_order', NewOrderView.as_view()),
    path('orders/<int:pk>', OrderView.as_view(), name='order_detail'),
    path('orders/<int:pk>/delete', DeleteOrderView.as_view(), name='order_delete'),
    path('services/', ServicesView.as_view(), name='services'),
    path('statistic/', StatisticView.as_view(), name='statistic'),
]
