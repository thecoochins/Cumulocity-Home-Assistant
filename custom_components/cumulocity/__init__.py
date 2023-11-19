"""
Sample integration repository for [HACS](https://github.com/custom-components/hacs).
"""
DOMAIN = "cumulocity"

async def async_setup(hass, config):
    """Set up the Cumulocity integration."""
    # Perform any setup tasks here
    return True

async def async_setup_entry(hass, entry):
    """Set up the Cumulocity entry."""
    # Perform setup for a specific entry (user configuration)
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )

    return True

async def async_unload_entry(hass, entry):
    """Unload a Cumulocity entry."""
    # Unload resources associated with the entry
    hass.async_create_task(
        hass.config_entries.async_forward_entry_unload(entry, "sensor")
    )

    return True
