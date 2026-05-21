import requests


def handle_get_request(
    url: str, parameters: dict[str, str] | None = None
) -> requests.Response:
    """
    Handle responses status codes.

    Handle the status codes GET requests's responses,
    by returning the response if status code is OK and throwing
    a base Exception with an error message in any other case.

    Parameters
    ----------
    url : str
        Url to send the GET request.
    parameters : dict [str, str] | None
        url parameters (default is None).

    Returns
    -------
    request.Response
        A request.Response object.

    Examples
    --------
    url = "kittens-photos.com"
    try:
        response = handle_get_request(url)
    except Exception as e:
        print(f"An exception occured with msg: {e}")
    photos = response.content
    """
    response = requests.get(url, params=parameters)
    if response.status_code == 200:
        return response
    else:
        raise Exception(
            f"An error occured with status code {response.status_code}: {response.reason}"
        )
