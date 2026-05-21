import requests


def handle_get_request(
    url: str, parameters: dict[str, str] | None = None
) -> requests.Response:
    response = requests.get(url, params=parameters)
    if response.status_code == 200:
        return response
    else:
        raise Exception(
            f"An error occured with status code {response.status_code}: {response.reason}"
        )
