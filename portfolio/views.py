import json
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from .models import Portfolio, Asset
from .forms import PortfolioForm, AddAsset, UpdateAsset

tickerList = []
global coins
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

params = {
    'start': '1',
    'limit': '100',
    'convert': 'USD'
}

headers = {
    'X-CMC_PRO_API_KEY': settings.APIKEY,
    'Accepts': 'application/json'
}

session = Session()
session.headers.update(headers)


def call_api():
    try:
        response = session.get(URL, params=params)
        data = json.loads(response.text)
        coins = data['data']
        get_ticker_list(data)

        return coins

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def get_ticker_list(data):
    for d in data['data']:
        ticker_from_api = d['symbol']
        tickerList.append(ticker_from_api)
    

def get_coin_price(ticker, coins):
    if ticker in tickerList:
        for x in coins:
            if x['symbol'] == ticker:
                price = float((x['quote']['USD']['price']))
                
        return price


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
        obj.usd_value = 0.00
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
    portfolios = Portfolio.objects.filter(user=request.user)
    context = {
        'assets': assets,
        'portfolio_id': portfolio_id,
        'portfolios': portfolios
    }
    return render(request, 'portfolio/assets.html', context)


def add_asset(request, portfolio_id, coin_id=None):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    returnedCoin = call_api()
    print(get_coin_price('LUNA', returnedCoin))
    form = AddAsset()
    if request.method == "POST":
        coin = request.POST.get("ticker")
        form = AddAsset(request.POST)
        if form.is_valid():
            try:
                asset = Asset.objects.get(portfolio_name=portfolio_id, ticker=coin)
                # asset = Asset.objects.get(portfolio_name=portfolio_id, coinID=coin)
                print(asset)
                print("A Coin with the ID " + coin + " exists!")
                pk = asset.id
                b_or_s = 'buy'
                update_asset(request, pk, b_or_s)

                return redirect(reverse('get_asset_list', args=[portfolio_id]))

            except Asset.DoesNotExist:
                print("Coin with that ID doesn't exist")
                obj = form.save(commit=False)
                obj.ticker = coin
                obj.pnl = 0.00
                obj.usd_earned = 0.00
                obj.portfolio_name = portfolio
                obj.average_price = form['average_price'].value()
                quantity = float(form['quantity'].value())
                AP = float(form['average_price'].value())
                # coinID = form['coinID'].value()
                # price = get_coin_price(str(coinID), returnedCoin)
                # print(price)
                USDspent = quantity * AP
                obj.usd_spent = USDspent
                obj.current_investment = USDspent
                obj.save()
                return redirect(reverse('get_asset_list', args=[portfolio_id]))

    context = {
        'form': form,
        'tickerList': tickerList
    }
    return render(request, 'portfolio/add_asset.html', context)


def update_asset(request, pk, b_or_s):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        coin = request.POST.get("ticker")
        form = UpdateAsset(request.POST, instance=asset)
        asset_qty = float(asset.quantity)
        curr_inv = float(asset.current_investment)
        curr_usd_earned = float(asset.usd_earned)
        curr_PnL = float(asset.pnl)
        if b_or_s == 'buy':
            # do the calculations for BUYING
            new_qty = float(form['quantity'].value())
            new_inv = float(form['average_price'].value()) * new_qty
            asset.quantity = asset_qty + new_qty
            asset.current_investment = curr_inv + new_inv
            asset.usd_spent = asset.current_investment
            asset.ticker = coin
            asset.save()
            messages.success(request, f"{new_qty} {coin} successfully purchased!")

        elif b_or_s == 'sell':
            # do the calculations for SELLING
            if float(form['quantity'].value()) > asset_qty:
                messages.error(request, "Not enough available to sell.")
                return redirect(update_asset, pk, 'sell')
            else:
                new_qty = float(form['quantity'].value())
                price = float(form['average_price'].value())
                usd_earned = price * new_qty
                asset.ticker = coin
                asset.quantity = asset_qty - new_qty
                asset.usd_earned = curr_usd_earned + usd_earned
                # asset.PnL = curr_PnL + (asset.USDEarned - asset.CurrentInvestment)
                if asset.quantity <= 0:
                    asset.delete()
                else:
                    asset.save()
                messages.success(request, f"{new_qty} {coin} successfully sold!")
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
