```
sumit [ ~ ]$ username=adminuser$RANDOM
```

password="SecretPassword@123$RANDOM"
```
sumit [ ~ ]$ echo $password
```

SecretPassword@12325674

```
sumit [ ~ ]$ az network vnet create \
  -n vm-vnet \
  -g $group \
  -l centralindia \
  --address-prefixes '192.168.0.0/16' \
  --subnet-name subnet \
  --subnet-prefixes '192.168.1.0/24'
```
{
  "newVNet": {
    "addressSpace": {
      "addressPrefixes": [
        "192.168.0.0/16"
      ]
    },
    "enableDdosProtection": false,
    "etag": "W/\"c7255a7a-92db-4933-97f0-51ae7479615c\"",
    "id": "/subscriptions/57b0d4b6-5bdd-426a-9c32-cf07e91dcb05/resourceGroups/rsg-adf-demo/providers/Microsoft.Network/virtualNetworks/vm-vnet",
    "location": "centralindia",
    "name": "vm-vnet",
    "privateEndpointVNetPolicies": "Disabled",
    "provisioningState": "Succeeded",
    "resourceGroup": "rsg-adf-demo",
    "resourceGuid": "7d0ec08a-5c26-4033-85bd-3e2b9631356d",
    "subnets": [
      {
        "addressPrefix": "192.168.1.0/24",
        "delegations": [],
        "etag": "W/\"c7255a7a-92db-4933-97f0-51ae7479615c\"",
        "id": "/subscriptions/57b0d4b6-5bdd-426a-9c32-cf07e91dcb05/resourceGroups/rsg-adf-demo/providers/Microsoft.Network/virtualNetworks/vm-vnet/subnets/subnet",
        "name": "subnet",
        "privateEndpointNetworkPolicies": "Disabled",
        "privateLinkServiceNetworkPolicies": "Enabled",
        "provisioningState": "Succeeded",
        "resourceGroup": "rsg-adf-demo",
        "type": "Microsoft.Network/virtualNetworks/subnets"
      }
    ],
    "type": "Microsoft.Network/virtualNetworks",
    "virtualNetworkPeerings": []
  }
}


```
sumit [ ~ ]$ az vm create \
  -n vm-sql \
  -g $group \
  -l centralindia \
  --size Standard_D2s_v3 \
  --image MicrosoftSQLServer:SQL2019-WS2019:Standard:latest \
  --admin-username $username \
  --admin-password $password \
  --vnet-name vm-vnet \
  --subnet subnet \
  --public-ip-address ""
```


The default value of '--size' will be changed to 'Standard_D2s_v5' from 'Standard_DS1_v2' in a future release.
Consider upgrading security for your workloads using Azure Trusted Launch VMs. To know more about Trusted Launch, please visit https://aka.ms/TrustedLaunch.
{
  "fqdns": "",
  "id": "/subscriptions/57b0d4b6-5bdd-426a-9c32-cf07e91dcb05/resourceGroups/rsg-adf-demo/providers/Microsoft.Compute/virtualMachines/vm-sql",
  "location": "centralindia",
  "macAddress": "00-22-48-6E-B4-DA",
  "powerState": "VM running",
  "privateIpAddress": "192.168.1.4",
  "publicIpAddress": "",
  "resourceGroup": "rsg-adf-demo"
}


```
sumit [ ~ ]$ az vm open-port -g $group --name vm-sql --port 1433
```
{
  "defaultSecurityRules": [
    {
      "access": "Allow",
      "description": "Allow inbound traffic from all VMs in VNET",
      "destinationAddressPrefix": "VirtualNetwork",
      "destinationAddressPrefixes": [],
      "destinationPortRange": "*",
      "destinationPortRanges": [],
      "direction": "Inbound",
      "etag": "W/\"ba9e2262-b65e-4136-aba2-3da94919fc5c\"",
      "id": "/subscriptions/57b0d4b6-5bdd-426a-9c32-cf07e91dcb05/resourceGroups/rsg-adf-demo/providers/Microsoft.Network/networkSecurityGroups/vm-sqlNSG/defaultSecurityRules/AllowVnetInBound",
      "name": "AllowVnetInBound",
      "priority": 65000,
      "protocol": "*",
      "provisioningState": "Succeeded",
      "resourceGroup": "rsg-adf-demo",
      "sourceAddressPrefix": "VirtualNetwork",
      "sourceAddressPrefixes": [],
      "sourcePortRange": "*",
      "sourcePortRanges": [],
      "type": "Microsoft.Network/networkSecurityGroups/defaultSecurityRules"
    },
    {
      "access": "Allow",
      "description": "Allow inbound traffic from azure load balancer",
      "destinationAddressPrefix": "*",
      "destinationAddressPrefixes": [],
      "destinationPortRange": "*",
      "destinationPortRanges": [],
      "direction": "Inbound",
      "etag": "W/\"ba9e2262-b65e-4136-aba2-3da94919fc5c\"",
      "id": "/subscriptions/57b0d4b6-5bdd-426a-9c32-cf07e91dcb05/resourceGroups/rsg-adf-demo/providers/Microsoft.Network/networkSecurityGroups/vm-sqlNSG/defaultSecurityRules/AllowAzureLoadBalancerInBound",
      "name": "AllowAzureLoadBalancerInBound",
      "priority": 65001,
      "protocol": "*",
      "provisioningState": "Succeeded",
      "resourceGroup": "rsg-adf-demo",
      "sourceAddressPrefix": "AzureLoadBalancer",
      "sourceAddressPrefixes": [],
      "sourcePortRange": "*",
      "sourcePortRanges": [],
      "type": "Microsoft.Network/networkSecurityGroups/defaultSecurityRules"
    },
    {
      "access": "Deny",
      "description": "Deny all inbound traffic",
      "destinationAddressPrefix": "*",
      "destinationAddressPrefixes": [],
      "destinationPortRange": "*",
      "destinationPortRanges": [],
      "direction": "Inbound",
      "etag": "W/\"ba9e2262-b65e-4136-aba2-3da94919fc5c\"",
      "id": "/subscriptions/57b0d4b6-5bdd-426a-9c32-cf07e91dcb05/resourceGroups/rsg-adf-demo/providers/Microsoft.Network/networkSecurityGroups/vm-sqlNSG/defaultSecurityRules/DenyAllInBound",
      "name": "DenyAllInBound",
      "priority": 65500,
      "protocol": "*",
      "provisioningState": "Succeeded",
      "resourceGroup": "rsg-adf-demo",
      "sourceAddressPrefix": "*",
      "sourceAddressPrefixes": [],
      "sourcePortRange": "*",
      "sourcePortRanges": [],
      "type": "Microsoft.Network/networkSecurityGroups/defaultSecurityRules"
    },
    {
      "access": "Allow",
      "description": "Allow outbound traffic from all VMs to all VMs in VNET",
      "destinationAddressPrefix": "VirtualNetwork",
      "destinationAddressPrefixes": [],
      "destinationPortRange": "*",
      "destinationPortRanges": [],
      "direction": "Outbound",
      "etag": "W/\"ba9e2262-b65e-4136-aba2-3da94919fc5c\"",
      "id": "/subscriptions/57b0d4b6-5bdd-426a-9c32-cf07e91dcb05/resourceGroups/rsg-adf-demo/providers/Microsoft.Network/networkSecurityGroups/vm-sqlNSG/defaultSecurityRules/AllowVnetOutBound",
      "name": "AllowVnetOutBound",
      "priority": 65000,
      "protocol": "*",
      "provisioningState": "Succeeded",
      "resourceGroup": "rsg-adf-demo",
      "sourceAddressPrefix": "VirtualNetwork",
      "sourceAddressPrefixes": [],
      "sourcePortRange": "*",
      "sourcePortRanges": [],
      "type": "Microsoft.Network/networkSecurityGroups/defaultSecurityRules"
    },
    {
      "access": "Allow",
      "description": "Allow outbound traffic from all VMs to Internet",
      "destinationAddressPrefix": "Internet",
      "destinationAddressPrefixes": [],
      "destinationPortRange": "*",
      "destinationPortRanges": [],
      "direction": "Outbound",
      "etag": "W/\"ba9e2262-b65e-4136-aba2-3da94919fc5c\"",
      "id": "/subscriptions/57b0d4b6-5bdd-426a-9c32-cf07e91dcb05/resourceGroups/rsg-adf-demo/providers/Microsoft.Network/networkSecurityGroups/vm-sqlNSG/defaultSecurityRules/AllowInternetOutBound",
      "name": "AllowInternetOutBound",
      "priority": 65001,
      "protocol": "*",
      "provisioningState": "Succeeded",
      "resourceGroup": "rsg-adf-demo",
      "sourceAddressPrefix": "*",
      "sourceAddressPrefixes": [],
      "sourcePortRange": "*",
      "sourcePortRanges": [],
      "type": "Microsoft.Network/networkSecurityGroups/defaultSecurityRules"
    },
    {
      "access": "Deny",
      "description": "Deny all outbound traffic",
      "destinationAddressPrefix": "*",
      "destinationAddressPrefixes": [],
      "destinationPortRange": "*",
      "destinationPortRanges": [],
      "direction": "Outbound",
      "etag": "W/\"ba9e2262-b65e-4136-aba2-3da94919fc5c\"",
      "id": "/subscriptions/57b0d4b6-5bdd-426a-9c32-cf07e91dcb05/resourceGroups/rsg-adf-demo/providers/Microsoft.Network/networkSecurityGroups/vm-sqlNSG/defaultSecurityRules/DenyAllOutBound",
      "name": "DenyAllOutBound",
      "priority": 65500,
      "protocol": "*",
      "provisioningState": "Succeeded",
      "resourceGroup": "rsg-adf-demo",
      "sourceAddressPrefix": "*",
      "sourceAddressPrefixes": [],
      "sourcePortRange": "*",
      "sourcePortRanges": [],
      "type": "Microsoft.Network/networkSecurityGroups/defaultSecurityRules"
    }
  ],
  "etag": "W/\"ba9e2262-b65e-4136-aba2-3da94919fc5c\"",
  "id": "/subscriptions/57b0d4b6-5bdd-426a-9c32-cf07e91dcb05/resourceGroups/rsg-adf-demo/providers/Microsoft.Network/networkSecurityGroups/vm-sqlNSG",
  "location": "centralindia",
  "name": "vm-sqlNSG",
  "networkInterfaces": [
    {
      "id": "/subscriptions/57b0d4b6-5bdd-426a-9c32-cf07e91dcb05/resourceGroups/RSG-ADF-DEMO/providers/Microsoft.Network/networkInterfaces/VM-SQLVMNIC",
      "resourceGroup": "RSG-ADF-DEMO"
    }
  ],
  "provisioningState": "Succeeded",
  "resourceGroup": "rsg-adf-demo",
  "resourceGuid": "4f4411b3-fbda-4ce3-bb6c-c74155e2c1ec",
  "securityRules": [
    {
      "access": "Allow",
      "destinationAddressPrefix": "*",
      "destinationAddressPrefixes": [],
      "destinationPortRange": "22",
      "destinationPortRanges": [],
      "direction": "Inbound",
      "etag": "W/\"ba9e2262-b65e-4136-aba2-3da94919fc5c\"",
      "id": "/subscriptions/57b0d4b6-5bdd-426a-9c32-cf07e91dcb05/resourceGroups/rsg-adf-demo/providers/Microsoft.Network/networkSecurityGroups/vm-sqlNSG/securityRules/default-allow-ssh",
      "name": "default-allow-ssh",
      "priority": 1000,
      "protocol": "Tcp",
      "provisioningState": "Succeeded",
      "resourceGroup": "rsg-adf-demo",
      "sourceAddressPrefix": "*",
      "sourceAddressPrefixes": [],
      "sourcePortRange": "*",
      "sourcePortRanges": [],
      "type": "Microsoft.Network/networkSecurityGroups/securityRules"
    },
    {
      "access": "Allow",
      "destinationAddressPrefix": "*",
      "destinationAddressPrefixes": [],
      "destinationPortRange": "1433",
      "destinationPortRanges": [],
      "direction": "Inbound",
      "etag": "W/\"ba9e2262-b65e-4136-aba2-3da94919fc5c\"",
      "id": "/subscriptions/57b0d4b6-5bdd-426a-9c32-cf07e91dcb05/resourceGroups/rsg-adf-demo/providers/Microsoft.Network/networkSecurityGroups/vm-sqlNSG/securityRules/open-port-1433",
      "name": "open-port-1433",
      "priority": 900,
      "protocol": "*",
      "provisioningState": "Succeeded",
      "resourceGroup": "rsg-adf-demo",
      "sourceAddressPrefix": "*",
      "sourceAddressPrefixes": [],
      "sourcePortRange": "*",
      "sourcePortRanges": [],
      "type": "Microsoft.Network/networkSecurityGroups/securityRules"
    }
  ],
  "tags": {},
  "type": "Microsoft.Network/networkSecurityGroups"
}

```
sumit [ ~ ]$ az sql vm create \
  -n vm-sql \
  -g $group \
  -l centralindia \
  --license-type PAYG \
  --connectivity-type PRIVATE \
  --sql-mgmt-type Full \
  --sql-auth-update-username $username \
  --sql-auth-update-pwd $password \
  --port 1433
```
Argument 'sql_management_mode' has been deprecated and will be removed in a future release.
Resource provider 'Microsoft.SqlVirtualMachine' used by this operation is not registered. We are registering for you.
Registration succeeded.
{
  "id": "/subscriptions/57b0d4b6-5bdd-426a-9c32-cf07e91dcb05/resourceGroups/rsg-adf-demo/providers/Microsoft.SqlVirtualMachine/sqlVirtualMachines/vm-sql",
  "leastPrivilegeMode": "Enabled",
  "location": "centralindia",
  "name": "vm-sql",
  "provisioningState": "Succeeded",
  "resourceGroup": "rsg-adf-demo",
  "sqlImageOffer": "SQL2019-WS2019",
  "sqlImageSku": "Standard",
  "sqlManagement": "Full",
  "sqlServerLicenseType": "PAYG",
  "tags": {},
  "virtualMachineResourceId": "/subscriptions/57b0d4b6-5bdd-426a-9c32-cf07e91dcb05/resourceGroups/rsg-adf-demo/providers/Microsoft.Compute/virtualMachines/vm-sql"
}




