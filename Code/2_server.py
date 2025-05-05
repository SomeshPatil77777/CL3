import Pyro4

#python -m Pyro4.naming

@Pyro4.expose
class StringConcatenationServer:
    def concatenate_strings(self, str1, str2):
        return str1 + str2

def main():
    # Start the Pyro daemon
    daemon = Pyro4.Daemon()

    # Locate the Pyro name server
    ns = Pyro4.locateNS()

    # Create an instance of the server class
    server = StringConcatenationServer()

    # Register the server object with the Pyro daemon
    uri = daemon.register(server)

    # Register the object with the name server under a specific name
    ns.register("string.concatenation", uri)

    print("Server is running. URI:", uri)

    # Optionally save the URI to a file
    with open("server_uri.txt", "w") as f:
        f.write(str(uri))

    # Start the server loop to wait for calls
    daemon.requestLoop()

if __name__ == "__main__":
    main()



