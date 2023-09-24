---
tag: Cloud, Azure
---

| SaaS  | PaaS | IaaS | On-Premises |  
| --- | --- | --- | --- | --- |
| Customer | Customer | Customer | Customer | Data |
| Microsoft | Customer | Customer | Customer | Application |
| Microsoft | Azure | Customer | Customer | Runtime |
| Microsoft | Azure | Customer | Customer | OS |
| Microsoft | Azure | Azure | Customer | H/V |
| Microsoft | Azure | Azure | Customer | Compute |
| Microsoft | Azure | Azure | Customer | Network |
| Microsoft | Azure | Azure | Customer | Storage |

![[Shared Responsibility Model.png]]

---

- most flexible category of cloud services.
- max control over cloud resources = largest share of responsibility on customer
- **Cloud Provider Responsibilities** :
    1. Hardware (Compute)
    2. Network connectivity (to the internet)
    3. Physical Security
- **Customer responsibilities** :
    1. OS installation
    2. OS configuration
    3. OS maintenance
    4. Network configuration
    5. Database and storage configuration
    6. Patching and Updates
    7. Security (e.g. Antivirus)

> ********NOTE******** : it doesn’t mean that the customer has to do everything alone. There are extensions in Azure to help u.
> 
- **Examples** :
    1. **Lift-and-shift migration** : users replicate their on-premises datacentre resources in the IaaS infrastructure.
    2. **Testing and development environments** that require rapid replication and control over configurations.
