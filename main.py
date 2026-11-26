#!/usr/bin/env python3
"""make.fun bounty entry: One Word, One Username, One Reward.

One word. One username. One reward. The word is the username,
and the username is the whole joke.
"""

USERNAME = "caffeinated-and-shipping"


def username():
    """Return the one-word username for this bounty."""
    return USERNAME


def main():
    print(username())


if __name__ == "__main__":
    main()
