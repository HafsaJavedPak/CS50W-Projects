---
tag: Cloud, Azure
---

#### Introduction to Windows Virtual Desktop (WVD)

- Azure Virtual Desktop (AVD) is a desktop and app virtualization solution offered by Microsoft on Microsoft Azure.
	- formerly known as Windows Virtual Desktop (WDI).
- PaaS
- It provides a fully managed desktop and app virtualization solution in the cloud.
- AVD works with various applications and devices, including Windows, Mac, iOS, Android, and modern web browsers.

#### Benefits of Desktop Virtualization

- Desktop virtualization enables central management and security of user desktops.
- It separates the operating system, data, and apps from local hardware, running them on remote servers.
- The main benefit is reducing the risk of confidential information being left on personal devices.
- Virtualization allows running virtual machines in close proximity to apps and services connecting to the data centre or the cloud.
- End-users can connect with any device over the internet, while IT focuses on securing the network connection.

#### Challenges of Traditional Desktop Virtualization

- Setting up a desktop virtualization environment has been complex and expensive.
- Users often lacked the productivity experience of a locally provisioned desktop.
- Implementation could take weeks or even months to complete.

#### Overview of Windows Virtual Desktop

- Azure Virtual Desktop simplifies desktop virtualization by providing a fully managed service on Azure.
- It includes essential components such as gateway, [[[AZ-900] Broker|broker]], diagnostics, and load balancing. 
- VMs in the Windows Virtual Desktop service communicate over a secure [[[AZ-900] Outbound connection|outbound connection]].
- Users have unlimited capacity and can choose any size VM in Azure, adjusting user density based on workload.
- Windows 10 or 11 Enterprise multi-session allows multiple users on a single VM, supporting modern apps.
- The service enables the deployment of full desktops, remote apps, or a combination of both.
- Scalability is flexible, allowing users to scale up or down as needed, and pay only for what they use.
- AVD also provides a more consistent experience with broader application support compared to Windows Server-based operating systems.
	- By assigning each user their individual virtual machine (VM) running on either Windows 10 or Windows 11, a familiar desktop environment is provided, ensuring a consistent user experience regardless of the device or location.
	- AVD supports running multiple Windows operating system versions and allows for more flexibility in application compatibility.


#### Enhanced security 

- Centralized security management with Azure Active Directory (Azure AD)
- Enable multifactor authentication for secure user sign-ins
- Assign granular role-based access controls (RBACs) to users
- Data and apps are separated from local hardware
- Desktop and apps run in the cloud, reducing the risk of confidential data on personal devices
- Isolated user sessions in both single and multi-session environments


#### User Experience and Device Compatibility

- Azure Virtual Desktop provides a seamless user experience comparable to locally hosted desktops.
- Users have access to their full collection of apps, including line-of-business apps and productivity tools.
- Apps are fully integrated with the start menu and can be pinned to the taskbar.
- The virtual app experience closely resembles running local apps, with minimal indications of virtualization.
- Users can copy, paste, or snap windows outside the virtual desktop.
- The experience is consistent across devices, supporting PCs, Macs, iPads, iPhones, Android phones, and web browsers.

#### Conclusion and Further Resources

- Azure Virtual Desktop simplifies desktop virtualization, offering a secure and scalable solution on Azure.
- Organizations can prepare, deploy, and optimize Windows Virtual Desktop with guidance provided in the series.
- By leveraging Windows Virtual Desktop, organizations can achieve a more efficient, productive, and secure desktop virtualization approach.
