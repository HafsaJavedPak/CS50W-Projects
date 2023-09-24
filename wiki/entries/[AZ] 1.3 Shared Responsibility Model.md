---
tag: Azure, Cloud
---
- In Shared Responsibility Model, responsibility gets shared between the cloud and the customer.
- **Cloud Service Model** is a type of service that cloud providers offer to customers.
    - It describes the resources and capabilities that are available, how customers can access and manage them, and how they are billed.
- The consumer will always be responsible for:
    - The information and data stored in the cloud
    - Devices that are allowed to connect to your cloud (cell phones, computers, and so on)
    - The accounts and identities of the people, services, and devices within your organization
- The cloud provider is always responsible for:
    - The physical datacentre
    - The physical network
    - The physical hosts
- Your service model will determine responsibility for things like:
    - Operating systems
    - Network controls
    - Applications
    - Identity and infrastructure

![[Shared Responsibility Model.png]]
- "accounts and identities" primarily deals with the management
    - of user accounts,
    - access controls,
    - permissions,
- "identity and infrastructure" refers to the broader management of identity-related infrastructure and services within a cloud environment, including
    - directory services,
    - authentication mechanisms,
    - the underlying systems that support identity management.
    

### Overview of IaaS, PaaS, SaaS


| SaaS  | PaaS | IaaS | On-Premises |  |
| --- | --- | --- | --- | --- |
| Customer | Customer | Customer | Customer | Data |
| Microsoft | Customer | Customer | Customer | Application |
| Microsoft | Azure | Customer | Customer | Runtime |
| Microsoft | Azure | Customer | Customer | OS |
| Microsoft | Azure | Azure | Customer | H/V |
| Microsoft | Azure | Azure | Customer | Compute |
| Microsoft | Azure | Azure | Customer | Network |
| Microsoft | Azure | Azure | Customer | Storage |
