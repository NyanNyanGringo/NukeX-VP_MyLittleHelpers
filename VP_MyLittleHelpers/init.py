import os


class InstrumentState:
    # User can choose whether to use the instrument or not
    USER_DEFAULTS = "user_defaults"

    # User can change the state of the instrument with GUI.
    # Instrument will be automatically enabled/disabled when Nuke starts up.
    ENABLE_AT_STARTUP = "enable_at_startup"
    DISABLE_AT_STARTUP = "disable_at_startup"

    # User cannot change the state of the instrument with GUI (action will be disabled).
    # Instrument will be automatically enabled/disabled when Nuke starts up.
    ALWAYS_ENABLED = "always_enabled"
    ALWAYS_DISABLED = "always_disabled"


# If necessary - set the path to the configuration file for Little Helpers
# os.environ["LITTLE_HELPERS_CONFIG_PATH"] = "/your/studio/config/path"


# Set the initial state for each instrument
os.environ["LITTLE_HELPERS_SMART_AUTOSAVE"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_DEFAULT_VIEWER_STATE_IS_INPUT"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_READ_WRITE_COLORIZER"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_COMPARE_VERSIONS_BEFORE_RENDER"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_DISCONNECT_VIEWERS_INPUTS_WHEN_SCRIPT_LOAD"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_DELETE_TEMP_FILES_AFTER_RENDER"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_CONFIG_EDITOR"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_VIEWER_BESIDE"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_LINEAR_ANIMATION"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_SHOW_SHORTCUTS_IN_TAB_MENU"] = InstrumentState.USER_DEFAULTS
os.environ["LITTLE_HELPERS_VERSION_UP_REMINDER"] = InstrumentState.USER_DEFAULTS
