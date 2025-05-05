import random

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.server_index_rr = 0

    def round_robin(self):
        server = self.servers[self.server_index_rr]
        self.server_index_rr = (self.server_index_rr + 1) % len(self.servers)
        return server

    def random_selection(self):
        return random.choice(self.servers)

def simulate_client_requests(load_balancer, num_requests):
    for i in range(num_requests):
        print(f"Request {i+1}:")
        # Using Round Robin algorithm
        server_rr = load_balancer.round_robin()
        print(f"  Round Robin - Server: {server_rr}")
        # Using Random algorithm
        server_random = load_balancer.random_selection()
        print(f"  Random - Server: {server_random}")
        print()

if __name__ == "__main__":
    servers = ["Server A", "Server B", "Server C"]
    load_balancer = LoadBalancer(servers)
    simulate_client_requests(load_balancer, 10)
