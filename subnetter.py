# Get list of IPs from each subnet in a file

import ipaddress
import sys

def get_ips_for_subnet(subnet):
  """Gets the IP addresses for a subnet.

  Args:
    subnet: The subnet in CIDR notation.

  Returns:
    A list of IP addresses.
  """

  network = ipaddress.ip_network(subnet)
  ips = []
  for host in network.hosts():
    ips.append(host)
  return ips

def get_ips_for_subnets(filename):
  """Gets the IP addresses for a list of subnets from a file.

  Args:
    filename: The filename of the file containing the subnets.

  Returns:
    A list of IP addresses.
  """

  with open(filename) as f:
    subnets = f.readlines()

  ips = []
  for subnet in subnets:
    ips.extend(get_ips_for_subnet(subnet.strip()))

  return ips

def pretty_print_ips(ips):
  """Pretty prints the IPs in groups.

  Args:
    ips: A list of IP addresses.

  Returns:
    A string containing the pretty printed IPs.
  """

  groups = []
  for i in range(0, len(ips), 256):
    groups.append(ips[i:i + 256])

  output = ""
  for group in groups:
    output += "\n".join([str(ip) for ip in group]) + "\n"

  return output

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python get_ips_for_subnets.py <filename>")
    sys.exit(1)

  filename = sys.argv[1]
  ips = get_ips_for_subnets(filename)
  print(pretty_print_ips(ips))
