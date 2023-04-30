#!/bin/sh

git filter-branch --env-filter '
export GIT_AUTHOR_NAME="idrni"
export GIT_AUTHOR_EMAIL="idrni@icloud.com"
' --tag-name-filter cat -- --branches --tags

# This has been used to fix git from my old email/incorrect (: