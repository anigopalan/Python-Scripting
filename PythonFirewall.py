#Firewall: What is it?
# - A program that sits between a network, evaluates the network based on predetermined rules:
# 2 Outcomes:
# either the data will get dropped
# allows the data to enter the network


# 1. Define Rules
# 2. Simulate Traffic
# 3. Evaluate + Act
# 4. Output Results

import random

def generate_random_ip():
    return f"192.168.1.{random.randint(0,20)}"

def check_firewall_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
        
    return "allow"

def main():
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block",
    }

    for _ in range(12):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0, 9999)
        print(f"IP: {ip_address}, Action: {action}, Identifier: {random_number}")

if __name__ == "__main__":
    main()



#Example Output:
#IP: 192.168.1.12, Action: allow, Identifier: 1002
#IP: 192.168.1.5, Action: allow, Identifier: 2044
#IP: 192.168.1.18, Action: allow, Identifier: 5061
#IP: 192.168.1.8, Action: allow, Identifier: 4080
#IP: 192.168.1.18, Action: allow, Identifier: 5556
#IP: 192.168.1.19, Action: block, Identifier: 4082
#IP: 192.168.1.8, Action: allow, Identifier: 5280
#IP: 192.168.1.14, Action: allow, Identifier: 6655
#IP: 192.168.1.3, Action: allow, Identifier: 1328
#IP: 192.168.1.10, Action: allow, Identifier: 3105
#IP: 192.168.1.8, Action: allow, Identifier: 2721
#IP: 192.168.1.12, Action: allow, Identifier: 3060
