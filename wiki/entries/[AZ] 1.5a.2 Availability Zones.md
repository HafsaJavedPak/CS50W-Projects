---
tag: Cloud, Azure
---

### Azure availability zones: 
> Physically separate datacenters within a region, designed for resiliency. i.e. diff buildings

- Each zone has independent power, cooling, and networking.
- Zones are connected through high-speed private networks.
- A minimum of three zones are present in availability zone-enabled regions.
- Availability zones can be used for running mission-critical applications and achieving high availability.
- Resiliency in case of a building level problem. Localized issue will only affect a particular datacentre.
- Each Subscription will only have a maximum of three availability zones available to a user, even if there are more available in that region .
- Updates will be rolled out to one availability zone 1st, so if they r successful then to other zones. and if not successful, your other instances of application in other zones won't be affected.

##### Categories of Azure services
1. **Zonal services** 
	 - Azure services that allow you to deploy a resource to a specific availability zone within a region. 
	 - This gives you more control over the **latency and performance** of your resource. howlatrncy??????????
	 - You can also replicate your resource across multiple zones for higher availability and resiliency.
	 - e.g., VMs, managed disks, IP addresses
	
2. **Zone-redundant services** 
	 - Azure services that automatically replicate or distribute your resource across multiple availability zones within a region. 
	 - Zone-redundant services are not tied to a single zone but operate within a single region.
	 - This gives you more **convenience and reliability** for your resource without having to manage the replication yourself
	 - e.g., zone-redundant storage, SQL Database
	
3. **Non-regional services**
	- are Azure services that are always available across all Azure regions and are resilient to zone-wide or region-wide outages.  then aht inc ase or 1 dand 2
	- Non-regional services are available in all Azure regions. They are not tied to any specific region or availability zone, meaning they function uniformly across all regions.
	- Since non-regional services are not tied to a specific region, they are always accessible regardless of the status of individual zones or regions, making them highly **reliable and widely available.**
	- Examples include Azure Active Directory, Azure Key Vault, and Azure Traffic Manager.

##### Examples of Azure Services

1. **Zonal services:**
   - You have a web application that serves users in a specific geographic area. You deploy the web application to a zonal service within the?????????????? closest availability zone to reduce latency and improve performance for those users.

2. **Zone-redundant services:**
   - You run a critical database for your application. You choose a zone-redundant service like Azure SQL Database, which automatically replicates your database across multiple availability zones. In case one zone goes down, your database remains available and operational from the other zones.

3. **Non-regional services:**
   - You need to implement a global authentication and authorization system for your application. You use [[[AZ] 2.7 Directory infrastructure]] as a non-regional service to manage user identities and access across all regions where your application is deployed.

4. **Combining services:**
   - For a comprehensive application deployment, you might use a combination of services. For example, you deploy your web application to a zonal service in one region for low-latency access, while using zone-redundant storage for the data to ensure data availability even during zone-level failures.

Remember that the choice of services depends on your specific application's requirements, performance needs, and desired level of resiliency. By understanding the characteristics of each service type, you can build a well-architected and reliable application in Azure.