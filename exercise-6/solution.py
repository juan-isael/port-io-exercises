import os
import json
import logging
import requests

# --------------------------------------------------
# Configuration
# --------------------------------------------------

BASE_URL = "https://api.port.io/v1"
TOKEN_URL = f"{BASE_URL}/auth/access_token"
FRAMEWORKS_URL = f"{BASE_URL}/blueprints/frameworks/entities"
SERVICES_URL = f"{BASE_URL}/blueprints/service/entities"

CLIENT_ID = os.getenv("PORT_CLIENT_ID")
CLIENT_SECRET = os.getenv("PORT_CLIENT_SECRET")

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")


# --------------------------------------------------
# Token and headers
# --------------------------------------------------

def get_access_token() -> str:
    """Authenticate against Port API and return access token."""
    payload = {
        "clientId": CLIENT_ID,
        "clientSecret": CLIENT_SECRET,
    }

    response = requests.post(TOKEN_URL, json=payload)
    response.raise_for_status()

    return response.json()["accessToken"]


def authorized_headers(token: str) -> dict[str, str]:
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": token,
    }


# --------------------------------------------------
# Data fetching
# --------------------------------------------------

def get_frameworks(headers: dict[str, str]) -> dict[str, str]:
    
    """
    Returns a dict:
    {
        framework_identifier: state
    }
    """
    response = requests.get(FRAMEWORKS_URL, headers=headers)
    response.raise_for_status()

    frameworks = {}
    for entity in response.json()["entities"]:
        frameworks[entity["identifier"]] = entity["properties"]["state"][0]

    return frameworks


def get_services(headers: dict[str, str]) -> list[dict]:
    response = requests.get(SERVICES_URL, headers=headers)
    response.raise_for_status()
    return response.json()["entities"]


# --------------------------------------------------
# EOL count
# --------------------------------------------------

def count_eol_frameworks(
    service_frameworks: list[str],
    frameworks_state: dict[str, str],
) -> int:
    return sum(
        1
        for fw in service_frameworks
        if frameworks_state.get(fw) == "EOL"
    )


def build_service_payloads(
    services: list[dict],
    frameworks_state: dict[str, str],
) -> list[dict]:
    result = []

    for service in services:
        frameworks_used = service["relations"]["frameworks"]
        eol_count = count_eol_frameworks(frameworks_used, frameworks_state)

        result.append(
            {
                "identifier": service["identifier"],
                "eol_packages": eol_count,
            }
        )

    return result


# --------------------------------------------------
# Update Port Service entities
# --------------------------------------------------

def update_service_eol(
    service_id: str,
    eol_packages: int,
    headers: dict[str, str],
) -> None:
    url = f"{SERVICES_URL}/{service_id}"

    payload = {
        "properties": {
            "number_of_eol_packages": eol_packages
        }
    }

    response = requests.patch(url, headers=headers, json=payload)
    response.raise_for_status()

    logging.info(
        "Updated service %s with %s EOL packages",
        service_id,
        eol_packages,
    )


# --------------------------------------------------
# Main
# --------------------------------------------------

def main() -> None:
    token = get_access_token()
    headers = authorized_headers(token)

    frameworks_state = get_frameworks(headers)

    logging.info("FRAMEWORKS ENTITIES AND STATE")
    logging.info(json.dumps(frameworks_state, indent=2))

    services = get_services(headers)

    service_payloads = build_service_payloads(
        services, frameworks_state
    )

    logging.info("SERVICE ENTITIES IDENTIFIER AND EOL SUMMARY:")
    logging.info(json.dumps(service_payloads, indent=2))

    for service in service_payloads:
        update_service_eol(
            service["identifier"],
            service["eol_packages"],
            headers,
        )


if __name__ == "__main__":
    main()
