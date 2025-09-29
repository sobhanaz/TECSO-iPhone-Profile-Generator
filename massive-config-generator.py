import uuid

# TECSO Massive Config Generator
# Network configuration templates

network_configs = {
    "All Network": {
        # All Network config settings will be added here
    },
    "Hamrah Aval": {
        # Hamrah Aval config settings will be added here
    },
    "Irancell": {
        # Irancell config settings will be added here
    },
    "Rightel": {
        # Rightel config settings will be added here
    },
}

def main():
    print("🚀 TECSO Massive Config Generator")
    print("=" * 40)
    
    # Config selection
    print("Please select a configuration:")
    for index, config_name in enumerate(network_configs.keys(), start=1):
        print(f"{index}. {config_name}")

    try:
        selected_index = int(input("\nEnter the number of your desired config: "))
        selected_config_name = list(network_configs.keys())[selected_index - 1]
        selected_config = network_configs[selected_config_name]
        
        print(f"\nSelected: {selected_config_name}")
        
        # Proxy settings
        need_proxy = input("Do you need proxy settings? (yes/no): ").strip().lower()
        if need_proxy in ['yes', 'y']:
            proxy_server = input("Enter proxy server address: ")
            proxy_port = int(input("Enter proxy port: "))
        else:
            proxy_server = ""
            proxy_port = 0

        # Generate unique IDs using uuid library
        num_uuids = int(input("How many UUIDs do you want to generate? (default: 5): ") or "5")
        unique_ids = [str(uuid.uuid4()) for _ in range(num_uuids)]

        # Add unique IDs to config
        selected_config["UniqueIDs"] = unique_ids

        # Add proxy settings if needed
        if need_proxy in ['yes', 'y']:
            selected_config["ProxyServer"] = proxy_server
            selected_config["ProxyPort"] = proxy_port

        # Display final config
        print(f"\n🎯 Final Configuration for {selected_config_name}:")
        print("-" * 50)
        print("Generated UUIDs:")
        for i, uid in enumerate(unique_ids, 1):
            print(f"  {i}. {uid}")
        
        if need_proxy in ['yes', 'y']:
            print(f"\nProxy Settings:")
            print(f"  Server: {proxy_server}")
            print(f"  Port: {proxy_port}")
        
        print(f"\n✅ Configuration ready for {selected_config_name}")
        print("© 2025 TECSO Team - Professional Mobile Solutions")
        
    except (ValueError, IndexError) as e:
        print(f"❌ Error: Invalid selection. Please try again.")
    except KeyboardInterrupt:
        print(f"\n👋 Goodbye!")

if __name__ == "__main__":
    main()
