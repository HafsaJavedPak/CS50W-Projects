---
tag: Cloud, Azure
---
❓❓❓❓❓❓❓❓❓❓
- In a cloud, you have three characteristics : 
	1. Pooling Resources  $\implies \therefore$ elasticity❓❓❓❓❓❓❓❓❓❓
	2. Self Service $\implies$ [[[AZ] 2.0 Important Terms | Quotas]] , Policies
	3. Showback / Chargeback $\implies$ show what they are using ❓

##### Public Cloud
- Meets all of the above requirements
	- it have limitless capabilities (because of many regions), has many services, and is OPEX.
- It is connected to user endpoints most through internet.
+ cloud computing environment is  built, controlled, and maintained by a third-party cloud provider. 
+ Anyone can purchase cloud services ;  can access and use resources. 
+ <mark style="background: #FF5582A6;">The general public availability is a key difference between public and private clouds</mark>

#### Private Cloud
- It is CAPEX, because organization is a buying server units.
	- Maybe as a business it's OPEX, but as a organization, it's CAPEX.
- It's defining advantage is its flexibility, and data security.
- cloud computing environment dedicated to a single organization or entity.
-  can be physically located at the organization’s on-site data centre, or it can be hosted by a third-party service provider 
- In the latter case, the service provider is responsible for deploying, configuring, and managing the private cloud infrastructure for the organization. This is also known as a **managed private cloud**.

#### Hybrid cloud
+ computing environment that uses both public and private clouds in an inter-connected environment. 
+ can be used to allow a private cloud to surge for increased, temporary demand by deploying public cloud resources. 
	+ This is known as "cloud bursting," where public cloud resources are deployed to handle the surge in workload.
	+ The term is commonly used in the context of hybrid clouds, where the bursting occurs from a private cloud to a public cloud.
	+ Though, the underlying concept can also apply to other cloud deployment models, such as scaling within a public cloud environment.
+ can be used to provide an extra layer of security. 
	+ Organizations can choose to keep sensitive or critical data and applications in their private cloud infrastructure, 
	+ while utilizing the public cloud for less sensitive workloads or for specific services.
+ For example,
	+ users can flexibly choose which services to keep in public cloud and which to deploy to their private cloud infrastructure.
	+ You can have a global load balancer to normally point traffic to a private cloud, but point to a public cloud in case of failure, or high traffic.

##### Multi-cloud:
  - Involves using multiple public cloud providers.
  - Allows organizations to leverage different features from different providers.
  - Can be a result of migrating from one provider to another.
  - Requires managing resources and security in multiple cloud environments.
  
| Public Cloud                                                       | Private Cloud                                                      | Hybrid Cloud                                                     |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ---------------------------------------------------------------- |
| No capital expenditures to scale up                                | Organizations have complete control over resources and security    | Provides the most flexibility                                    |
| Applications can be quickly provisioned and deprovisioned          | Data is not collocated with other organizations’ data              | Organizations determine where to run their applications          |
| Organizations pay only for what they use                           | Hardware must be purchased for startup and maintenance             | Organizations control security, compliance, or legal requirements |
| Organizations don’t have complete control over resources and security | Organizations are responsible for hardware maintenance and updates |                 

>**NOTE** : "No capital expenditures to scale up"  means that you don't need to make upfront investments in physical hardware or infrastructure to increase the resources (such as computing power, storage, or networking) of your cloud-based applications or service


##### Azure Arc:
- Set of technologies for managing cloud environments.
- Supports various cloud configurations, including public clouds on Azure, private clouds in datacenters, hybrid configurations, and multi-cloud environments.
- Enables centralized management and control across different cloud environments.

##### Azure VMware Solution:
- Enables running VMware workloads in Azure.
- Seamless integration and scalability for VMware-based private cloud environments.
- Facilitates migration from private cloud to public or hybrid cloud.
- Provides a consistent operational model for VMware workloads in Azure.
- [[[AZ] 2.4 VMware]]


