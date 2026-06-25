#!/usr/bin/env python3
import argparse
import sys
from google.oauth2 import service_account
import google.auth.transport.requests

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sa-key-file", required=True)
    parser.add_argument("--subject", required=True, help="Admin email to impersonate")
    parser.add_argument("--scope", required=True)
    args = parser.parse_args()

    credentials = service_account.Credentials.from_service_account_file(
        args.sa_key_file,
        scopes=[args.scope],
        subject=args.subject,
    )

    request = google.auth.transport.requests.Request()
    credentials.refresh(request)

    print(credentials.token)

if __name__ == "__main__":
    main()