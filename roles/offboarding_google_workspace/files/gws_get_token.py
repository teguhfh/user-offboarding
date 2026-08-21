#!/usr/bin/env python3

import argparse
from google.oauth2 import service_account
import google.auth.transport.requests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sa-key-file", required=True)
    parser.add_argument(
        "--subject",
        required=False,
        help="Admin email to impersonate"
    )
    # Space-separated, the same shape the OAuth2 scope parameter uses.
    # signOut needs admin.directory.user.security on top of the user scope.
    parser.add_argument("--scope", required=True)
    args = parser.parse_args()

    if args.subject:
        credentials = service_account.Credentials.from_service_account_file(
            args.sa_key_file,
            scopes=args.scope.split(),
            subject=args.subject,
        )
    else:
        credentials = service_account.Credentials.from_service_account_file(
            args.sa_key_file,
            scopes=args.scope.split(),
        )

    request = google.auth.transport.requests.Request()
    credentials.refresh(request)

    print(credentials.token)


if __name__ == "__main__":
    main()
