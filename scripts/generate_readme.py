from pathlib import Path


def generate_img_tag(file):
    return f'<img src="png/{file.name}" alt="{file.stem}" width="50">'


if __name__ == "__main__":
    imgs = sorted(Path("../png").glob("*.png"))
    img_tags = [generate_img_tag(x) for x in imgs]

    with open("README.md", "wt", encoding="UTF-8") as f:
        f.write("# Dashboard Icons\n\n")
        f.write("### The best Dashboards:\n\n")
        f.write("- [Homer Dashboard](https://github.com/bastienwirtz/homer)\n")
        f.write("- [Heimdall](https://github.com/linuxserver/Heimdall)\n")
        f.write("- [Organizr (v2)](https://github.com/causefx/Organizr)\n")
        f.write("- [Dashy](https://github.com/Lissy93/dashy)\n")
        f.write("- [Flame](https://github.com/pawelmalak/flame)\n")
        f.write("- [SUI](https://github.com/jeroenpardon/sui)\n\n\n")
        f.write(
            "##### [How to download images on UNIX?](#how-to-download-images-on-unix)\n\n\n")
        f.write(" ".join(img_tags))
        f.write("\n\n\n")
        f.write("---\n\n### How to download images on UNIX?\n\n\n`UNIX`\n\n```bash\n\n$ curl https://raw.githubusercontent.com/WalkxCode/dashboard-icons/master/png/example.png > example.png\n\n```\nor\n```bash\n\n$ wget https://raw.githubusercontent.com/WalkxCode/dashboard-icons/master/png/example.png -O example.png\n\n```")
        f.write("\n\n\n---\n\n## Trademark Legal Notices\n\n(Almost) All product names, trademarks and registered trademarks in the images in this repository, are property of their respective owners. All images in this repository are used by the users of the Dashboard Icons project for identification purposes only.\n\n\nThe use of these names, trademarks and brands appearing in these image files, do not imply endorsement.")
