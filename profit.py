***
A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00
***
def calculate_profit_or_loss(cost_price_per_dozen, selling_price_per_banana):
    cost_price_per_banana = cost_price_per_dozen / 12
    if selling_price_per_banana > cost_price_per_banana:
        profit = (selling_price_per_banana - cost_price_per_banana) * 12
        return f"Profit : Rs.{profit:.2f}"
    elif selling_price_per_banana < cost_price_per_banana:
        loss = (cost_price_per_banana - selling_price_per_banana) * 12
        return f"Loss : Rs.{loss:.2f}"
    else:
        return "No Profit, No Loss"
cost_price_per_dozen = float(input())
selling_price_per_banana = float(input())
result = calculate_profit_or_loss(cost_price_per_dozen, selling_price_per_banana)
print(result)
