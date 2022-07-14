from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render
from extra_views import ModelFormSetView
import calendar
from .forms import OrderForm, ClientForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import DetailView, UpdateView, CreateView, ListView, DeleteView
from .models import Orders, Services, Clients, Babys
from django.urls import reverse_lazy
from calendar import HTMLCalendar
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from itertools import groupby
from django.utils.html import conditional_escape as esc

PAGINATE = 12

# Create your views here.
class BabysView(ListView):
    model = Babys
    template_name = 'babys_list.html'
    paginate_by = PAGINATE
    context_object_name = 'babys'

    # def get_context_data(self, **kwargs):
    #     context = super(BabysView, self).get_context_data(**kwargs)
    #     context["babys"] = Babys.objects.all().order_by(F('bith').desc(nulls_last=True))
    #     return context

    def get_queryset(self):
        return Babys.objects.all().order_by(F('bith').desc(nulls_last=True))


class BabyView(UpdateView):
    model = Babys
    # form_class = BabyForm
    fields = '__all__'
    template_name = 'baby.html'
    context_object_name = 'baby'

    def get_success_url(self):
        return reverse_lazy('baby_detail', kwargs={'pk': self.object.pk})

class NewBabyView(CreateView):
    model = Babys
    # form_class = ClientForm
    fields = '__all__'
    template_name = 'baby.html'
    context_object_name = 'baby'

    def get_success_url(self):
        return reverse_lazy('baby_detail', kwargs={'pk': self.object.pk})


class DeleteBabyView(DeleteView):
    model = Babys
    success_url = '../'

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

class Calendar_redirectView(RedirectView):
    now = date.today()
    year = now.year
    month = calendar.month_name[now.month]
    url = f'{year}/{month}'


class OrdersCalendar(HTMLCalendar):
    def __init__(self, orders):
        super(OrdersCalendar, self).__init__()
        self.orders = self.group_by_day(orders)
        self.firstweekday = 0

    def group_by_day(self, orders):
        field = lambda order: order.date.day
        return dict(
            [(day, list(items)) for day, items in groupby(orders, field)]
        )

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(OrdersCalendar, self).formatmonth(year, month)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if day in self.orders:
                cssclass += ' active'
                body = [f'<div id="info_{day}" style="display: none;"><b><p>{day}.{self.month}.{self.year}</p></b>']
                for order in self.orders[day]:
                    body.append('<p>')
                    body.append('<a href="%s">' % order.get_url())
                    body.append(esc(order.service.name))
                    body.append('</a></p>')
                body.append('</div>')
                return self.day_cell(day, cssclass, ''.join(body))
            return self.day_cell(0, cssclass, day)
        return self.day_cell(0, 'noday', '&nbsp;')

    def day_cell(self, day, cssclass, body):
        if day:
            return f'<td class="%s" onclick="Show_data(\'%s\')">%s %s</td>' % (cssclass, day, day, body)
        return f'<td class="%s">%s</td>' % (cssclass, body)

class CalendarView(TemplateView):
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        month_number = list(calendar.month_name).index(self.kwargs['month'].capitalize())
        orders = Orders.objects.order_by('date').filter(
            date__year=self.kwargs['year'], date__month=month_number
        )
        calend = OrdersCalendar(orders).formatmonth(self.kwargs['year'], month_number)

        Begindate = datetime.strptime(f"{self.kwargs['year']}-{month_number}", "%Y-%m")
        Prewdate = Begindate - relativedelta(months=1)
        Nextdate = Begindate + relativedelta(months=1)

        context = {
            'year': self.kwargs['year'],
            'month': self.kwargs['month'],
            'calend': calend,
            'prew_year': Prewdate.year,
            'prew_month': calendar.month_name[Prewdate.month],
            'next_year': Nextdate.year,
            'next_month': calendar.month_name[Nextdate.month]
        }
        return context

class StatisticView(TemplateView):
    template_name = 'home.html'

class LogoutView(LogoutView):
    next_page = '/admin/'

# CLIENTS
class ClientsView(ListView):

    model = Clients
    template_name = 'clients_list.html'
    paginate_by = PAGINATE
    context_object_name = 'clients'

    def get_queryset(self):
        return Clients.objects.all().order_by('name', 'surname')


class ClientView(UpdateView):
    model = Clients
    form_class = ClientForm
    template_name = 'client.html'
    context_object_name = 'client'

    def get_success_url(self):
        return reverse_lazy('client_detail', kwargs={'pk': self.object.pk})


class NewClientView(CreateView):
    model = Clients
    form_class = ClientForm
    template_name = 'client.html'
    context_object_name = 'client'

    def get_success_url(self):
        return reverse_lazy('client_detail', kwargs={'pk': self.object.pk})


class DeleteClientView(DeleteView):
    model = Clients
    success_url = '../'

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)


# ORDERS
class OrdersView(ListView):
    # a = Orders.objects.all()
    # for i in a:
    #     if i.service == 13:
    #         i.service = 5
    #         i.save()
        # try:
        #     j = Clients.objects.get(id = i.client)
        #     print(j.name)
        # except:
            # print("NO {}".format(i.client))
            # i.delete()
        #
        #     i.client = 3
        #     i.save()
        #

    model = Orders
    template_name = 'orders_list.html'
    paginate_by = PAGINATE
    context_object_name = 'orders'

    def get_queryset(self):
        return Orders.objects.all().order_by('status', '-date')
# .order_by('name', 'surname')

class OrderView(UpdateView):
    model = Orders
    form_class = OrderForm
    template_name = 'order.html'
    context_object_name = 'order'

    def get_success_url(self):
        return reverse_lazy('order_detail', kwargs={'pk': self.object.pk})


class NewOrderView(CreateView):
    model = Orders
    form_class = OrderForm
    template_name = 'order.html'
    context_object_name = 'order'

    def get_success_url(self):
        return reverse_lazy('order_detail', kwargs={'pk': self.object.pk})


class DeleteOrderView(DeleteView):
    model = Orders
    success_url = '../'

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)


# SERVISES

class ServicesView(UpdateView):
    model = Services
    # form_class = ServiceForm
    template_name = 'services_list.html'
    success_url = '../done/'

    def get_context_data(self, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        context["services"] = Services.objects.all()
        return context

    # extra_context = {'services': Services.objects.all()}
