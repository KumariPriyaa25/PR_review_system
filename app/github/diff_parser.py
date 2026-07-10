class DiffParser:

    def parse(self, files):
        parsed_files = []

        for file in files:

            filename = file["filename"]
            patch = file.get("patch")

            if not patch:
                continue

            added_lines = []

            for line in patch.splitlines():

                if line.startswith("+") and not line.startswith("+++"):
                    added_lines.append({
                        "code": line[1:]
                    })

            parsed_files.append({
                "filename": filename,
                "added_lines": added_lines
            })

        return parsed_files