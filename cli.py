import click
from bot.orders import place_order
from bot.validators import validate_order
from bot.client import get_client
import time

@click.command()
@click.option('--symbol', required=True)
@click.option('--side', required=True)
@click.option('--type', 'order_type', required=True)
@click.option('--quantity', type=float, required=True)
@click.option('--price', type=float, default=None)

def run(symbol, side, order_type, quantity, price):
    try:
        validate_order(symbol, side, order_type, quantity, price)

        print("\nOrder Summary:")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if price:
            print(f"Price: {price}")

        # 🔹 Place Order
        order = place_order(symbol, side, order_type, quantity, price)

        print("\nOrder Response:")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")

        # 🔹 Wait for execution
        time.sleep(2)

        # 🔹 Fetch updated status
        client = get_client()
        updated_order = client.futures_get_order(
            symbol=symbol,
            orderId=order.get("orderId")
        )

        print("\nUpdated Order Status:")
        print(f"Status: {updated_order.get('status')}")
        print(f"Executed Qty: {updated_order.get('executedQty')}")
        print(f"Avg Price: {updated_order.get('avgPrice')}")

        if updated_order.get("status") == "FILLED":
            print("\n✅ Order fully executed")
        else:
            print("\n⚠️ Order not filled yet")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    run()