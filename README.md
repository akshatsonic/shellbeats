# Shellbeats command hook
preexec_shellbeats() {
    # Store the command that's about to be executed
    SHELLBEATS_LAST_CMD=$1
}

precmd_shellbeats() {
    local exit_status=$?
    if [ -n "$SHELLBEATS_LAST_CMD" ]; then
        # Run the sound in the background
        (`python` `core.py` "$SHELLBEATS_LAST_CMD" &) >/dev/null 2>&1
        SHELLBEATS_LAST_CMD=""
    fi
    return $exit_status
}

# Add the hooks
preexec_functions+=(preexec_shellbeats)
precmd_functions+=(precmd_shellbeats)