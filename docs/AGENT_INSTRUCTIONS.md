# Agent Workflow Instructions

This document outlines the standard operating procedure for agents working on this repository.

## Documentation Structure

*   **`docs/PROJECT_CONTEXT.md`**: Shared, high-level overview of the project state, tech stack, and recent progress. This is the "Source of Truth" for the project's overall status.
*   **`docs/logs/log_<user_id>.md`**: Individual, granular log of code changes and tool outputs for a specific developer/agent.
    *   *Filename convention:* Sanitize the git user email (replace `@` and `.` with `_`).
    *   *Example:* `docs/logs/log_a081127_naver_com.md`
*   **`docs/AGENT_INSTRUCTIONS.md`**: These instructions.

## The Development Loop

### 1. Start of Task - Identity & Context
*   **Identify User:** Run `git config user.email` to determine your identity and locate your specific log file in `docs/logs/`.
*   **Read Shared Context:** Read `docs/PROJECT_CONTEXT.md` to understand high-level goals and recent project-wide history.
*   **Read Personal Log:** Read your specific `docs/logs/log_<user_id>.md`.
    *   Check for unfinished work in the "Current Task" section.
    *   *(Future)* Check this file for user-specific preferences (languages, formatting, etc.).

### 2. During Development
*   **Record Changes:** As you modify files or run important commands, append a brief note to the `## Current Task` section in **your individual log file**.
    *   *Format:* `- [Time/Step]: Description of change (File modified)`

### 3. Pre-Commit / Completion
Before running `git commit`, perform the "Log Rotation":

1.  **Summarize for Context:** Create a concise summary of the items in your `## Current Task`.
2.  **Update Shared Context:** Add this summary to `docs/PROJECT_CONTEXT.md` under the `## Recent Progress` section.
    *   **Important:** Insert the new summary at the *top* of the list (immediately after the header) to maintain reverse chronological order.
    *   *Do not* overwrite the entire file. Use targeted replacement or insertion.
3.  **Archive Personal Log:** Move the content from `## Current Task` to the `## History` section in your `docs/logs/log_<user_id>.md`.
    *   Insert at the top of the `## History` section (reverse chronological).
    *   Clear the `## Current Task` section so it is empty for the next task.

### 4. Git Commit
*   Include the documentation updates (your log and the shared context) in your commit.