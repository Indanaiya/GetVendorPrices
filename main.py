import json
import requests

# TODO string formatting so I can make a nice looking table of the resuls
# TODO A loading... message while data is fetched from Universalis
# TODO maybe use better variable names

universalis_url = "https://universalis.app/api/"
stored_item_values_address = "btvendoritems.json"
server = "Cerberus"


def getItemsFromUniversalis(item_values=None):
    with open(stored_item_values_address) as f:
        stored_item_values = json.load(f)
        if not item_values:
            item_values = stored_item_values
    item_prices = {}
    for i in item_values:
        with requests.request("GET", universalis_url + server + "/" + str(item_values[i]['id']) + "?entries=1") as response:
            response_json = response.json()
            price = response_json['listings'][0]['pricePerUnit']
            profit = price - item_values[i]['price']
            #Sales velocity is average sales per day in the past week. Value is capped at 10/7
            sales = response_json['regularSaleVelocity']*7
            item_prices[i] = {'price': price,
                              'profit': profit,
                              'sales':sales}
    sorted_prices = sorted(
        item_prices.items(), key=lambda x: x[1]['profit'], reverse=True)

    header_profit = "Profit Per Item"
    header_name = "Item(Unit Price)"
    price_per_colwidth = max([len(str(item[1]['profit']))
                              for item in item_prices.items()] + [len(header_profit)])
    header_title = f"{header_profit} | {header_name}"

    #print(*["=" for i in range(len(header_string))], sep="")
    data_to_print = []
    for k, v in sorted_prices:
        data_to_print.append(
            f"{str(v['profit']):>{price_per_colwidth}} | {str(k)}({str(v['sales'])})")

    print(header_title)
    # Prints enough = to cover the width of the widest point of the table
    print(*["=" for i in range(max([len(string)
                                    for string in data_to_print] + [len(header_title)]))], sep="")
    print(*data_to_print, sep="\n")


if __name__ == "__main__":
    getItemsFromUniversalis()
