import requests
from typing import Optional

colors_to_hex = {
    "bright_red": "#FF0000",
    "bright_blue": "#0000FF",
    "bright_green": "#00FF00",
}

hex_to_colors = {
    "#FF0000": "bright_red",
    "#0000FF": "bright_blue",
    "#00FF00": "bright_green",
}


class ColorUtilities:
    """ 
    The color utilities handling all the color utilities.

    Parameters
    -------------
    enable_experimental_features: :class:`bool`
        Whether to enable experimental features (alpha and beta features).
    """

    def __init__(self, enable_experimental_features: bool):
        self._color_list = [color for color in colors_to_hex.keys()]
        self._url = "https://www.thecolorapi.com/"
        self.enable_experimental_features: bool = enable_experimental_features

    def color_to_hex(color: str) -> str:
        """
        Converts a specified color to an equivalent hex.

        Parameters
        -------------
        color: :class:`str`
            The color to be converted to hex.

        Returns
        -------------
        :class:`str`
            An equivalent hex of the specified color.
        """

        try:
            if colors_to_hex.get(color) is None:
                raise ColorNotFoundError("This color does not exist in the list of colors!")
            else:
                return colors_to_hex.get(color)
        except:
            raise ColorUtilitiesError("An unexpected error occured!")

    def hex_to_color(hex: str) -> str:
        """
        Converts a specified hex to an equivalent color.

        Parameters
        -------------
        hex: :class:`str`
            The hex to be converted to color.

        Returns
        -------------
        :class:`str`
            An equivalent color of the specified hex.
        """

        try:
            if hex.startswith("#"):
                hex = hex[1:]

            request_url = self._url + f"id?hex={hex}"

            r = requests.get(request_url)

            data = r.json()

            return data["name"]["value"]
        except:
            raise HexNotFoundError("This hex does not exist in the list of hexes!")