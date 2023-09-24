---
tag: Cloud, Azure
---

### <mark style="background: #BBFABBA6;">1. High availability</mark>

- High availability focuses on ensuring maximum availability, regardless of disruptions or events that may occur.
- While architecting a solution, service availability guarantees are taken into account. These guarantees are part of the service-level agreements (SLAs).
    - If a service is made up of multiple services, each service then has its own SLA.
- Azure is a highly available cloud environment with uptime guarantees depending on the service. The most common plans are 99%, 99.9%, 99.95% and 99.99%.

### <mark style="background: #BBFABBA6;">2. Scalability</mark>

- Scalability refers to the ability to adjust resources to meet demand
- **Benefits :**
    - add more resources to better handle the increased demand.
    - you aren't overpaying for services.
- **Vertical Scaling** :
    - aka scaling up or scaling vertically.
    - involves increasing or decreasing the capacity of an individual resource within a system.
    - i.e. upgrading or downgrading the specifications of a single server or instance e.g. e.g. memory, CPU power, storage etc.
        - upgrading or downgrading the specifications of a single server or instance e.g. e.g. memory, CPU power, storage etc.
    - is suitable when the application or workload can be effectively managed within a single server.
    - is often used when the scalability requirements are moderate, and the focus is on optimizing the performance and capacity of an individual server.
- **Horizontal Scaling :**
    - aka scaling out or scaling horizontally.
    - focuses on expanding the system by adding more identical resources in parallel.
    - to handle increased workloads.
    - This approach allows for better load distribution, improved fault tolerance, and increased overall performance.
    - commonly used to accommodate high-traffic websites, distributed applications, or systems that require high availability.
    - is suitable when the workload cannot be efficiently handled by a single server or when there is a need for high availability and fault tolerance.

### <mark style="background: #BBFABBA6;">3. Reliability</mark>

- ability of a system to recover from failures and continue to function.
- one of the pillars of the Microsoft Azure Well-Architected Framework.
- Applications can be designed to benefit from the high reliability of cloud.
    - Cloud has a decentralized design.
    - Therefore, resources can be deployed in multiple regions of world.
    - So, in the case of a catastrophic event in one region, resources are still available.
- The following features support Reliability :
    1. Auto healing
        - e.g. Redeployment of VM to another node, server, region etc. incase of a rack/ service level failure.
    2. Storage
        - 3 min copies of your data ❓❓❓❓❓❓❓❓❓ r they supposed to happen or auto happen
    3. SLAs
        - financially backed commitment from azure for that service.
    4. Design for failure
        - Active Active over multiple regions
        - Active Passive over multiple regions
        - Active with a backup to another region


##### <mark style="background: #BBFABBA6;">4. Predictability</mark>
- Predictability in the cloud provides confidence and enables informed decision-making.
- It encompasses performance and cost predictability.
- Microsoft Azure Well-Architected Framework significantly influences both aspects.
- The following features support predictability : 
	1. [[[AZ] 2.8 SKU|SKU]]
		- Stock Keeping Units, unique identifier to distinguish btw diff products or services in terms of their specs, characteristics or pricing.
		- ❓❓❓❓❓❓❓❓
	2. Behaviour
		- Only specific interactions btw the components in a cloud environment  are allowed.
		- e.g. different APIs, certain tools, templates, predictable price based on region. ❓❓❓❓❓❓❓
	3. Use [[[AZ] 2.1 Set Templates| Set Templates]] 
		- Some of the reliability built into Azure also comes inti the predictability aspect but we have to be predictable as well. Hence, we should use set templates. 
		- Advantages: Automation, DevOps. ❓❓❓❓❓❓❓❓ 

+ **Performance Predictability:**
	- focuses on predicting the resources needed for a positive customer experience.
	- Cloud concepts such as autoscaling, load balancing, and high availability support performance predictability.
	- Autoscaling can deploy additional resources to meet increased demand and scale back when demand decreases.
	- Load balancing helps redirect traffic from overloaded areas to less stressed areas.
+ **Cost Predictability:**
	- Cost predictability focuses on forecasting the cost of cloud spend.
	- Real-time tracking of resource usage and monitoring resources for efficiency contribute to cost predictability.
	- Data analytics can be applied to identify patterns and trends for better resource deployment planning.
	- Operating in the cloud and utilizing cloud analytics allow for predicting future costs and adjusting resources accordingly.
	- Tools like [[[AZ-900] Total Cost of Ownership (TCO) vs Pricing Calculator|Total Cost of Ownership (TCO) or Pricing Calculator]] can provide estimates of potential cloud spend.

#### <mark style="background: #BBFABBA6;">5. Governance</mark> 
- involves implementing policies and controls to ensure compliance, accountability, and effective management of cloud resources.
+ Accountability is important to ensure that the responsible individuals or teams are identified and held responsible for the actions they take in managing cloud resources.
+ Effective management of cloud resources involves putting in place processes, procedures, and controls to optimize resource usage, ensure security, and maintain compliance with organizational policies and regulatory requirements.
+ Cloud features support governance and compliance.
+ [[[AZ] 2.1 Set Templates| Set Templates]] ensure deployed resources meet corporate standards and regulatory requirements.
+ Updates can be applied to deployed resources as standards change.
- [[[AZ] 2.2 Cloud-based Auditing| Cloud-based auditing]] identifies non-compliant resources and provides mitigation strategies.
- Software patches and updates can be automatically applied based on the operating model.
###### Establishing Good Governance
- Early establishment of a strong governance footprint is crucial.
- It helps keep the cloud footprint updated, secure, and well-managed.
- Governance helps in maintaining control and oversight over cloud resources, managing risks, and ensuring that resources are used efficiently and in alignment with organizational goals and policies.

#### <mark style="background: #BBFABBA6;">6. Security :</mark>

- Choose a cloud solution that matches your security needs.
- Infrastructure as a Service (IaaS) provides maximum control over security.
- Platform as a Service (PaaS) or Software as a Service (SaaS) handle patches and maintenance automatically.
- Cloud providers are well-equipped to handle distributed **[[[AZ] 2.3 Denial of Service (DDos) Attacks|denial of service (DDoS) attacks]]**.
- Cloud delivery enhances network robustness and security.


#### <mark style="background: #BBFABBA6;">7. Management </mark>
+ **Management of the cloud** 
	speaks to managing your cloud resources. In the cloud, you can:
	- Automatically scale resource deployment based on need.
	- Deploy resources based on a preconfigured template, removing the need for manual configuration.
	- Monitor the health of resources and automatically replace failing resources.
		- In cloud computing, resources such as servers, storage systems, or network components can occasionally fail due to hardware issues, software bugs, or other factors.
	- Receive automatic alerts based on configured metrics, so you’re aware of performance in real time.
+ **Management in the cloud**
	how you’re able to manage your cloud environment and resources. 
	+ You can manage these:
		- Through a web portal.
		- Using a command line interface.
		- Using APIs.
		- Using PowerShell.