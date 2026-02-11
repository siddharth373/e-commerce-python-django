from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Product
from . import recommender


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    recs = recommender.recommend_for_product(pk, topn=5, session=request.session)
    # Get the actual product objects for recommendations to display names
    rec_ids = [r['id'] for r in recs]
    rec_products = Product.objects.filter(pk__in=rec_ids)
    rec_map = {p.pk: p for p in rec_products}
    enriched_recs = [{'id': r['id'], 'score': r['score'], 'name': rec_map.get(r['id'], {}).name} 
                     for r in recs if r['id'] in rec_map]
    return render(request, 'store/product_detail.html', {'product': product, 'recommendations': enriched_recs})


@require_POST
def add_to_cart(request, pk):
    cart = request.session.get('cart', {})
    cart[str(pk)] = cart.get(str(pk), 0) + 1
    request.session['cart'] = cart
    return redirect('store:view_cart')


def view_cart(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for pid, qty in cart.items():
        try:
            p = Product.objects.get(pk=int(pid))
        except Product.DoesNotExist:
            continue
        subtotal = float(p.price) * qty
        items.append({'product': p, 'quantity': qty, 'subtotal': subtotal})
        total += subtotal
    return render(request, 'store/cart.html', {'items': items, 'total': total})


@require_POST
def checkout(request):
    request.session.pop('cart', None)
    return render(request, 'store/checkout.html')


def recommendations(request):
    recs = recommender.recommend_for_session(request.session, topn=10)
    products = Product.objects.filter(pk__in=[r['id'] for r in recs])
    # preserve order
    prod_map = {p.pk: p for p in products}
    ordered = [prod_map[r['id']] for r in recs if r['id'] in prod_map]
    return render(request, 'store/recommendations.html', {'products': ordered})


@require_POST
def feedback(request):
    # user can like/dislike product ids via POST 'action'='like'|'dislike' and 'product'
    action = request.POST.get('action')
    pid = request.POST.get('product')
    if not pid:
        return redirect('store:product_list')
    likes = set(request.session.get('likes', []))
    dislikes = set(request.session.get('dislikes', []))
    if action == 'like':
        likes.add(pid)
        dislikes.discard(pid)
    elif action == 'dislike':
        dislikes.add(pid)
        likes.discard(pid)
    request.session['likes'] = list(likes)
    request.session['dislikes'] = list(dislikes)
    return redirect(request.META.get('HTTP_REFERER', '/'))
