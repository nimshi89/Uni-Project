
def output_profit_data(stock_items, no_of_items_bought, item_cost, buy_commission, no_of_items_sold, item_sale_price, sale_commission):

    for item_count in range(0,len(no_of_items_bought)):
        print("================================")
        print(f"{no_of_items_bought[item_count]} {stock_items[item_count]} brought for {item_cost[item_count]} each (0.1% buy commission) ")
        cost = (item_cost[item_count] + (item_cost[item_count] * 0.1)) * no_of_items_bought [item_count]
        print(f"Money spent buying shoes was {cost:.2f}")
        print(f"{no_of_items_sold[item_count]} {stock_items[item_count]} sold for {item_sale_price[item_count]} each (0.1% sale commission)")
        earned = (item_sale_price[item_count] - (item_sale_price[item_count] * 0.1)) * no_of_items_sold[item_count]
        print(f"Money earned selling shoes was {earned:.2f}")
        profit = earned - cost
        print(f"Profit for {stock_items[item_count]} was {profit:.2f}")
        print("================================")
        print()

def load_purchase_data(filename):
    stock_items = []
    no_of_items_bought = []
    items_cost = []
    buy_commision = []
    file = open(filename, 'r')
    line = file.readline()
    while line != "":
        line = line.strip()
        stock_items.append(line)
        line = file.readline()
        no_of_items_bought.append(int(line))
        line = file.readline()
        items_cost.append(float(line))
        line = file.readline()
        buy_commision.append(float(line))
        line = file.readline()
    file.close()
    return stock_items, no_of_items_bought, items_cost, buy_commision  

def load_sales_data(filename):
    stock_items = []
    no_of_items_sold = []
    item_sale_price = []
    sale_commission = []
    file = open(filename, 'r')
    line = file.readline()
    while line != "":
        line = line.strip()
        stock_items.append(line)
        line = file.readline()
        no_of_items_sold.append(int(line))
        line = file.readline()
        item_sale_price.append(float(line))
        line = file.readline()
        sale_commission.append(float(line))
        line = file.readline()
    file.close()
    return stock_items, no_of_items_sold, item_sale_price, sale_commission
    
        
 

if __name__ == '__main__':
    stock_items = []        #list of strings
    no_of_items_bought = [] 
    item_cost = []          
    buy_commission = []     
    no_of_items_sold = []   
    item_sale_price = []    
    sale_commission = []    
    
    stock_items, no_of_items_bought, item_cost, buy_commission = load_purchase_data("purchase_data.txt")
    stock_items, no_of_items_sold, item_sale_price, sale_commission = load_sales_data("sales_data.txt")

    output_profit_data(stock_items, no_of_items_bought, item_cost, buy_commission, no_of_items_sold, item_sale_price, sale_commission)
