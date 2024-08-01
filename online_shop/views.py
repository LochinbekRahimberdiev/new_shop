from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment
from .forms import CommentForm

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.filter(is_visible=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = CommentForm()

    return render(request, 'product_detail.html', {'product': product, 'comments': comments, 'form': form})
 
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def add_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        product = request.POST.get('product')
        order = Order(name=name, phone=phone, product=product)
        order.product = Product.objects.get(id=request.POST.get('product'))
        order.save()
