---
tag: Cloud, Azure
---

#### Resource Groups:
- **Resources**:
  - Azure is a platform where you can create, provision, and deploy various resources.
  - Resources can include VMs, databases, and cognitive services.

- **Cognitive Services**:
  - Cognitive services are a collection of cloud-based APIs and services provided by Microsoft Azure.
  - They enable adding intelligent features and capabilities to applications without extensive knowledge in ML or AI.

- **Resource Groups**:
  - Resources can be grouped into resource groups to create structure and manage them effectively.
  - A resource group can contain multiple resources from multiple regions.
  - Resource groups cannot be nested.

- **Reasons for Resource Groups**:
	- Policies, [[[AZ-900] 2.1.1.1 Role-Based Access Control|role-based access control]], and budget can be applied to resource groups.
		- **<span style='color:#eb3b5a'>NOTE</span>** : All of these got inherited by the resources within that resource group to which they are applied. 
	- These characteristics are inherited by all resources within the resource group.
	- Resources within the same resource group have the same life cycle, so they can be provisioned and de-provisioned together. 

- **Communication between Resources**:
	- Resources in different resource groups can communicate if they are part of the same virtual network or connected through network-level connectivity mechanisms.
	- Appropriate network security controls can restrict communication between resource groups.
	- Azure provides features like virtual network service endpoints and private endpoints.
	- These features allow further control and secure communication between resources.

- **Further Points**
	- Resource Group has its won metadata.
	- So, when you create a resource group in a region, only its metadata lives within that region. 
	- therefore you can have resources from multiple regions
	
	- 

