import pathlib
from pathlib import Path
root = pathlib.Path(__file__).parent.resolve()
readme_path = root / 'README.md'


def generate_img_tag(file):
    return f'<img src="png/{file.name}" alt="{file.stem}" width="50">'


if __name__ == "__main__":
    imgs = sorted(Path("./png").glob("*.png"))
    img_tags = [generate_img_tag(x) for x in imgs]

    with open(readme_path, "wt", encoding="UTF-8") as f:
        f.write("<p align = \"center\" >\n")
        f.write("  <h3 align = \"center\" > Dashboard Icons </h3>\n")
        f.write("\n")
        f.write("  <p align = \"center\" >\n")
        f.write("    Dashboard Icons for your selfhosted services.\n")
        f.write(" <br/>\n")
        f.write(
            "    <a href = \"#icons\" > <strong > Get icons »</strong> </a>\n")
        f.write(
            "    <a href = \"https://ko-fi.com/walkx\" > <img src = \"https://ko-fi.com/img/githubbutton_sm.svg\" > </a>\n")
        f.write("</p>\n")
        f.write("\n")
        f.write("# Table of Contents\n")
        f.write("- [Table of Contents](#table-of-contents)\n")
        f.write("- [Getting Started](#getting-started)\n")
        f.write("  - [Dashboards](#dashboards)\n")
        f.write("  - [Installation](#installation)\n")
        f.write("- [Icons](#icons)\n")
        f.write("- [Legal](#legal)\n")
        f.write("\n")
        f.write("<!-- GETTING STARTED -->\n")
        f.write("# Getting Started\n")
        f.write("\n")
        f.write("## Dashboards\n")
        f.write("\n")
        f.write(
            "There's multiple Dashboards available. Here are some of the popular ones.\n")
        f.write("\n")
        f.write("- [Dashy*](https://github.com/Lissy93/dashy)\n")
        f.write(
            "- [Homer Dashboard](https://github.com/bastienwirtz/homer)\n")
        f.write("- [Heimdall](https://github.com/linuxserver/Heimdall)\n")
        f.write("- [Organizr(v2)](https://github.com/causefx/Organizr)\n")
        f.write("- [Flame](https://github.com/pawelmalak/flame)\n")
        f.write("- [SUI](https://github.com/jeroenpardon/sui)\n")
        f.write("\n")
        f.write("## Installation\n")
        f.write(
            "_*Dashy natively supports all icons in this repo, and is synced automatically. (Clicking [this link](https://github.com/Lissy93/dashy/blob/master/docs/icons.md#home-lab-icons) will take you to the docs that explain how to use the integration.)_\n")
        f.write("\n")
        f.write("To download an icon, simple `Right click > Save image`.\n")
        f.write("\n")
        f.write(
            "For non-desktop operating systems, or people that prefer to use terminal.\n")
        f.write("```sh\n")
        f.write("$ curl https://raw.githubusercontent.com/walkxhub/dashboard-icons/master/png/example.png > example.png\n")
        f.write("```\n")
        f.write("or\n")
        f.write("```sh\n")
        f.write("$ wget https://raw.githubusercontent.com/walkxhub/dashboard-icons/master/png/example.png - O example.png\n")
        f.write("```\n")
        f.write("\n")
        f.write("<!-- ICONS -->\n")
        f.write("# Icons\n")
        f.write(" ".join(img_tags))
        f.write("\n\n")
        f.write("<!-- LEGAL -->\n")
        f.write("# Legal\n")
        f.write("(Almost) All product names, trademarks and registered trademarks in the images in this repository, are property of their respective         owners. All images in this repository are used by the users of the Dashboard Icons project for identification purposes only.\n")
        f.write("\n")
        f.write("The use of these names, trademarks and brands appearing in these image files, do not imply endorsement.\n")
