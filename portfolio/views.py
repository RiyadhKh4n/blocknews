from django.shortcuts import render, redirect, get_object_or_404
from .models import Portfolio, Asset
from django.contrib.auth.models import User
from .forms import PortfolioForm, AddAsset


def get_portfolio_list(request):
    portfolios = Portfolio.objects.filter(user=request.user)
    context = {
        'portfolios': portfolios
    }
    return render(request, 'portfolio/portfolio.html', context)


def create_portfolio(request):
    form = PortfolioForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.slug = form['name'].value()
        obj.USDvalue = 0.00
        obj.save()
        return redirect('get_portfolio_list')

    context = {'form': form}
    return render(request, 'portfolio/create_portfolio.html', context)


def edit_portfolio(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('get_portfolio_list')
    form = PortfolioForm(instance=portfolio)
    context = {
        'form': form
    }
    return render(request, 'portfolio/edit_portfolio.html', context)


def delete_portfolio(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    portfolio.delete()
    return redirect('get_portfolio_list')


def get_asset_list(request, portfolio_id):
    assets = Asset.objects.filter(portfolioID=portfolio_id)
    context = {
        'assets': assets
    }
    return render(request, 'portfolio/assets.html', context)


def add_asset(request):
    form = AddAsset(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.portfolioID = request.portfolio.name
        obj.save()
        return redirect('get_asset_list')

    context = {'form': form}
    return render(request, 'portfolio/add_asset.html', context)