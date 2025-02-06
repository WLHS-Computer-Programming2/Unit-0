def find_average_price(price1,price2):
    return (price1+price2)/2

def cube_volume(side_length):
    """Returns the volume of a cube
    """
    volume = side_length**3
    return volume


# exception for not printing inside functions
def main():
    '''price1 = float(input("What is the price? "))
    price2 = float(input("What is the next price? "))
    avg_price = find_average_price(price1,price2)
    print(f"The average price of ${price1} and ${price2} is ${avg_price:.2f}.")
    '''
    print(f"Side length 3, volume {cube_volume(3)}")
    print(f"Side length 7, volume {cube_volume(7)}")
    print(f"Side length 10, volume {cube_volume(10)}")

if __name__ == '__main__':
    main()