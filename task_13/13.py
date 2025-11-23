from ipaddress import ip_network

def analyze_network(ip_with_mask):
    network = ip_network(ip_with_mask, strict=False)
    hosts = list(network.hosts())
    
    return f"""
Анализ сети: {ip_with_mask}
════════════════════════════════
• Адрес сети:        {network.network_address}
• Широковещательный: {network.broadcast_address}
• Маска сети:        {network.netmask}
• Длина префикса:    /{network.prefixlen}
• Всего адресов:     {network.num_addresses}
• Доступные устройства: {len(hosts)}
• Первое устройство:   {hosts[0] if hosts else 'N/A'}
• Последнее устройство: {hosts[-1] if hosts else 'N/A'}
• Диапазон устройств:  {hosts[0] if hosts else 'N/A'} - {hosts[-1] if hosts else 'N/A'}
"""

result = analyze_network("192.168.1.0/27")
print(result)
