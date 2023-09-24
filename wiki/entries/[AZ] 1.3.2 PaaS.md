---
tag: Cloud, Azure
---
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

![[Shared Responsibility Model.png]]

---

- well suited to provide a complete development environment without the headache of maintaining all the development infrastructure.
- PaaS is like using a domain joined machine: IT maintains the device with regular updates, patches, and refreshes.
- **Services in PaaS** include :
    1. VMs,
    2. Azure Container Instances (ACI),
    3. Azure Kubernetes Services (AKS), 
    4. or App Services. e.g. :
        1.  https based website,
        2. endpoints,
        3. mobile APIs that I want to access.
- Serverless Computing is a PaaS service.
    - Normally in **IaaS**, you pay for the VMs that you use, but in Serverless, you pay for the work that is done to achieve goal of a particular function.
- ********************Serverless********************
    - Serverless is an event-driven approach where functions are triggered in response to events (e.g., file uploads, REST API calls).
    - There is no need to manage or provision servers or virtual machines; the customer is charged only for the actual execution of the function.
    - It allows for highly granular billing based on the consumed CPU cycles and memory.
- **Cloud Provider Responsibilities** :
    1. same as IaaS
    2. OS maintenance
    3. Middleware
    4. Development tools,
    5. Business intelligence services
    6. Databases
- **Customer Responsibilities** :
    1. Data
    2. Applications
    
    > So you have access this deploying apps, which makes it less flexible than IaaS. But you also have a lot of options, such as choice of whether to deploy on Windows or Linux, Java (any version) or .NET.
    > 
- **Shared responsibilities** :
Following depend on the configuration
    1. Networking settings and connectivity within your cloud environment
    2. Network and application security
    3. Directory infrastructure 
- **Examples** :
    1. **Development framework** :
        - PaaS provides a framework that developers can build upon to develop or customize cloud-based applications.
        - Cloud features such as scalability, high-availability, and multi-tenant capability are included, reducing the amount of coding that developers must do.
        - Multi-tenant capability refers to the ability of a software application or service to serve multiple customers or tenants on a shared infrastructure.
    2. **Analytics or business intelligence** :
    Tools provided as a service with PaaS allow organizations to
        - analyse and mine their data,
        - finding insights and patterns
        - predicting outcomes to improve
            - forecasting,
            - product design decisions,
            - investment returns,
            - and other business decisions.
    3. For s**erverless event-driven workloads** with minimal administration, consider Azure Functions or Logic Apps, depending on the use case.
    4. For **web-based** applications with a focus on minimizing responsibilities, Platform as a Service (PaaS), such as Azure App Service, is a good fit.
    5. For **container-based workloads** with auto-scaling and rich networking requirements, use Azure Kubernetes Service (AKS) for container orchestration.
