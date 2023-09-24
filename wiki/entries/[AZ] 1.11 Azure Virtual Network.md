
---
tag: Cloud, Azure
---

- each Vnet has 1 defaut subnet. 

###### When you set up a virtual network, you define a private IP address space by using either public or private IP address ranges.
Defining a private IP address space means specifying the range of IP addresses that will be used within a network for internal communication. Private IP addresses are not routable over the public internet, and they are used for internal communication within a specific network, such as a local area network (LAN) or a virtual network in Azure.

When defining a private IP address space, you can choose to base it on either a public or a private IP address range:

1. Private IP address range: This refers to the reserved IP address ranges specified by the Internet Assigned Numbers Authority (IANA) for private use. These ranges are not reachable over the public internet and are intended for internal networks. The most commonly used private IP address ranges are:

   - 10.0.0.0 to 10.255.255.255 (CIDR notation: 10.0.0.0/8)
   - 172.16.0.0 to 172.31.255.255 (CIDR notation: 172.16.0.0/12)
   - 192.168.0.0 to 192.168.255.255 (CIDR notation: 192.168.0.0/16)

   Choosing a private IP address range means you are using these reserved address ranges within your network.

2. Public IP address range: This refers to IP addresses that are routable over the public internet. Public IP addresses are used to uniquely identify devices or resources accessible from the internet. However, it's important to note that you should not use public IP addresses for private networks, as this can lead to IP address conflicts and other issues.

When setting up a private network, you would typically choose a private IP address range (e.g., 10.0.0.0/16) for your virtual network in Azure or for your on-premises network. This ensures that the IP addresses used within the network are reserved for private use and are not reachable from the public internet. Public IP addresses, on the other hand, are assigned to resources that need to be accessible from the internet, such as web servers or load balancers.

In summary, the decision to use a public or private IP address range is based on the purpose of the network and whether the IP addresses need to be routable over the public internet or restricted to internal communication. Private IP addresses are used for internal networks, while public IP addresses are used for resources accessible from the internet.


It's important to plan your VNet address space and subnet ranges carefully, as they determine the number of IP addresses available for your resources and can impact network communication and resource placement. Azure does not automatically assign subnet IP address ranges; you need to specify them during the VNet and subnet creation process.

###### Azure-provided name resolution

Name resolution service in Azure is a service that allows you to find the IP address of a resource in a virtual network by using its domain name. A domain name is a human-readable name that identifies a resource on the internet, such as www.bing.com. An IP address is a numerical address that identifies a resource on the network, such as 204.79.197.200. Name resolution service helps you to connect to resources in a virtual network without having to remember their IP addresses.

Azure provides several name resolution options, depending on your needs and preferences. One of these options is Azure-provided name resolution, which is the default option when you create a virtual network. Azure-provided name resolution automatically assigns a domain name and an IP address to each resource in your virtual network, and handles the name resolution for you. You don’t have to configure anything or manage any DNS servers to use this option. However, you also don’t have much control over the domain names or the DNS records of your resources.

Another option is Azure DNS private zones, which is a service that allows you to create and manage your own private DNS zones in Azure. A DNS zone is a collection of domain names and their corresponding IP addresses. Azure DNS private zones lets you create custom domain names for your resources in your virtual network, and manage the DNS records of those domain names. You can also link multiple virtual networks to the same private DNS zone, and enable secure communication between them. Azure DNS private zones gives you more control and flexibility over your name resolution service, but it also requires more configuration and management.



###### Border Gateway Protocol (BGP) works with Azure VPN gateways, Azure Route Server, or Azure ExpressRoute to propagate on-premises BGP routes to Azure virtual networks.

Azure Route Server ???


###### hardened network appliance.

###### wide area network (WAN) optimization

###### Route Tables vs User Defined Routes

###### Route Tables vs BGPs