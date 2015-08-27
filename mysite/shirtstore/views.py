# Given the app shirtstore, write a view to display which shirts are available at which store

# Create your views here.
from django.http import HttpResponse

from .models import Shirt, Store

def index(request):
    # a = [[x for x in range(columns)] for y in range(rows)]

    stores = Store.objects.all()
    shirts = stores.available_shirts.all()
    store1 = stores[0]
    # store2 = stores[1]
    # store3 = stores[2]
    # store4 = stores[3]
    # shirts = Shirt.objects.all()

    super_list = [x for x in stores]

    # ss1 = stores[0].available_shirts.all()
    # ss1s = []
    #
    # for each in ss1:
    #     ss1s.append(str(each))
    # ss1j = ' '.join(ss1s)
    #
    # for store in stores:
    #     shirts = store.objects.all()
    #     for shirt in shirts:
    #         super_list.append(store, shirt)

    # store =
    # store.available_shirts.all()
    #
    # shirt = Shirt.objects.first()
    # shirt.store_set_all()

    # html = "<html><body>Stores!: {}, {}, {}, {}</body></html>".format(store1, store2, store3, store4)

    html = "<html><body> {}</body></html>".format(super_list)

    return HttpResponse(html)

