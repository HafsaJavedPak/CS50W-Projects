
---
tag: Cloud, Azure
---

### <mark style="background: #D2B3FFA6;">Azure Virtual Machines (VMs):
</mark>

- IaaS
- They virtualize the hardware, hence, the user can focus on developing the OD, and software.
- Azure virtual machines are one of several types of [on-demand, scalable computing resources](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree) that Azure offers.
- Each Azure Virtual Machine (VM) is intended to be used by a single user or workload.
- The pay-as-you-go model with VMs and containers means that you are charged based on the actual usage of the allocated resources. If you have idle VMs or containers, you won't be billed for CPU or memory usage, but you will still incur storage costs and may pay for unused allocated resources.
- Suitable for scenarios requiring 
	1. total control over the OS 
	2. running custom software
	3. use custom hosting configs 

#### <mark style="background: #D2B3FFA6;">Scaling VMs in Azure</mark>

- While single VMs are suitable for testing, development, and smaller workloads; grouping VMs enable high availability, scalability and [[[AZ] 2.0 Important Terms|redundancy]].
- Azure can also manage this grouping for the user in the following ways : 
	1. Virtual Machine Scale Sets
	2. Virtual Machine Availability Sets

##### <mark style="background: #D2B3FFA6;">1. Virtual Machine Scale Sets</mark>

- Virtual machine scale sets let you create and manage a group of identical, load-balanced VMs.
- Automatic scaling based on demand or defined schedule.
- Automatic deployment of load balancers for efficient resource utilization.
- VM scale sets can be used to build large-scale services for areas such as 
	- compute, 
	- big data,
	- container workloads.

##### <mark style="background: #D2B3FFA6;">2. Virtual Machine Availability Sets</mark>

- Virtual machine availability sets are another tool to help you build a more resilient, highly available environment.
- When an availability set is created, Azure automatically distributes the virtual machines across these update domains and fault domains to provide resiliency and high availability.
	1. **Update Domains**
		- The update domain groups VMs that can be rebooted at the same time.
		- An update group going through the update process is given a 30-minute time to recover before maintenance on the next update domain starts.
		- Update domains are distributed across different fault domains. ❓
	2. **Fault Domains**
		-  The fault domain groups your VMs by common power source and network switch.
- No additional cost for configuring availability sets. Cost is incurred for created VM instances.
- By default, the number of update domains in an availability set is five, but you can increase it up to 20. The number of fault domains in an availability set varies by region, but it can be up to three. These configurations can’t be changed once the availability set has been created.

#### <mark style="background: #D2B3FFA6;">Characteristics of VMs</mark>

1. **Resource utilization and improved ROI:**
   - Multiple VMs can run on a single physical computer, allowing better utilization of hardware and maximizing return on investment.
   - return on investment (ROI)

2. **Scale:**
   - Cloud computing enables easy deployment of multiple copies of the same virtual machine to handle increased workload.

3. **Portability:**
   - VMs can be moved among physical computers in a network, allowing workload allocation based on available computing power.
   - VMs can also be migrated between on-premises and cloud environments, enabling hybrid cloud scenarios.
   - However, they are less portable than containers.

4. **Flexibility:**
   - Creating a VM is faster and easier compared to installing an OS on a physical server.
   - VMs can be cloned with the OS already installed, allowing quick creation of new environments as needed.

5. **Security:**
   - VMs offer enhanced security compared to operating systems running directly on hardware.
   - VMs can be scanned for malicious software, and snapshots of VMs can be taken and restored if infected with malware.
   - VMs can be easily deleted and recreated to expedite recovery from malware infections.

#### <mark style="background: #D2B3FFA6;">Downsides of VMs:</mark>

1.  VMs can only run one operating system at a time.
   
2. **Multiple Runtime Environments:**
   - If you have multiple server applications that require different runtime environments, such as different versions of programming frameworks or libraries, separate VMs are needed for each application.
   - This can lead to increased management complexity and resource overhead, as each VM runs its own operating system instance.	
   - **runtime environments** : such as different versions of programming languages or frameworks

3. **Resource Consumption:**
   - Running multiple VMs with separate operating systems consumes more resources, including CPU, memory, and storage.
   - This can result in higher costs and inefficient resource utilization, especially when the applications have varying levels of resource requirements.

4. **Start ups and Snapshot Time:**
   - VMs require the entire operating system to boot and initialize when started or when taking a snapshot.
   - This process can take several minutes, impacting the agility and responsiveness of the infrastructure.
   - It also increases the time required for tasks such as scaling or recovering from failures.
   - **snapshot** : a copy of the VM's state at a specific point in time



