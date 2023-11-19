import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_PASSWORD

# Define the schema for the Cumulocity IoT configuration.
CONFIG_SCHEMA = vol.Schema({
    vol.Required("base_url"): str,
    vol.Required("tenant"): str,
    vol.Required("username"): str,
    vol.Required(CONF_PASSWORD): str,
})

class CumulocityConfigFlow(config_entries.ConfigFlow, domain="cumulocity"):
    """Cumulocity IoT Configuration Flow."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            # Store the configuration data in the options entry.
            title = "Cumulocity IoT"
            data = user_input
            return self.async_create_entry(title=title, data=data)

        return self.show_form()

    async def show_form(self, errors=None):
        """Show the configuration form to the user."""
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(CONFIG_SCHEMA),
            errors=errors or {},
        )

    async def async_step_config_entry(self, config_entry):
        """Handle the configuration entry options."""
        if config_entry.source == config_entries.SOURCE_IMPORT:
            return self.async_abort(reason="Configuration via YAML not supported.")

        if self.source == config_entries.SOURCE_REAUTH:
            # Reauth is not supported.
            return self.async_abort(reason="Reauthentication is not supported.")

        # Configure the options flow for additional settings, including password.
        return await self.async_step_options()

    async def async_step_options(self, user_input=None):
        """Handle the options flow."""
        if user_input is not None:
            # Update the options with the user's input.
            self.hass.config_entries.async_update_entry(
                self.config_entry,
                options=user_input,
            )
            return self.async_create_entry(title="", data={})

        return self.async_show_form(
            step_id="options",
            data_schema=vol.Schema(CONFIG_SCHEMA),
            description_placeholders={"title": self.config_entry.title},
        )

    async def async_step_remove(self, user_input=None):
        """Handle removal of the entry."""
        if user_input is not None:
            return await self.async_remove_entry(entry=self.config_entry)

        return self.async_show_form(step_id="remove_confirm")

# Example YAML configuration for the configuration.yaml file.
# cumulocity:
#   base_url: "https://your-cumulocity-instance.com"
#   tenant: "your-tenant-id"
#   username: "your-username"
#   password: "your-password"
