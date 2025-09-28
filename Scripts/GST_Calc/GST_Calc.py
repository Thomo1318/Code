# Function to calculate GST
def calculate_gst(prices):
    gst_list = [round(price * 0.10 / 1.10 + 0.00005, 2) for price in prices]  # Rounding to 4 decimal places
    return gst_list

# Read prices from file
def read_prices_from_file(file_name):
    invoice_data = []  # List to hold tuples of (invoice_number, price)
    try:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()  # Remove any leading/trailing whitespace
                if line:  # Check if the line is not empty
                    # Split the line to extract the invoice number and price
                    parts = line.split('-')
                    if len(parts) > 1:
                        invoice_number = parts[0].strip()  # Get the invoice number
                        try:
                            price = float(parts[1].strip())  # Convert the price part to float
                            invoice_data.append((invoice_number, price))  # Store as a tuple
                        except ValueError:
                            print(f"Error: Could not convert price '{parts[1].strip()}' to float.")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    return invoice_data

# Main code execution
if __name__ == "__main__":
    file_name = 'GST_Calc_Prices.txt'
    invoice_data = read_prices_from_file(file_name)
    
    if invoice_data:
        gst_amounts = calculate_gst([price for _, price in invoice_data])  # Calculate GST for prices
        for (invoice_number, price), gst in zip(invoice_data, gst_amounts):
            print(f"Invoice: {invoice_number}, Price: ${price:.2f}, GST: ${gst:.2f}")  # Printing invoice number, price, and GST
