import Pyro4

def main():
    # Read the server URI from the saved file
    with open("server_uri.txt", "r") as f:
        uri = f.read()

    # Create a proxy to the server object
    server = Pyro4.Proxy(uri)

    # Get user input
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    # Call the remote method
    result = server.concatenate_strings(str1, str2)

    # Display the result
    print("Concatenated Result:", result)

if __name__ == "__main__":
    main()
