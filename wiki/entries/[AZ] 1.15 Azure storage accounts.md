---
tag: Azure, Cloud
---


###### non-core and Core storage services

Azure core storage services are the basic data services that Azure Storage platform provides for modern data storage scenarios. They include:

- **Azure Blobs**: A massively scalable object store for text and binary data[1](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction)[2](https://www.testpreptraining.com/tutorial/what-are-core-azure-storage-services/).
- **Azure Files**: Managed file shares for cloud or on-premises deployments[1](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction).
- **Azure Queues**: A messaging store for reliable messaging between application components[1](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction)[2](https://www.testpreptraining.com/tutorial/what-are-core-azure-storage-services/).
- **Azure Tables**: A NoSQL store for schemaless storage of structured data[1](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction)[2](https://www.testpreptraining.com/tutorial/what-are-core-azure-storage-services/).
- **Azure Disks**: Block-level storage volumes for Azure VMs[1](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction).

There are also other storage services that are not core services, such as:

- **Azure Data Lake Storage**: Massively scalable and secure data lake for your high-performance analytics workloads[1](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction)[3](https://azure.microsoft.com/en-us/products/category/storage/).
- **Azure NetApp Files**: Enterprise-grade Azure file shares, powered by NetApp[1](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction)[3](https://azure.microsoft.com/en-us/products/category/storage/).
- **Azure File Sync**: Hybrid cloud file shares for caching your on-premises data[1](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction)[3](https://azure.microsoft.com/en-us/products/category/storage/).
- **Azure Stack Edge**: Cloud storage gateway to transfer data efficiently and easily between the cloud and the edge[1](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction)[3](https://azure.microsoft.com/en-us/products/category/storage/).
- **Azure Data Box**: Appliances and solutions for transferring data into and out of Azure quickly and cost-effectively[1](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction)[3](https://azure.microsoft.com/en-us/products/category/storage/).
- **Azure Elastic SAN (preview)**: A fully integrated solution that simplifies deploying, scaling, managing, and configuring a SAN in Azure[1](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction).

 

###### Distributed acess in Azure Blob storage 
  
In the context of Azure Blob Storage, "distributed access" refers to the capability of serving and accessing data from multiple locations or users simultaneously. It means that the stored data in Blob Storage can be accessed from different applications, services, or users across various geographical locations or network endpoints.

When data is stored in Azure Blob Storage, it becomes accessible via a unique URL (Uniform Resource Locator). This URL allows applications or users to retrieve the data from Blob Storage over the internet. Since the data is stored in the cloud, it can be accessed and served to users or applications from anywhere with an internet connection.

For example, if you have a website hosted in one region and you store images or documents in Azure Blob Storage, those images or documents can be accessed and served directly to the website visitors from anywhere in the world. This is especially useful for scenarios where you want to distribute content to a global audience or serve data to different applications running in different region

- The Azure Storage service endpoint is the URL that you use to access the specific services within your storage account. Each service in the storage account, such as Blob Storage, File Storage, Table Storage, and Queue Storage, has its own unique service endpoint.

###### namespace ? 
 
In Azure, a namespace is a logical container used to organize and manage multiple resources of the same type. It acts as a unique identifier for a set of related resources and provides a way to group them together for easier management and administration.

> A storage account provides a unique namespace for your Azure Storage data that's accessible from anywhere in the world over HTTP or HTTPS : 
 
In Azure, a storage account is a unique namespace that acts as a container for your Azure Storage data. It provides a way to store and manage various types of data, such as blobs, files, tables, and queues. Each storage account is associated with a globally unique name, and this name becomes part of the URL that allows access to the data stored in the account.

When you create a storage account in Azure, you choose a name for the account. This name must be unique across all existing storage accounts in Azure. Once the storage account is created, you can use it as a central repository to store and manage your data.


###### In ZRS,  No remounting of Azure file shares from the connected clients is required
In the context of Azure File Storage with Zone-Redundant Storage (ZRS), "remount" refers to the process of reconnecting or reestablishing a connection between a client machine and the Azure file share after a failover event or any disruption to the storage infrastructure.

With ZRS, the failover process is transparent to the connected clients. When a failover occurs, the Azure platform automatically handles the redirection of client requests to the available replica in another zone without requiring clients to take any action. This means that the clients do not need to remount or reconfigure their connections to the Azure file share. The transition between the primary and secondary replicas is seamless, and the connected clients can continue to access the file share as if nothing happened.

 


###### Data Lake Storage

######  network file system (NFS) in Azure Files

###### types of storage account

###### Storage account endpoints