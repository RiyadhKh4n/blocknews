from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Portfolio, Asset
from .forms import PortfolioForm, AddAsset, UpdateAsset
from coin.views import *


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
    assets = Asset.objects.filter(portfolio_name=portfolio_id)
    context = {
        'assets': assets,
        'portfolio_id': portfolio_id,
    }
    return render(request, 'portfolio/assets.html', context)


def add_asset(request, portfolio_id, coin_id=None):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    form = AddAsset()
    if request.method == "POST":
        form = AddAsset(request.POST)
        if form.is_valid():
            coin = form['coinID'].value()
            try:
                asset = Asset.objects.get(portfolio_name=portfolio_id, coinID=coin)
                print(asset)
                print("A Coin with the ID " + coin + " exists!")
                pk = asset.id
                b_or_s = 'buy'
                update_asset(request, pk, b_or_s)

            except Asset.DoesNotExist:
                print("Coin with that ID doesn't exist")
                obj = form.save(commit=False)
                obj.PnL = 0.00
                obj.USDEarned = 0.00
                obj.portfolio_name = portfolio
                obj.AveragePrice = form['AveragePrice'].value()
                quantity = float(form['quantity'].value())
                AP = form['AveragePrice'].value()
                # coinID = form['coinID'].value()
                # price = get_coin_price(coinID)
                USDspent = (quantity) * float(AP)
                obj.USDSpent = USDspent
                obj.CurrentInvestment = USDspent
                obj.save()
                return redirect(reverse('get_asset_list', args=[portfolio_id]))

    context = {'form': form}
    return render(request, 'portfolio/add_asset.html', context)


def update_asset(request, pk, b_or_s):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        form = UpdateAsset(request.POST, instance=asset)
        asset_qty = float(asset.quantity)
        curr_inv = float(asset.CurrentInvestment)
        curr_usd_earned = float(asset.USDEarned)
        if b_or_s == 'buy':
            # do the calculations for BUYING
            new_qty = float(form['quantity'].value())
            new_inv = float(form['AveragePrice'].value()) * new_qty
            asset.quantity = asset_qty + new_qty
            asset.CurrentInvestment = curr_inv + new_inv
            asset.USDSpent = asset.CurrentInvestment
            asset.save()
            messages.success(request, f"{new_qty} {asset} successfully purchased!")

        elif b_or_s == 'sell':
            # do the calculations for SELLING
            if float(form['quantity'].value()) > asset_qty:
                messages.error(request, "Not enough available to sell.")
                return redirect(update_asset, pk, 'sell')
            else:
                new_qty = float(form['quantity'].value())
                price = float(form['AveragePrice'].value())
                usd_earned = price * new_qty
                asset.quantity = asset_qty - new_qty
                asset.USDEarned = curr_usd_earned + usd_earned
                if asset.quantity <= 0:
                    asset.delete()
                else:
                    asset.save()
                messages.success(request, f"{new_qty} {asset} successfully sold!")
        return redirect(get_asset_list, asset.portfolio_name.pk)

    if b_or_s == 'sell':
        # grab the current quantity available to sell
        form = UpdateAsset(instance=asset)
    else:
        form = UpdateAsset()
    context = {
        'asset': asset,
        'b_or_s': b_or_s,
        'form': form,
    }
    return render(request, 'portfolio/buy_sell_asset.html', context)

