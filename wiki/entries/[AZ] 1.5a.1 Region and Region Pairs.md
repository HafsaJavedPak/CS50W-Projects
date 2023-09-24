---
tag: Cloud, Azure
---
#### Azure regions: 
> Geographical areas containing one or more nearby datacenters networked together with low latency connectivity.
- Regions intelligently assign and balance resources for workloads.
- Resource deployment in Azure requires choosing a specific region.
- Some services or features are region-specific.
- envelops 2ms round trip areas
- There are used for : 
	- Regulatory Reasons (storing data in a certain region to meet regulatory and security demands )
	- Performance (e.g. deploying application near customers)
	- Data Resiliency
###### Advantages of multiple regions
1. **Performance** : 
	- You can have your service deployed close to you.
	- or closer to your customers, therefore your customer will access the closest region.
2. **Regulatory reasons**
	- in order for your data to stay in the appropriate geopolitical boundary.
3. **Resiliency**
	- You could deploy your application or service in region A, but in case of a disaster it would fall over to region B.
	- Or your service could be running in both of them and you could strike a balance between them based on factors such as user demand, network conditions, and resource utilization.

### Region Pairs
- Most regions are paired with another region within the same geography.
- Paired regions are located at least 300 miles apart to reduce the likelihood of interruptions.
- Resources can be replicated across paired regions for resilience and failover.
- Not all Azure services automatically replicate or fall back, requiring manual configuration by the customer.
##### Resiliency for Customer
like above reason in "Regions" Section.

##### Resiliency for Microsoft
>  Region pairs provide advantages like prioritized restoration during outages, staged updates, and jurisdiction compliance.	

 - In case of large scale e.g. power outage, Microsoft will prioritize a certain region pair then the the pair, to quickly restart the system
- In case of updates and patches, they will be deployed to a certain region pair first, and if it's successful, then to the other region pair. 


#### Azure sovereign regions: 
>Isolated (physical and logical) instances of Azure for compliance or legal purposes.
- by US, Germany and China.
- Hence, it can only be  accessed by people from that area or government. Unlike a public cloud where anyone who pays for it can use it.
- **Examples** include US government regions and regions in partnership with 21Vianet in China.
