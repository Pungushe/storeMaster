from django.shortcuts import render


# контролеры-views(вьюхи)- функции

def index(request):
    context={
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context={
        'title': 'Store-Каталог'
    }
    return render(request, 'products/products.html', context)


def test_context(request):
    context = {
        'title': 'Store',
        'header': 'Welcome',
        'username': 'Иван Иванов',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090.00},
            {'name': 'Синяя куртка The North Face', 'price': 23725.00},
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340.00}
        ],
        # 'promotion': True,
        'products_of_promotion': [
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890.00}
        ]
    }
    return render(request, 'products/test-context.html', context)
