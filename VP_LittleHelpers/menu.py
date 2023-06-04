from nuke import NUKE_VERSION_MAJOR


if NUKE_VERSION_MAJOR < 13:
    print("VP_LittleHelpers: supports Nuke13.0 or higher.")
else:
    import little_helpers.menu
