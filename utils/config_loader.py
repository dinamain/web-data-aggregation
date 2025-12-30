import yaml

def load_site_config(site_name):
    with open("config/sites.yaml", "r") as f:
        config = yaml.safe_load(f)

    if site_name not in config:
        raise ValueError(f"Site '{site_name}' not found in config")

    return config[site_name]
