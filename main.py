import json
import requests

universalis_url = "https://universalis.app/api/"
server = "Cerberus"

items = {
    "Windfowl Feather": {
        "id": 5360,
        "price": 259
    },
    "Undyed Velveteen": {
        "id": 5326,
        "price": 169
    },
    "Undyed Linen": {
        "id": 5327,
        "price": 411
    },
    "Undyed Cotton Cloth": {
        "id": 5325,
        "price": 52
    },
    "Turquoise Green Dye": {
        "id": 5786,
        "price": 334
    },
    "Sylphic Silk": {
        "id": 7028,
        "price": 693
    },
    "Sylphic Lamppost": {
        "id": 6496,
        "price": 21780
    },
    "Sylphic Lamp Tree": {
        "id": 6495,
        "price": 26136
    },
    "Straw": {
        "id": 5342,
        "price": 9
    },
    "Shale Brown Dye": {
        "id": 5759,
        "price": 216
    },
    "Qiqirn Brown Dye": {
        "id": 5751,
        "price": 334
    },
    "Marsh Green Dye": {
        "id": 5777,
        "price": 216
    },
    "Linen Yarn": {
        "id": 5336,
        "price": 186
    },
    "Lime Green Dye": {
        "id": 5773,
        "price": 216
    },
    "Glamour Dispeller": {
        "id": 7621,
        "price": 500
    },
    "Crow Feather": {
        "id": 5352,
        "price": 21
    },
    "Cotton Yarn": {
        "id": 5334,
        "price": 22
    },
    "Cactuar Green Dye": {
        "id": 5779,
        "price": 334
    },
    "Aldgoat Green Dye": {
        "id": 5753,
        "price": 216
    },
    "Acorn Brown Dye": {
        "id": 5755,
        "price": 334
    },

    "Yew Lumber": {
        "id": 5368,
        "price": 108
    },
    "Yew Branch": {
        "id": 5405,
        "price": 60
    },
    "Walnut Lumber": {
        "id": 5371,
        "price": 219
    },
    "Soot Black Dye": {
        "id": 5734,
        "price": 216
    },
    "Snow White Dye": {
        "id": 5729,
        "price": 216
    },
    "Royal Blue Dye": {
        "id": 5801,
        "price": 216
    },
    "Oak Lumber": {
        "id": 5373,
        "price": 470
    },
    "Oak Branch": {
        "id": 5409,
        "price": 238
    },
    "Morbol Green Dye": {
        "id": 5787,
        "price": 216
    },
    "Maple Lumber": {
        "id": 5361,
        "price": 9
    },
    "Maple Branch": {
        "id": 5396,
        "price": 6
    },
    "Ixali Shelter": {
        "id": 7124,
        "price": 26136
    },
    "Ixali Banner": {
        "id": 7125,
        "price": 21780
    },
    "Hunter Green Dye": {
        "id": 5780,
        "price": 216
    },
    "Elm Lumber": {
        "id": 5367,
        "price": 78
    },
    "Ash Lumber": {
        "id": 5364,
        "price": 43
    },
    "Ash Branch": {
        "id": 5402,
        "price": 33
    },
    "Adamantoise Green Dye": {
        "id": 5782,
        "price": 334
    },
    "Aldgoat Horn": {
        "id": 5436,
        "price": 238
    },
    "Apple Green Dye": {
        "id": 5778,
        "price": 334
    },
    "Automaton Digger": {
        "id": 7126,
        "price": 26136
    },
    "Beastkin Blood": {
        "id": 5492,
        "price": 7
    },
    "Blue Landtrap Leaf": {
        "id": 5549,
        "price": 128
    },
    "Bomb Ash": {
        "id": 5528,
        "price": 82
    },
    "Cloves": {
        "id": 4831,
        "price": 16
    },
    "Coral Butterfly": {
        "id": 4876,
        "price": 18
    },
    "Cork Brown Dye": {
        "id": 5750,
        "price": 334
    },
    "Gobbiebag Brown Die": {
        "id": 5758,
        "price": 334
    },
    "Jellyfish Umbrella": {
        "id": 5557,
        "price": 24
    },
    "Kobold Furnace": {
        "id": 7127,
        "price": 21780
    },
    "Meadow Green Dye": {
        "id": 5775,
        "price": 216
    },
    "Morbol Vine": {
        "id": 5554,
        "price": 128
    },
    "Quicksilver": {
        "id": 5489,
        "price": 4
    },
    "Scalekin Blood": {
        "id": 5493,
        "price": 73
    },
    "Sylph Brown Dye": {
        "id": 5772,
        "price": 216
    },
    "Ul Brown Dye": {
        "id": 5763,
        "price": 216
    },
    "Vitriol": {
        "id": 5490,
        "price": 216
    },
    "Black Pepper":{
        "id": 4830,
        "price": 13
    },
    "Cinnamon": {
        "id": 4828,
        "price": 4
    },
    "Coral Pink Dye":{
        "id": 5741,
        "price": 334
    },
    "Corpse Blue Dye": {
        "id": 5793,
        "price": 216
    },
    "Garlean Garlic": {
        "id": 4829,
        "price": 5
    },
    "Iris Purple Dye": {
        "id": 5808,
        "price": 334
    },
    "Lavender Purple Dye":{
        "id": 5805,
        "price": 216
    },
    "Lilac Purple Dye": {
        "id": 5736,
        "price": 216
    },
    "Midland Basil": {
        "id": 4837,
        "price": 111
    },
    "Night Milk": {
        "id": 6149,
        "price": 84
    },
    "Olive Oil": {
        "id": 4857,
        "price": 8
    },
    "Rhotano Blue Dye": {
        "id": 5792,
        "price": 334
    },
    "Sahagin Hanging Larder": {
        "id": 7123,
        "price": 21780
    },
    "Sahagin Living Lamp": {
        "id": 7122,
        "price": 26136
    },
    "Shadow Blue Dye": {
        "id": 5803,
        "price": 334
    },
    "Smooth Butter": {
        "id": 4853,
        "price": 2
    },
    "Sun Lemon": {
        "id": 4811,
        "price": 28
    },
    "Sunset Wheat Flour": {
        "id": 4826,
        "price": 4
    },
    "Table Salt": {
        "id": 4847,
        "price": 2
    },
    "Amalj'aa Pavis Shield":{
        "id": 6687,
        "price": 21780
    },
    "Amalj'aa Supply Carriage": {
        "id": 6686,
        "price": 26136
    },
    "Bronze Plate": {
        "id": 5071,
        "price": 32
    },
    "Bronze Rivets": {
        "id": 5091,
        "price": 13
    },
    "Coerl Yellow Dye":{
        "id": 5767,
        "price": 216
    },
    "Currant Purple Dye": {
        "id": 5807,
        "price": 334
    },
    "Iron Ingot": {
        "id": 5057,
        "price": 68
    },
    "Iron Plate": {
        "id": 5072,
        "price": 157
    },
    "Iron Rivets": {
        "id": 5092,
        "price": 73
    },
    "Mythril Ingot": {
        "id": 5065,
        "price": 514
    },
    "Mythril Rings": {
        "id": 5089,
        "price": 617
    },
    "Mythril Rivets":{
        "id": 5099,
        "price": 583
    },
    "Peacock Blue Dye": {
        "id": 5791,
        "price": 334
    },
    "Raisin Brown Dye": {
        "id": 5770,
        "price": 334
    },
    "Raptor Blue Dye": {
        "id": 5797,
        "price": 216
    },
    "Seafog Blue Dye": {
        "id": 5790,
        "price": 216
    },
    "Steel Ingot": {
        "id": 5058,
        "price": 258
    },
    "Steel Plate": {
        "id": 5073,
        "price": 610
    },
    "Steel Rings": {
        "id": 5083,
        "price": 389
    },
    "Steel Rivets": {
        "id": 5093,
        "price": 313
    }
}


def getItemsFromUniversalis(item_values=items, min_sales=0):
    item_prices = {}
    for i in item_values:
        print("Fetching: " + i)
        with requests.request("GET", universalis_url + server + "/" + str(item_values[i]['id']) + "?entries=1") as response:
            if response == None:
                print(item_values[i]['id'] + " returned None")
                break
            response_json = response.json()
            price = response_json['listings'][0]['pricePerUnit'] if len(
                response_json['listings']) > 0 else 0
            avg_price = response_json['averagePrice'] - item_values[i]['price']
            profit = price - item_values[i]['price']
            # Sales velocity is average sales per day in the past week. Value is capped at 10/7
            sales = response_json['regularSaleVelocity']*7
            item_prices[i] = {'price': price,
                              'profit': profit,
                              'sales': sales,
                              'avg_price': avg_price}
    sorted_prices = sorted(
        item_prices.items(), key=lambda x: x[1]['profit'], reverse=True)

    header_profit = "Profit Per Item"
    header_name = "Item"
    header_sale_rate = "Sales in past week"
    header_avg_price = "Average Profit"
    price_per_colwidth = max([len(str(item[1]['profit']))
                              for item in item_prices.items()] + [len(header_profit)])
    item_colwidth = max([len(str(k))
                         for k, v in item_prices.items()] + [len(header_name)])
    sale_rate_colwidth = len(header_sale_rate)
    avg_price_colwidth = max([len(str(item[1]['avg_price']))
                              for item in item_prices.items()] + [len(header_avg_price)])
    header_title = f"{header_profit:>{price_per_colwidth}} | {header_name:^{item_colwidth}} | {header_sale_rate:^{sale_rate_colwidth}} | {header_avg_price:<{avg_price_colwidth}}"

    #print(*["=" for i in range(len(header_string))], sep="")
    data_to_print = []
    for k, v in sorted_prices:
        if v['sales'] >= min_sales:
            data_to_print.append(
                f"{str(v['profit']):>{price_per_colwidth}} | {str(k):^{item_colwidth}} | {str(int(v['sales'])):^{sale_rate_colwidth}} | {str(int(v['avg_price'])):<{avg_price_colwidth}}")

    print(header_title)
    # Prints enough = to cover the width of the widest point of the table
    print(*["=" for i in range(max([len(string)
                                    for string in data_to_print] + [len(header_title)]))], sep="")
    print(*data_to_print, sep="\n")


if __name__ == "__main__":
    min_sales_str = input(
        "Provide a minimum sales for the past week [Default=10]: ")
    try:
        min_sales_int = int(min_sales_str)
    except:
        print("Invalid input, defaulting to ten")
        min_sales_int = 10

    getItemsFromUniversalis(min_sales=min_sales_int)
    input("Press enter to exit...")
